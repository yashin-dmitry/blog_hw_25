from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='users/login'),
    path('logout/', LogoutView.as_view(next_page='http://127.0.0.1:8000/'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]