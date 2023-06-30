from django.urls import path, include
from users.views import login, registartion, profile, user_logout

urlpatterns = [
    path('login/', login),
    path('registration/', registartion),
    path('profile/', profile),
    path('logout/', user_logout)
]