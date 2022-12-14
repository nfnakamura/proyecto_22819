
from datetime import datetime 
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from cac.forms import ContactoForm
from django.contrib import messages

# Create your views here.
def index(request):
 
    listado_cursos = [
        {
            'nombre':'Fullstack Java',
            'descripcion':'Curso de Fullstack',
            'categoria':'Programación'
        },
        {
            'nombre':'Diseño UX/IU',
            'descripcion':'🎨',
            'categoria':'Diseño'
        },
        {
            'nombre':'Big Data',
            'descripcion':'test',
            'categoria':'Analisis de Datos'
        },
    ]
    
    if(request.method == 'POST'):
        contacto_form = ContactoForm(request.POST)
       
        if(contacto_form.is_valid()):
            #debería validar y realizar alguna acción
            messages.success(request, 'Muchas gracias por contactarete, te estaremos respondiendo en breve')
            contacto_form=ContactoForm() #instancio para que me limpie el form una vez enviado
        else:
            messages.error(request, 'Por favor revisa los errores')
    else:
        contacto_form = ContactoForm()

    return render(request,'cac/publica/index.html',{
                                        'cursos':listado_cursos,
                                        'contacto_form':contacto_form,
                                        })
   #opcion 1 para renderizar

def quienes_somos(request):
    #return redirect('saludar_por_defeto')
    #return redirect(reverse('saludar', kwargs={'nombre: Roberto'}))
    template = loader.get_template('cac/publica/quienes_somos.html')
    context = {'titulo': 'Codo a Codo - Quienes Somos'}
    return HttpResponse(template.render(context,request))
    #opcion 2 para renderizar

def ver_proyectos(request,anio=2022,mes=1):
    proyectos = []
    return render(request,'cac/publica/proyectos.html',{'proyectos':proyectos})

def ver_cursos(request):
    listado_cursos = [
        {
            'nombre':'Fullstack Java',
            'descripcion':'Curso de Fullstack',
            'categoria':'Programación'
        },
        {
            'nombre':'Diseño UX/IU',
            'descripcion':'🎨',
            'categoria':'Diseño'
        },
        {
            'nombre':'Big Data',
            'descripcion':'test',
            'categoria':'Analisis de Datos'
        },
    ]

    return render(request,'cac/publica/cursos.html',{'cursos':listado_cursos})

def index_administracion(request):
    variable = 'test variable'
    return render(request,'cac/administracion/index_administracion.html',{'variable':variable})


def api_proyectos(request,):
    proyectos = [{
        'autor': 'Gustavo Villegas',
        'portada': 'https://agenciadeaprendizaje.bue.edu.ar/wp-content/uploads/2021/12/Gustavo-Martin-Villegas-300x170.png',
        'url':'https://marvi-artarg.web.app/'
    },{
        'autor': 'Enzo Martín Zotti',
        'portada': 'https://agenciadeaprendizaje.bue.edu.ar/wp-content/uploads/2022/01/Enzo-Martin-Zotti-300x170.jpg',
        'url':'https://hablaconmigo.com.ar/'
    },{
        'autor': 'María Echevarría',
        'portada': 'https://agenciadeaprendizaje.bue.edu.ar/wp-content/uploads/2022/01/Maria-Echevarria-300x170.jpg',
        'url':'https://compassionate-colden-089e8a.netlify.app/'
    },]
    response = {'status':'Ok','code':200,'message':'Listado de proyectos','data':proyectos}
    return JsonResponse(response,safe=False)
# def hola_mundo(request):
#     return HttpResponse('Hola Mundo Django')

# def saludar(request, nombre='Pepe'):
#     return HttpResponse(f"""
#         <h1>Hola Mundo Django - {nombre}</h1>
#         <p>Estoy haciendo mi primera prueba</p>
#     """)

# def ver_proyectos_2022_07(request):
#     return HttpResponse(f"""
#         <h1>proyecto del mes 7 del año 2022</h1>
#         <p>Mis proyectos</p>
#     """)    

# def ver_proyectos(request,anio, mes=1):
#     return HttpResponse(f"""
#         <h1>Proyectos del - {mes}/{anio}</h1>
#         <p>Mis proyectos</p>
#     """)

# def ver_proyectos_anio(request,anio):
#     return HttpResponse(f"""
#         <h1>Proyectos del - {anio}</h1>
#         <p>Mis proyectos</p>
#     """)




# def cursos_detalle(request,nombre_curso):
#     return HttpResponse(f"""
#         <h1>{nombre_curso}</h1>
#     """)

# def cursos(request,nombre):
#     return HttpResponse(f"""
#         <h2>{nombre}</h2>
#     """)