"""mensajeriaapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from mensajes import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path("registrousuario/",views.registro_usuario,name="registro_usuario"),
    path("usuario/",views.usuario,name="usuario"),
    path("signin/",views.signin,name="signin"),
    path("signout/",views.signout,name="signout"),
    path("registroconversacion/",views.registro_conversacion,name="registro_conversacion"),
    path("mismensajes/",views.mismensajes,name="mismensajes"),
    path("chats/<str:remitente>/",views.listadochat,name="listadochat"),
    path("miperfil/",views.miperfil,name="miperfil"),
 ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)