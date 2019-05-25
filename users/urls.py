from users import views
from django.urls import path

app_name = "users"
urlpatterns = [
    path('profile/', views.profile_create, name="profile_create"),
    path('userprofile/',views.user_profile, name="user_profile"),
]
