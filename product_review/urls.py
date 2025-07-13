
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import ProductViewSet, ReviewViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')

product_router = NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', ReviewViewSet, basename='product-reviews')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('auth/', obtain_auth_token),
]
