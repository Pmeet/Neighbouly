from django.urls import path
from . import views
from django.conf.urls.static import static
from neighbourly import settings


app_name = 'product_info'

urlpatterns = [
    path('category',views.category,name='category'),
    path('category/<str:cat>', views.category),
    path('script',views.script)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
