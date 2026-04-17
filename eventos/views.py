from django.shortcuts import render, redirect
from .forms import Form

evento = []

def novo(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            evento.append(form.cleaned_data)
            return redirect('evento')
    else:
        form = Form()

    return render(request, 'eventos/novo.html', {'form': form})


def eventos(request):
    return render(request, 'eventos/lista.html', {'eventos': evento})