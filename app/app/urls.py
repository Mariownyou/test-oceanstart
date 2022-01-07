from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from products.views import ProductViewSet
from categories.views import CategoryViewSet


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
