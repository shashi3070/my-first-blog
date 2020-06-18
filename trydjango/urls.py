"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from products.views import home,callpythonfun,actionUrl,secondcall,PythonRequest
from website.views import index 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls),
    
    # For Website 
    path('', include('website.urls')),
    # End

    path('show/', home,name='home'),
    path('callpython/', callpythonfun,name='callpythonfun'),
    path('callpython/actionUrl/', actionUrl,name='actionUrl'),
    path('callpython/secondcall/', secondcall,name='secondcall'),
    path('callpython/PythonRequest/', PythonRequest,name='PythonRequest'),

]

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)