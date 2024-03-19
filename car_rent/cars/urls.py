from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register('brands', BrandView, basename='brands')
router.register('car_models', CarModelView, basename='car_models')

urlpatterns = [
    path('', include(router.urls))
]
