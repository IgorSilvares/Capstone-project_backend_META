from django.shortcuts import render
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer, UserSerializer
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer