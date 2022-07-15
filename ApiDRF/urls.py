from django.urls import path, re_path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'product', ProductViewSet, basename='product')


urlpatterns = [
    path('v1/drf-auth/', include('rest_framework.urls')), # Session-based authentication
    path('v1/', include(router.urls)),

    ]