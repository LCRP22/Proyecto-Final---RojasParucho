from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, request
from django.template import loader, context
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from devsocial.forms import *
from devsocial.models import *
import datetime
from django.contrib.auth.decorators import login_required


def ver_index(request):
    return render(request, "index.html")

def ver_about(request):
    return render(request, 'about.html')

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "index.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "index.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "index.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "login.html", {"form": form})

def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"index.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"register.html" ,  {"form":form})
@login_required
def ver_blog(request):
    
    return render(request, 'blog.html')
@login_required
def leerblogs(request):

      posts = post.objects.all() #trae todos los profesores

      contexto= {"posts":posts} 

      return render(request, 'blog-copy.html',contexto)
@login_required
def postear(request):
    if request.method == "POST":
    
        miFormulario = Postear(request.POST, request.FILES) # Aqui me llega la informacion del html
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            p = post(usuario=request.user, titulo=informacion["titulo"],contenido=informacion["contenido"],imagen=informacion["imagen"])
            p.save()
            return render(request, "index.html")
    else:
        miFormulario = Postear()
 
    return render(request, "postear.html", {"miFormulario": miFormulario})    

def PostDetalle(request, id):
    blog = post.objects.get(id=id)
    
    comentarios = comentario.objects.all()
    
    if request.method == "POST":
        miComentario = Comentar(request.POST)
        
        if miComentario.is_valid():
            informacion = miComentario.cleaned_data
            c = comentario(nombre=request.user,info=informacion["info"],post=blog.titulo)
            c.save()
            return render(request, "index.html")
    else:
        miComentario = Comentar()
    
    contexto = {"blog":blog,"miComentario":miComentario,"comentarios":comentarios}
    
    return render(request, "post_detalle.html", contexto)

def buscar(request):
    if request.GET['titulo']:
        
        titulo = request.GET['titulo']
        posts = post.objects.filter(titulo__icontains=titulo)
        
        return render(request, 'resultados.html', {'posts':posts, 'titulo':titulo})
        

def eliminar(request, id):
    Post = post.objects.get(id=id)
    Post.delete()
    
    return render(request, 'index.html')

