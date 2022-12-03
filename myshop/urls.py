from django.contrib import admin
from django.urls import path, include
from shop.views import ProductViewSet, OrderViewSet, ReviweViewSet, ProductCollectionViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Shop API",
        default_version='v1',
        description="My description",
        terms_of_service="https://www.mysite.com/policies/terms/",
        contact=openapi.Contact(email="My_contact@snippets.local"),
        license=openapi.License(name="My License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('orders', OrderViewSet, basename='orders')
router.register('product-reviews', ReviweViewSet, basename='product-reviews')
router.register('product-collections', ProductCollectionViewSet, basename='product-collections')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token, name='auth-token'),
    path('api/v1/auth-token/', include('djoser.urls.authtoken')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
