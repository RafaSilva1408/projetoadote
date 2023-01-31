from django.db import models
from django.contrib.auth.models import User

# Os models modelam o banco de dados ou a página admin


class Raca(models.Model):
    raca = models.CharField(max_length=50)

    def __str__(self):
        return self.raca


class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag


class Pet(models.Model):  # Quando tem relação de um pra muitos é Foreignkey
    choices_status = (('P', 'Para adoção'),
                      ('A', 'Adotado'))
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    foto = models.ImageField(upload_to="fotos_pets")
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=14)
    tags = models.ManyToManyField(Tag)  # Quando tem relação de muitos pra muitos
    raca = models.ForeignKey(Raca, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=choices_status, default='P')

    def __str__(self):
        return self.nome
