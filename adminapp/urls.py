"""OnlineFoodOrdering URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from OnlineFoodOrdering import settings
from adminapp import views

urlpatterns = [

  path('',views.showindex,name='admin_main'),
  path('admin_login_check/',views.admin_login_check,name="admin_login_check"),
  path('welcome/',views.welcome,name="welcome"),
  path('state/',views.openState,name="state"),
  path('state_submit/',views.state_submit,name="state_submit"),
  path('state_update/',views.state_update,name="state_update"),
  path('state_update_process/',views.state_update_process,name="state_update_process"),
  path('delete_state/',views.delete_state,name="delete_state"),

  path('city/',views.openCity,name="city"),
  path('city_submit/', views.city_submit, name="city_submit"),
  path('city_update/', views.city_update, name="city_update"),
  path('city_update_process/', views.city_update_process, name="city_update_process"),
  path('delete_city/', views.delete_city, name="delete_city"),



  path('cuisine/',views.openCuisine,name="cuisine"),
  path('cuisine_submit/', views.cuisine_submit, name="cuisine_submit"),
  path('cuisine_update/', views.cuisine_update, name="cuisine_update"),
  path('cuisine_update_process/', views.cuisine_update_process, name="cuisine_update_process"),
  path('delete_cuisine/', views.delete_cuisine, name="delete_cuisine"),

  path('vendor/',views.openVendor,name="vendor"),
  path('reports/',views.openReports,name="reports"),
  path('logout',views.admin_login_check,name="logout"),

]
if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)
