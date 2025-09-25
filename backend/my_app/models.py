from django.db import models



# Contato direto
# Telefone, WhatsApp, e-mail ou botão “Fale comigo”.
# Localização (quando aplicável)
# Endereço físico, mapa integrado ou atendimento online.

class Person(models.Model):
    # Criando os campos da tabela
    name = models.CharField(max_length=120)
    email_id = models.CharField(max_length=320, null=True)
    atuacao_especialidade = models.CharField(max_length=150, null=True)
    breve_descricao_apresentacao = models.CharField(max_length=500, null=True)
    # birthday = models.DateTimeField()
    profissao = models.CharField(max_length=120, null=True)
    servicos_oferecidos = models.TextField(max_length=500, null=True)
    watzapp = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=320, null=True)
    instagram =  models.CharField(max_length=100, null=True)
    facebook = models.CharField(max_length=100, null=True)
    localizacao = models.CharField(max_length=200, null=True)
    
    

    def __str__(self):
        return self.email_id
