from django.shortcuts import render, HttpResponse,redirect
from miapp.models import Articulo

def crear_articulo(request, titulo, contenido, publicado):
    articulo = Articulo(
        titulo = titulo,
        contenido = contenido,
        publicado = publicado
    )
    articulo.save()
    return HttpResponse(f"Articulo Creado: {articulo.titulo} - {articulo.contenido}")

def buscar_articulo(request, id):
    try:
        articulo = Articulo.objects.get(id=1000)
        resultado = f"""Articulo:
                    <br> <strong>ID:</strong> {articulo.id}
                    <br> <strong>Título:</strong> {articulo.titulo}
                    <br> <strong>Contenido:</strong> {articulo.contenido}
                        """
    except:
        resultado = "<h1> Artículo No Encontrado </h1>"
    return HttpResponse(resultado)

def editar_articulo(request, id):
    articulo = Articulo.objects.get(pk=id)
    articulo.titulo = "Enseñanza onLine en la UNTELS"
    articulo.contenido = "Aula Virtual, Google Meet, Portal Académico, Google Classroom..."
    articulo.publicado = False
    articulo.save()
    return HttpResponse(f"Articulo Editado: {articulo.titulo} - {articulo.contenido}")

def listar_articulos(request):
    articulos = Articulo.objects.all()
    """articulos = Articulo.objects.filter(
        Q(titulo__contains="Py") |
        Q(titulo__contains="Hab")
        )"""

    return render(request, 'listar_articulos.html',{
        'articulos':articulos,
        'titulo': 'Listado de Artículos'
        })

def eliminar_articulo(request, id):
    articulo = Articulo.objects.get(pk=id)
    articulo.delete()
    return redirect('listar_articulos')

def save_articulo(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        if len(titulo)<=5:
            return HttpResponse("<h2>El tamaño del título es pequeño,intente nuevamente</h2>")
        contenido = request.POST['contenido']
        publicado = request.POST['publicado']

        articulo = Articulo(
            titulo = titulo,
            contenido = contenido,
            publicado = publicado
        )
        articulo.save()
        return HttpResponse(f"Articulo Creado: {articulo.titulo} - {articulo.contenido}")
    else:
        return HttpResponse("<h2>No se ha podido registrar el artículo</h2>")


def create_articulo(request):
    return render(request, 'create_articulo.html')
       
# Create your views here.
layout="""
    <h1> Proyecto Web (LP3) | kevin </h1>
<hr/>
<ul>
<li>
<a href="/inicio"> Inicio</a>
</li>
<li>
<a href="/saludo"> Mensaje de Saludo</a>
</li>
<li>
<a href="/rango"> Mostrar Números [a,b]</a>
</li>
<li>
<a href="/rango2/10/15"> Mostrar Números [10,15]</a>
</li>
</ul>
<hr/>
"""
def index(request):
    estudiantes = [ 'Isabella Caballero',
'Alejandro Hermitaño',
'Joan Palomino',
'Pierre Bernaola']
   

    return render(request,'index.html', {
        'titulo':'Inicio',
        'mensaje':'Proyecto web con Django',
        'estudiantes':estudiantes
})

def saludo(request):
    return render(request,'saludo.html',{
'titulo':'Saludo',
'autor_saludo':'Mg. Flor Elizabeth Cerdán León'
})

def rango(request):
    a = 10
    b = 20
    
    rango_numeros = range(a,b+1)
    return render(request,'rango.html',{
    'titulo':'Rango',
    'a':a,
    'b':b,
    'rango_numeros':rango_numeros
})

    
def rango2(request,a=0,b=100):
    if a>b:
        return redirect('rango2',a=b, b=a)
    resultado1 = f"""
        <h2> Números de [{a},{b}] </h2>
        Resultado: <br>
        <ul>
    """
    while a<=b:
        resultado1 += f"<li> {a} </li>"
        a+=1
    resultado1 += "</ul>"
    return HttpResponse(layout + resultado1)