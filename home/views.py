from django.shortcuts import render,redirect
from .models import Usuario
from django.contrib import messages,auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from time import sleep

def index(request):
    return render(request,'home/index.html')

def loguin(request):
    if request.method !='POST':
        return render(request,'home/loguin.html')
    

    email = request.POST.get('email')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=email , password=senha)
    

    if not user:
        messages.error(request,'Email ou senha incorreta')
        return render(request,'home/loguin.html')
    else:
        auth.login(request,user)
        messages.error(request,'Voçe fez loguin com sucesso!!')
        return redirect('videos')

def logout(request):
    auth.logout(request)
    return redirect('homepage')

def cadastro(request):
    if request.method !='POST':
        return render(request,'home/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    email_02 = request.POST.get('email_02')
    telefone = request.POST.get('telefone')
    senha = request.POST.get('senha')
    senha_02 =  request.POST.get('senha_02')
    criaçao = Usuario.criaçao

    if not nome or not sobrenome or not email or not email_02 or not telefone or not senha or not senha_02 :
        messages.error(request,'Favor preenchar todos os campos')
        return render(request,'home/cadastro.html')
    try:
        validate_email(email)
    except:
        messages.error(request,'E-email invalido')
        return render(request,'home/cadastro.html')
    
    if email != email_02:
        messages.error(request,'E-mail-incorreto')
        return render(request,'home/cadastro.html')

    if senha != senha_02:
        messages.error(request,'Senha incorreta')
        return render(request,'home/cadastro.html')
    
    if User.objects.filter(email=email).exists():
        messages.error(request,'E-mail , ja cadastrado')
        return render(request,'home/cadastro.html')
    
    if len(senha) < 6 :
        messages.error(request,'Senha muito curta, minimo 6 digito')
        return render(request,'home/cadastro.html')

    

    user = User.objects.create_user(username=email, email=email, password=senha,
                                        first_name=nome, last_name=sobrenome)

    user.save()
    
    messages.error(request,f'Cadastro realizado com sucesso, \n {request.POST.get("nome")} \n Bem vindo')
    sleep(1)
    return redirect('homepage')


    
@login_required(redirect_field_name='loguin')
def videos(request):
    nome = {request.POST.get("nome")}
    return render(request,'home/videos.html')