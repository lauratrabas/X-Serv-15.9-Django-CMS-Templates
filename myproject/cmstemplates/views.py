from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
from django.views.decorators.csrf import csrf_exempt
from django.template.response import TemplateResponse
from django.template.loader import get_template
from django.template import Context, Template, RequestContext
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def buscar(request, identificador):
    try:
        pag = Pages.objects.get(id = int(identificador))
        respuesta = pag.page
    except Pages.DoesNotExist:
        respuesta = "No existe en la base de datos"
    template = get_template('plantilla.html')
    return HttpResponse(template.render(Context({'texto': respuesta})))

def mostrar(request):
    login = administrador(request)
    if login:
        template = get_template('login.html')
        usuario = request.user.username
    else:
        usuario = ""
        template = get_template('nologin.html')
    lista = Pages.objects.all()
    respuesta = "<ol>"
    for pag in lista:
        respuesta += '<li><a href="' + str(pag.id) + '">' + pag.name + '</a>'
    respuesta += "</ol>"
    return HttpResponse(template.render(Context({'usuario':usuario, 'contenidos':respuesta})))

def usuario(request):
    respuesta = "Eres " + request.user.username
    return HttpResponse(respuesta)

@csrf_exempt
def pagina_nueva(request):
    logueado = administrador(request)
    if logueado:
        if request.method == "GET":
            # muestro el formulario
            template = get_template('formulario.html')
            return HttpResponse(template.render(Context({})))

        elif request.method == "POST":
            nombre = request.POST['nombre']
            print "Este es el nombre:" + str(nombre)
            cont = request.POST['contenido']
            print "Este el contenido es: " + str(cont)
            nueva_pag = Pages(name = str(nombre), page = str(cont))
            nueva_pag.save()
            template = get_template('plantilla.html')
            texto = "Pagina anadida correctamente"
        return HttpResponse(template.render(Context({'texto': texto})))
    else:
        template = get_template('plantilla.html')
        texto = "Tienes que registrarte primero"
        return HttpResponse(template.render(Context({'texto': texto})))
