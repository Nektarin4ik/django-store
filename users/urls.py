from django.contrib.auth.decorators import login_required
from django.urls import path

from users.views import (EmailVerificationView, LoginView, UserProfileView,
                         UserRegistrationView, logout)

app_name = 'users'

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('registration', UserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>', login_required(UserProfileView.as_view()), name='profile'),
    path('logout', logout.as_view(), name='logout'),
    path('verify/<str:email>/<str:code>', EmailVerificationView.as_view(), name='verify'),
]

# /<int:id_profile>
