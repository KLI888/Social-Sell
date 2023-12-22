from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    path('registerPage/', registerPage, name='registerPage'),
    path('aboutusPage/', aboutusPage, name='aboutusPage'),
    path('sellPage/', sellPage, name='sellPage'),
    path('deliveryPage/', deliveryPage, name='deliveryPage'),
    path('followerPage/', followerPage, name='followerPage'),
    path('contactPage/', contactPage, name='contactPage'),
    path('categoryPage/', categoryPage, name='categoryPage'),
    path('productViewPage/<str:ac_name>/', productViewPage, name='productViewPage'),
    path('success/', success, name='success'),
    path('categoryType/<int:id>', categoryType, name='categoryType'),
    path('followersType/<int:id>', followerType, name='followerType'),
]
