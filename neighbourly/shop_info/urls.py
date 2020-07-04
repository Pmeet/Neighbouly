from django.urls import path
from . import views
from django.conf.urls.static import static
from neighbourly import settings

app_name = 'shop_info'

urlpatterns = [
    path('storepage', views.storeView, name='store_page'),
    path('storepage/<str:id>', views.storeView),
    path('script', views.script),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
