from django.shortcuts import render, redirect
from django.http import HttpResponse
from gestionEquipos.models import Equipo, Jugador
from gestionEquipos.forms import EquipoForm, JugadorForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def index(request):
	return HttpResponse ("Hello, world. You're at the polls index.")
def detail(request, question_id):
	return HttpResponse ("You are looking at question %s." % question_id)
def mostrarPrimero(request):
	listaEquipos=Equipo.objects.all()
	equipo=listaEquipos[1]
	return HttpResponse("Equipo: %s. Ciudad: %s" % (equipo.nombre, equipo.ciudad))




#def listaEquipos(request):
#	listaEquipos=Equipo.objects.all().order_by("anyoCreacion")
#	context={'listaEquipos':listaEquipos}
#	return render(request,'gestionEquipos/listaEquipos.html',context)
class listaEquipos(ListView):
	model=Equipo
	template_name = "gestionEquipos/listaEquipos.html"
	context_object_name="listaEquipos"




#def mostrarEquipo(request,equipo_id):
#	equipo=Equipo.objects.get(pk=equipo_id)
#	listaJugadores=Jugador.objects.filter(equipo=equipo)
#	edad=0
#	for jugador in listaJugadores:
#		edad=edad+jugador.edad
#	if len(listaJugadores)>0:
#		edadMedia=edad/len(listaJugadores)
#	else:
#		edadMedia=0
#	context={'equipo':equipo,'listaJugadores':listaJugadores,'edadMedia':edadMedia}
#	return render(request,'gestionEquipos/equipo.html',context)
class mostrarEquipo(DetailView):
	model=Equipo
	template_name="gestionEquipos/equipo.html"
	pk_url_kwarg="usuario_id"



#def listaJugadores(request):
#	listaJugadores=Jugador.objects.all()
#	context={'listaJugadores':listaJugadores}
#	return render(request,'gestionEquipos/listaJugadores.html',context)
class listaJugadores(ListView):
	model=Jugador
	template_name="gestionEquipos/listaJugadores.html"
	context_object_name="listaJugadores"


#def mostrarJugador(request,jugador_id):
#	jugador=Jugador.objects.get(pk=jugador_id)
#	context={'jugador':jugador}
#	return render(request,'gestionEquipos/jugador.html',context)
class mostrarJugador(DetailView):
	model=Jugador
	template_name="gestionEquipos/jugador.html"
	pk_url_kwarg="jugador_id"



#def eliminarJugador(request, jugador_id):
#	jugador=Jugador.objects.get(pk=jugador_id)
#	jugador.delete()
#	return HttpResponse ("Hola, estas en la pagina de eliminacion del jugador %s." % jugador.nombre )
class eliminarJugador(DeleteView):
	model=Jugador
	success_url="/gestionEquipos/listaJugadores/"

#def nuevoEquipo(request):
#	if request.method == 'POST':
#		form = EquipoForm(request.POST,  request.FILES)
#		if form.is_valid():
#			form.save()
#			return redirect('/gestionEquipos/listaEquipos/')
#	else:
#		form= EquipoForm()
#	context = {'form':form}
#	return render(request, 'gestionEquipos/nuevoEquipo.html', context)

class nuevoEquipo(CreateView):
	model=Equipo
	template_name="gestionEquipos/nuevoEquipo.html"
	success_url="/gestionEquipos/listaEquipos/"


def nuevoJugador(request):
	if request.method == 'POST':
		form =JugadorForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/gestionEquipos/listaJugadores/')
	else:
		form= JugadorForm()
	context = {'form':form}
	return render(request, 'gestionEquipos/nuevoJugador.html', context)
#class nuevoJugador(CreateView):
#	model=Jugador
#	template_name="gestionEquipos/nuevoJugador.html"
#	success_url="/gestionEquipos/listaJugadores/"




#def editarJugador(request,jugador_id):
#	jugador=Jugador.objects.get(pk=jugador_id)
#	if request.method == 'POST':
#		form =JugadorForm(request.POST, request.FILES, instance=jugador)
#		if form.is_valid():
#			form.save()
#			return redirect('/gestionEquipos/listaJugadores/')
#	else:
#		form= JugadorForm(instance=jugador)
#	context = {'form':form}
#	return render(request, 'gestionEquipos/nuevoJugador.html', context)
#@login_required(login_url='/gestionEquipos/listaJugadores/')
	
class editarJugador(UpdateView):
	model=Jugador
	template_name="gestionEquipos/editarJugador.html"
	success_url="/gestionEquipos/listaJugadores/"




def editarEquipo(request,equipo_id):
	equipo=Equipo.objects.get(pk=equipo_id)
	if request.method == 'POST':
		form =EquipoForm(request.POST, request.FILES, instance=equipo)
		if form.is_valid():
			form.save()
			return redirect('/gestionEquipos/listaEquipos/')
	else:
		form= EquipoForm(instance=equipo)
	context = {'form':form}
	return render(request, 'gestionEquipos/nuevoEquipo.html', context)

def newUser(request):
	if request.method== 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form=UserCreationForm()
	context = {'form':form}
	return render(request, 'gestionEquipos/newUser.html/', context)
def user_login(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = request.POST['username']
			passwd = request.POST['password']
			access = authenticate(username=user, password=passwd)
			if access is not None:
				if access.is_active:
					login(request, access)
					return redirect('/')
				else:
					return HttpResponse ("User inactive")
			else:
				return HttpResponse ("No user")
	else:
		form = AuthenticationForm()
	context = {'form': form}
	return render(request,'gestionEquipos/login.html', context)



def user_logout(request):
	logout(request)
	return redirect ('/gestionEquipos/userlogin/')
	

# Create your views here.
