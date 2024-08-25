from django.urls import path, include
from rest_framework import routers

from cats.api.viewsets import CatViewSet, FactViewSet

router = routers.DefaultRouter()
router.register(r"cats", CatViewSet, basename="cats")
router.register(r"fact", FactViewSet, basename="fact")

urlpatterns = [
    path("", include(router.urls))
]