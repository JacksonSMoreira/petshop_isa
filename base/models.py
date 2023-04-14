from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)


class Reserva(models.Model):
    nomepet = forms.CharField(max_length=50)
    telefone = forms.CharField(max_length=11)
    dia = forms.DateField()
    mensagem = forms.CharField(widget=forms.Textarea)