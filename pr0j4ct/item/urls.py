from django.urls import path 
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'item'
from .models import Data
from django_downloadview import ObjectDownloadView
download = ObjectDownloadView.as_view(model=Data, file_field=
'file')

urlpatterns = [
    path('', views.items, name='items'),  
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    # other URL patterns
   path('download//', download, name="default"),
]
urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


 