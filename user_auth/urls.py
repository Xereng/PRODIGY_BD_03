from django.urls import path
from .views import RegisterView, LoginView, ProfileView, ProfileCreateView, AllProfilesView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('profile/create/', ProfileCreateView.as_view()),
    path('profiles/', AllProfilesView.as_view()),  # Admin or allowed users only
]
