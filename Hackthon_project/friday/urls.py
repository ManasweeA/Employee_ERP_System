from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'friday'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('signup/', views.sign_up, name="sign_up"),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('profile/', views.UserProfilePage.as_view(), name='profile'),
    path('calendar/', views.CalendarPage.as_view(), name='calendar'),
    path('projects/', views.ProjectsPage.as_view(), name='projects')
]