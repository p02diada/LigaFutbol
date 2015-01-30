from django.conf.urls import patterns, url
from gestionEquipos import views
from django.contrib.auth.decorators import login_required


urlpatterns=patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
	url(r'^primero/$', views.mostrarPrimero, name='mostrarPrimero'),


	#url(r'^listaEquipos/$', views.listaEquipos, name='listaEquipos'),
	url(r'^listaEquipos/$', views.listaEquipos.as_view(), name='listaEquipos'),

	#url(r'^equipos/(?P<equipo_id>\d+)/$', views.mostrarEquipo, name='equipo'),
	url(r'^equipos/(?P<usuario_id>\d+)/$', views.mostrarEquipo.as_view(), name='equipo'),

	#url(r'^listaJugadores/$', views.listaJugadores, name='listaJugadores'),
	url(r'^listaJugadores/$', views.listaJugadores.as_view(), name='listaJugadores'),

	#url(r'^jugador/(?P<jugador_id>\d+)/$', views.mostrarJugador, name='equipo'),
	url(r'^jugador/(?P<jugador_id>\d+)/$', views.mostrarJugador.as_view(), name='equipo'),

	#url(r'^jugador/eliminar/(?P<jugador_id>\d+)/$', views.eliminarJugador, name='equipo'),
	url(r'^jugador/eliminar/(?P<pk>\d+)/$', views.eliminarJugador.as_view(), name='equipo'),


	#url(r'^nuevoEquipo/$', views.nuevoEquipo , name='nuevoEquipo'),
	url(r'^nuevoEquipo/$', views.nuevoEquipo.as_view() , name='nuevoEquipo'),



	url(r'^nuevoJugador/$', views.nuevoJugador, name='nuevoJugador'),
	#url(r'^nuevoJugador/$', views.nuevoJugador.as_view(), name='nuevoJugador'),


	#url(r'^editarJugador/(?P<pk>\d+)/$', views.editarJugador.as_view(), name='editarJugador'),
	url(r'^editarJugador/(?P<pk>\d+)/$', login_required(views.editarJugador.as_view()), name='editarJugador'),




	
	url(r'^editarEquipo/(?P<equipo_id>\d+)/$', views.editarEquipo, name='editarEquipo'),
	url(r'^newUser/$', views.newUser, name='NewUser'),
	url(r'^userlogin/$', views.user_login, name='NewUser'),
	url(r'^userlogout/$', views.user_logout, name='NewUser'),
	

	
	
)
