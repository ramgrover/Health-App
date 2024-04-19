"""
URL configuration for healthApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from myapp.views import calculate_days_view,target_weight_view
from myapp.views import home 
from myapp.views import edit_profile, SignUpView,custom_logout



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='home'),
    path('calculate_days/', calculate_days_view, name='calculate_days'),
    #path('profiles/', include('profiles.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),  # Add this line for user registration
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('logout/', custom_logout, name='logout'),
    path('target_weight/<int:weight_input_id>/', target_weight_view, name='target_weight'),
    

]
