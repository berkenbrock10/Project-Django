from django.db import models

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    nascimento = models.DateField()
    rg = models.IntegerField(max_length=7)
    cpf = models.IntegerField(max_length=11)
    cep = models.IntegerField(max_length=8)
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    uf = models.CharField(max_length=200)
    telefone = models.IntegerField(max_length=10)
    celular = models.IntegerField(max_length=11)
    email = models.CharField(max_length=200)


class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.IntegerField()
    desde = models.DateField()
    cep = models.IntegerField(max_length=8)
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    uf = models.CharField(max_length=200)
    telefone = models.IntegerField(max_length=10)
    celular = models.IntegerField(max_length=11)
    email = models.CharField(max_length=200)
