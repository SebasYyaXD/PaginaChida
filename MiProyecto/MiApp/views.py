from django.shortcuts import render

def Principal(request):
    return render(request,'MiApp/index.html')
def Formulario(request):
    return render(request,'MiApp/Contacto.html')
def Acerca(request):
    return render(request,'MiApp/about.html')
