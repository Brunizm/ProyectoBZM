from django.shortcuts import render

def inicio(request):
    return render(request,'AppBZM/inicio.html')

def cursos(request):
    return render(request,'AppBZM/cursos.html')

def profesores(request):
    return render(request,'AppBZM/profesores.html')

def estudiantes(request):
    return render(request,'AppBZM/estudiantes.html')

def entregables(request):
    return render(request,'AppBZM/entregables.html')