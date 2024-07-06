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
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.registro_view, name='register'),
    path('update_user/', views.update_user, name='update_user'),
    path('delete_user/', views.delete_user_view, name='delete_user'),
    path('manage_usuarios/', views.manage_usuarios, name='manage_usuarios'),
    path('user/<int:user_id>/edit/', views.find_edit_user, name='find_edit_user'),
    path('user/update/', views.update_user, name='update_user'),
    path('profile/', views.profile_view, name='profile'),
    path('user/<int:user_id>/delete/', views.delete_user_view, name='delete_user_view'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 