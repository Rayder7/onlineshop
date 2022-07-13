from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from onlineshop.views import *


urlpatterns = [
    path('', onlineshopHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('product/<slug:product_slug>/', ShowProduct.as_view(), name='product'),
    path('category/<slug:cat_slug>/', ProductCategory.as_view(), name='category'),
    path('api/v1/productlist/', ProductAPIView.as_view()),
    path('api/v1/productlist/<int:pk>/', ProductAPIView.as_view()),
    ]
# from onlineshop.models import *
# from django.db import connection
# connection.queries