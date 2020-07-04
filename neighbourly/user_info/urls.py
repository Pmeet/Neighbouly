from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from neighbourly import settings
from django.conf.urls.static import static

app_name = 'user_info'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup_customer/',views.SignUp_customer.as_view(),name='signup_customer'),
    path('signup_shopkeeper/',views.SignUp_shopkeeper.as_view(),name='signup_shopkeeper'),
    path('signup_query',views.SignUp_query,name='signup_query'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
