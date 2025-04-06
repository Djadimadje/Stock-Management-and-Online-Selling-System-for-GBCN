from django.contrib import admin
from django.urls import path, include  # Ensure you have `include`

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/inventory/', include('inventory.urls')),
    #path('aoi/orders/', include(orders.urls))# This line includes the accounts URLs
    # Include other app URLs as needed
]
