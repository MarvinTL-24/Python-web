from decimal import Decimal
from django.shortcuts import render
from .models import Produto

def home(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        quantidade = int(request.POST.get("quantidade"))
        valor = float(request.POST.get("valor"))

        if nome and quantidade > 0 and valor > 0:
            Produto.objects.create(nome=nome, quantidade=quantidade, valor=valor)

    produtos = Produto.objects.all()

    produtos_com_totais = [
        {
            'id': p.id,
            'nome': p.nome,
            'quantidade': p.quantidade,
            'valor': p.valor,
            'total': p.quantidade * p.valor
        }
        for p in produtos
    ]
    
    total = sum(p['total'] for p in produtos_com_totais)
    total_itens = sum(p['quantidade'] for p in produtos_com_totais)

    if total_itens >= 50:
        desconto = 0.15
    elif total_itens >= 20:
        desconto = 0.10
    elif total_itens >= 10:
        desconto = 0.05
    else:
        desconto = 0

    # Converte o desconto para Decimal para garantir precisão.
    total_com_desconto = total * Decimal(1 - desconto)

    context = {
        'produtos': produtos_com_totais,
        'total': total,
        'desconto': desconto * 100,  # Converte o desconto para porcentagem.
        'total_com_desconto': total_com_desconto
    }

    return render(request, 'home/home.html', context)
