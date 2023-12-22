from django.db import models
from datetime import datetime


class Fotografia(models.Model):

    opcoes_categoria = [
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA","Galáxia"),
        ("PLANETA","Planeta"),
    ]

    nome = models.CharField(max_length=100, null = False, blank=False)
    legenda = models.CharField(max_length=150, null = False, blank=False)
    categoria = models.CharField(max_length=100, choices=opcoes_categoria, default="")
    descricao = models.TextField(null = False, blank=True)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'Fotografia [nome={self.nome}]'