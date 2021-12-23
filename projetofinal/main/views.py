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
    context={"ppf": projetofinal.objects.all}
    )

def formulario(request):
    submitbutton = request.POST.get("submit")

    Urrls = str

    form = UserForm(request.POST or None)
    if form.is_valid():
        Urrls = form.cleaned_data.get("Urrls")
        if Urrls == Urrls:
            navegar = get(Urrls)
            tags = BeautifulSoup(navegar.text, "html5lib")
            tds = tags.find_all("a", attrs={"class": "mw-redirect"})
            [a.text for a in tds]
            refe = [Urrls + h2["href"] for h2 in tds]
            refe
            refe = sorted(refe, reverse = True)
            refe



    context = {"form" : form, "Urrls" : Urrls,"submitbutton" : submitbutton} # adicione o "refe": refe quando o arquivo estiver rodando

    return render(
    request=request,
    template_name="observacao.html",
    context=context
    )

# https://pt.wikipedia.org/wiki/Filmes_do_Universo_Cinematogr%C3%A1fico_Marvel/wiki/Hist%C3%B3rias_em_quadrinhos
