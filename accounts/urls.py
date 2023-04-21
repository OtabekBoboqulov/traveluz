from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('change/<int:pk>', EditProfileView.as_view(), name='change'),
]
