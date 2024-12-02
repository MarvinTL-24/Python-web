from django.shortcuts import render, get_object_or_404, redirect
from .models import Enquete, Alternativa, Resposta
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    # Buscando todas as enquetes
    enquetes = Enquete.objects.all()  
    return render(request, 'usuarios/home.html', {'enquetes': enquetes})

@login_required
def responder_enquete(request):
    if request.method == "POST":
        for enquete in Enquete.objects.all():
            alternativa_id = request.POST.get(f'alternativa_{enquete.id}')
            if alternativa_id:
                alternativa = get_object_or_404(Alternativa, id=alternativa_id)
                Resposta.objects.create(usuario=request.user, alternativa=alternativa)
        return redirect('usuarios:home')
    else:
        enquetes = Enquete.objects.all()
        return render(request, 'usuarios/home.html', {'enquetes': enquetes})
