
from datetime import datetime

from django.shortcuts import render
from django.utils.dateparse import parse_date

from rest_framework import generics, viewsets, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer


def home(request):
    return render(request, "home.html", {})


def about(request):
    return render(request, "about.html")


def menu_list(request):
    menu = Menu.objects.all()
    context = {"menu": menu}
    return render(request, "menu_list.html", context)


def menu_item(request, pk):
    menu_item = Menu.objects.get(pk=pk)
    context = {"menu_item": menu_item}
    return render(request, "menu_item.html", context)


def booking(request):
    return render(request, "booking.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "register.html")


class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.groups.filter(name="Manager").exists()
        )


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.request.method != "GET":
            return [IsAuthenticated(), IsManager()]
        return []


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.request.method != "GET":
            return [IsAuthenticated(), IsManager()]
        return []


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Booking.objects.all()
        date_value = self.request.query_params.get("date")

        if date_value:
            selected_date = parse_date(date_value)
            if selected_date is None:
                return Booking.objects.none()

            queryset = queryset.filter(booking_date__date=selected_date)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        booking_date = request.data.get("booking_date")
        no_of_guests = request.data.get("no_of_guests")

        if not booking_date or not no_of_guests:
            return Response(
                {"error": "Booking date and number of guests are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            parsed_datetime = datetime.fromisoformat(
                booking_date.replace("Z", "+00:00")
            )
        except (ValueError, AttributeError):
            return Response(
                {"error": "Invalid booking date."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Prevent two bookings for the same date and time.
        if Booking.objects.filter(booking_date=parsed_datetime).exists():
            return Response(
                {"error": "This time slot is already booked."},
                status=status.HTTP_409_CONFLICT,
            )

        serializer = self.get_serializer(
            data={
                **request.data,
                "user": request.user.pk,
            }
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"message": "Booking created successfully"},
            status=status.HTTP_201_CREATED,
        )

    def destroy(self, request, *args, **kwargs):
        booking = self.get_object()

        is_manager = request.user.groups.filter(name="Manager").exists()

        if booking.user_id != request.user.id and not is_manager:
            return Response(
                {"error": "You cannot delete this booking."},
                status=status.HTTP_403_FORBIDDEN,
            )

        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
