from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('', views.UserView.as_view(), name='user_view'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Password
    path("password-change/", views.ChangePasswordView.as_view(), name="change_password_view"),
    path("password-reset-email/", views.PasswordResetView.as_view(), name="password_reset_email_view"),
    path("password-reset/<uidb64>/<token>/", views.PasswordTokenCheckView.as_view(), name="password_reset_confirm_view"),
    path("password-reset-complete/", views.SetNewPasswordView.as_view(), name="password_reset_complete_view"),
    
]