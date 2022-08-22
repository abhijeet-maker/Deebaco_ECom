from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('products/', views.product_list),
    path('add_product/', views.add_product),
    path('add_products/', views.add_product),
    path('delete_product/<sku>', views.delete_product),
    path('product_details/<sku>', views.product_detail),
    path('', views.overview),
    path('publish_product/<sku>', views.publish_product),
    path('unpublish_product/<sku>', views.unpublish_product),
]
