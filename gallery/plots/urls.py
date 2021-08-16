from django.urls import path, include
from rest_framework.routers import DefaultRouter
from plots import views

router = DefaultRouter()
router.register('plots', views.PlotsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
