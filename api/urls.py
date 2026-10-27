from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RestaurantViewSet, TableViewSet, TimeSlotViewSet,
    BookingViewSet, MenuItemViewSet
)

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet, basename='restaurant')
router.register(r'tables', TableViewSet, basename='table')
router.register(r'timeslots', TimeSlotViewSet, basename='timeslot')
router.register(r'bookings', BookingViewSet, basename='booking')
router.register(r'menu', MenuItemViewSet, basename='menuitem')

urlpatterns = [
    path('', include(router.urls)),
]

