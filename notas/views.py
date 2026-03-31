from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Nota
from .forms import NotaForm, RegistroForm


def lista_notas(request):
    notas = Nota.objects.all()
    return render(request, 'notas/lista_notas.html', {'notas': notas})

def crear_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Nota creada exitosamente!')
            return redirect('lista_notas')
    else:
        form = NotaForm()
    
    return render(request, 'notas/crear_nota.html', {'form': form})

def editar_nota(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)
    
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Nota actualizada exitosamente!')
            return redirect('lista_notas')
    else:
        form = NotaForm(instance=nota)
    
    return render(request, 'notas/editar_nota.html', {'form': form, 'nota': nota})

@require_POST
def eliminar_nota(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)
    nota.delete()
    messages.success(request, '¡Nota eliminada exitosamente!')
    return redirect('lista_notas')


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Registro exitoso! Bienvenido.')
            return redirect('lista_notas')
    else:
        form = RegistroForm()
    
    return render(request, 'notas/registro.html', {'form': form})