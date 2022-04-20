from django.shortcuts import render,redirect
from .forms import FormUpload, FormUploadConf
from django.conf import settings
import os
from .services import *
from . models import Arquivos
# Create your views here.

def home(request):
    return render(request,"base.html")


def upload_arquivo(request):
    form = FormUpload()

    if request.method == "POST":
        form = FormUpload(request.POST,request.FILES)
        if form.is_valid():
            pasta_temporaria = os.path.join(settings.BASE_DIR, "media/temp/")
            
            arquivo = form.cleaned_data['arquivo']
            autor = form.cleaned_data['autor']
            nome_arquivo = str(form.cleaned_data['arquivo'])
            with open(f'{pasta_temporaria}{nome_arquivo}', 'wb+') as destination:
                for chunk in arquivo.chunks():
                    destination.write(chunk)

            caminho_arquivo = os.path.join(pasta_temporaria, nome_arquivo)
            link = upload_drive(caminho_arquivo)
            Arquivos.objects.create(autor=autor, nome_arquivo=nome_arquivo, link_arquivo=link)
            #remove o arquivo temporário do disco
            os.remove(caminho_arquivo)
            return redirect('lista')

    return render(request,"form_upload.html",{'form':form})


def upload_config(request):
    form = FormUploadConf()
    pasta = settings.BASE_DIR
    if request.method == "POST":
        form = FormUploadConf(request.POST,request.FILES)
        if form.is_valid():
            arquivo = form.cleaned_data['arquivo_config']
            nome_arquivo = str(form.cleaned_data['arquivo_config'])
            with open(f'{pasta}/{nome_arquivo}', 'wb+') as destination:
                for chunk in arquivo.chunks():
                    destination.write(chunk)
        return redirect('home')
            
    return render(request,"form_upload_config.html",{'form':form})


def listar_todos(request):
    arquivos = Arquivos.objects.all()
    return render(request,"lista_arquivos.html",{'arquivos':arquivos})
