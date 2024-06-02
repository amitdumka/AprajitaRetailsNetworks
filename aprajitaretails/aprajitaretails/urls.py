"""
URL configuration for aprajitaretails project.

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

try:
    from rest_framework.authtoken.views import obtain_auth_token
except:
    pass

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/jwt/", view=obtain_auth_token),
    
    path("accounting/", include("accounting.urls")),
    path("banking/", include("banking.urls")),
    path("sales/", include("pos.urls")),
    path("inventory/", include("inventory.urls")),
    path("hr/", include("hrms.urls")),
    path("core/", include("core.urls")),
    path("home/",include("home.urls")),
    path("", include("ui.urls")),
   
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
   # below there line need to be reviews
    path('api-auth/', include('rest_framework.urls')), # Need to check which one is working
    path('dyn/', include('django_dyn_api.urls')),     # <-- NEW
   
]

# Lazy-load on routing is needed
# During the first build, API is not yet generated
try:
    urlpatterns.append(path("api/", include("api.urls"))) # Need to check which one is working
    urlpatterns.append(path("login/jwt/", view=obtain_auth_token)) # Need to check which one is working
   
except:
    pass
 
 # TODO: Note Import either use dynamic api or auto gen api for a particular model not both. 
 #  Note: use dynanic api for models where there is no auto gen pk and post processing is required
 # Note Use Auto gen api for model where auto gen pk is required or any post- pre processing is required
  