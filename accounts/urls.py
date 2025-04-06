from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Djoser built-in routes (register, users, etc.)
    path('', include('djoser.urls')),

    # JWT authentication routes
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),     # Login
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),      # Refresh token
]
