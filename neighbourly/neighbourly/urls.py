"""neighbourly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path
from user_info import urls
from . import views
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('userInfo/',include('user_info.urls')),
    path('userInfo/',include('django.contrib.auth.urls')),
    path('productInfo/',include('product_info.urls')),
    path('shopInfo/',include('shop_info.urls')),
    path('',views.index,name="Home"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
