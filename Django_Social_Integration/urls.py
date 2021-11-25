from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.HomeView.as_view(), name='home'),

    # Login and Logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),  # <-- here
    # path('settings/', views.SettingsView, name='settings'),
    # path('settings/password/', views.password, name='password'),
    path('accounts/', include('allauth.urls')),
]
