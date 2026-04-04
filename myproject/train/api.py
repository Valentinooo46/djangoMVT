from rest_framework import viewsets
from rest_framework.routers import DefaultRouter

from .models import Train, Carriage
from .serializers import TrainSerializer, CarriageSerializer


class TrainViewSet(viewsets.ModelViewSet):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer


class CarriageViewSet(viewsets.ModelViewSet):
    queryset = Carriage.objects.all()
    serializer_class = CarriageSerializer


router = DefaultRouter()
router.register(r'trains', TrainViewSet, basename='train')
router.register(r'carriages', CarriageViewSet, basename='carriage')
