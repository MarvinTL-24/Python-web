# Importando os modelos
from usuarios.models import Enquete, Alternativa

# Criando a enquete
enquete = Enquete.objects.create(pergunta="Você é estudante do SENAC?")

# Criando as alternativas para a primeira pergunta
Alternativa.objects.create(enquete=enquete, texto="Sim")
Alternativa.objects.create(enquete=enquete, texto="Não")

# Criando a segunda pergunta
enquete2 = Enquete.objects.create(pergunta="Você terminará o curso em dezembro?")

# Criando as alternativas para a segunda pergunta
Alternativa.objects.create(enquete=enquete2, texto="Sim")
Alternativa.objects.create(enquete=enquete2, texto="Não")

# Criando a terceira pergunta
enquete3 = Enquete.objects.create(pergunta="O seu curso está relacionado à programação?")

# Criando as alternativas para a terceira pergunta
Alternativa.objects.create(enquete=enquete3, texto="Sim")
Alternativa.objects.create(enquete=enquete3, texto="Não")
