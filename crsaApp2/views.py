from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vista3(request):
    return HttpResponse("<h1>hola mundo</h1>'<a>Pagina:---https://www.pcfactory.cl/?gclid=EAIaIQobChMI847xpoWz-gIVokFIAB0YagBnEAAYASAAEgIi0fD_BwE</a> <h1>Cristhofer Sandoval Fuentes </h1>")

def vista4(request):
    return HttpResponse("<h1>hola mundo</h1>'<a> pagina 1:---https://www.pcfactory.cl/?gclid=EAIaIQobChMI847xpoWz-gIVokFIAB0YagBnEAAYASAAEgIi0fD_BwE</a>   <a>  pagina 2 :----https://www.youtube.com/</a>")