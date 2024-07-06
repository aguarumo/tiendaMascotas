from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('index', views.index, name='index'),
    path('tienda_productos/', views.tienda_productos, name='tienda_productos'),
    path('tienda', views.tienda, name='tienda'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('creacion_producto/', views.creacion_producto, name='creacion_producto'),
    path('admin_index', views.admin_index, name='admin_index'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('editar_producto/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 