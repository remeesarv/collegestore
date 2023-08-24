from django.urls import path, include
from . import views
app_name='collegeapp'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('registration/',views.registration,name='registration'),
    path('login/', views.login, name='login'),
    path('submit/',views.submit,name='submit'),
    path('logout/', views.logout, name='logout'),
]