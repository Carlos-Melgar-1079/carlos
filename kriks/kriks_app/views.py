from django.shortcuts import render
from .views import proovedores
# Create your views here.


def inicio_vista(request):
    lasmaterias=proovedores.objects.all()
    return render(request,"gestionarproovedores.html",{"mismaterias":lasmaterias})


def registrarproovedores(request):
    id=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["txt"]
    edad=request.POST["txtedad"]
    INE=request.POST["txtINE"]
    permiso=request.POST["txtpermiso"]
    matricula=request.POST["txtmatricula"]
    guardarproovedor=proovedores.objects.create(id=id,nombre=nombre,telefono=telefono,edad=edad,INE=INE,permiso=permiso,matricula=matricula)
    return redirect("/")

def seleccionarproovedores(request,codigo):
    proovedor=proovedores.objects.get(codigo=codigo)
    return render(request,"editarproovedor.html",{"mismaterias":proovedor})

def editarproovedor(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["numtelefono"]
    edad=request.POST["numedad"]
    INE=request.POST["numINE"]
    permiso=request.POST["txtpermiso"]
    matricula=request.POST["nummatricula"]
    proovedor=proovedores.objects.get(id=id)
    proovedor.nombre=nombre
    proovedor.telefono=telefono
    proovedor.edad=edad
    proovedor.INE=INE
    proovedor.permiso=permiso
    proovedor.matricula=matricula
    proovedor.save()
    return redirect("/")

def borrarproovedor(request,codigo):
    proovedor=proovedores.objects.get(codigo=codigo)
    proovedor.delete()

    return redirect("/")