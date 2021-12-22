from django.shortcuts import render
from .models import projetofinal
from .forms import UserForm
from requests import get
from bs4 import BeautifulSoup



# Create your views here.
def homepage(request):


    return render(
    request=request,
    template_name="home.html",
    context={"cursos": projetofinal.objects.all}
    )

def formulario(request):
    submitbutton = request.POST.get("submit")

    Urls = str

    form = UserForm(request.POST or None)
    if form.is_valid():
        Urls = form.cleaned_data.get("Urls")

    navegar = get(Urls)
    tags = BeautifulSoup(navegar.text, "html5lib")
    tds = tags.find_all("a", attrs={"class": "mw-redirect"})
    [a.text for a in tds]
    refe = [Urls + h2["href"] for h2 in tds]
    refe

    context = {"form" : form, "Urls" : Urls,"refe" : refe,"submitbutton" : submitbutton}

    return render(
    request=request,
    template_name="observacao.html",
    context=context
    )

# https://pt.wikipedia.org/wiki/Filmes_do_Universo_Cinematogr%C3%A1fico_Marvel/wiki/Hist%C3%B3rias_em_quadrinhos
