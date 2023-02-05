from django.urls import path
from devsocial.views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', ver_index, name='index'),
    path('about', ver_about, name='about'),
    path('login', login_request, name='login'),
    path('register', register, name='register'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('blog', leerblogs, name = "leeblogs"),
    path('postear', postear, name='postear'),
    path('postdetalle/<id>/', PostDetalle, name='v'),
    path('buscar/', buscar),
    path('eliminar/<id>',eliminar,name='eliminar'),
]