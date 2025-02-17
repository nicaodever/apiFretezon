from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

# Create your models here.
class User(AbstractUser, PermissionsMixin):
    id = models.IntegerField(
        primary_key=True,
        unique=True,
        db_column='id_user'
    )
    password = models.CharField(
        db_column='password',
        null=False,
        max_length=64
    )
    name = models.CharField(
        db_column='name',
        null=False,
        max_length=255
    )
    email = models.EmailField(
        db_column='email',
        unique=True,
        null=False
    )
    phone = models.CharField(
        db_column='phone',
        null=False,
        max_length=25
    )
class Frete(models.Model):
    objects = models.Manager()
    id = models.IntegerField(
        primary_key=True,
        unique=True,
        db_column='id_post'
    )
    tp_veiculo = models.CharField(
        db_column='tp_veiculo',
        null=False,
        max_length=255
    )
    local_partida = models.CharField(
        db_column='local_partida',
        null=False,
        max_length=255
    )
    destino = models.CharField(
        db_column='destino',
        null=False,
        max_length=255
    )
    horario_retir = models.DateField(
        db_column='horario_retir',
        null=False
    )
    sugerir_tarifa = models.FloatField(
        db_column='sugerir_tarifa',
        null=False
    )
    foto_carga = models.DateField(
        db_column='foto_carga',
        null=False
    )
    data_entrega = models.DateField(
        db_column='data_entrega',
        null=False
    )
    descricao_carga = models.CharField(
        db_column='descricao_carga',
        max_length=150,
        null=False
    )

    class Meta:
        managed = True
        db_table = 'frete'
        verbose_name = 'Frete'
        verbose_name_plural = 'fretes'

class Motorista(models.Model):
    objects = models.Manager()
    id = models.IntegerField(
        primary_key=True,
        unique=True,
        db_column='id'
    )
    name = models.CharField(
        db_column='name',
        max_length=250,
        null=False
    )
    data_nascimento = models.DateField(
        db_column='data_nascimento',
        null=False
    )
    cpf = models.IntegerField(
        db_column='cpf',
        null=False
    )
    telefone = models.IntegerField(
        db_column='Telefone',
        null=False
    )
    email = models.CharField(
        db_column='email',
        max_length=250,
        null=False
    )
    cidade = models.CharField(
        db_column='cidade',
        max_length=250,
        null=False
    )
    estado = models.CharField(
        db_column='estado',
        max_length=250,
        null=False
    )

class Veiculo(models.Model):
    id = models.IntegerField(
        primary_key=True,
        unique=True,
        db_column='id'
    )
    modelo = models.CharField(
        db_column='Modelo',
        max_length=50,
        null=False
    )
    placa = models.CharField(
        db_column='placa',
        max_length=6,
        null=False
    )
    marca = models.CharField(
        db_column='marca',
        max_length=30,
        null=False
    )
    ano = models.IntegerField(
        db_column='ano',
        null=False
    )

class Cnh(models.Model):
    id = models.IntegerField(
        primary_key=True,
        unique=True,
        db_column='id'
    )
    status_cnh = models.CharField(
        db_column='status_cnh',
        max_length=250,
        null=False
    )
    data_emicao_cnh = models.DateField(
        db_column='data_emicao_cnh',
        null=False
    )
    categoryta_cnh = models.CharField(
        db_column='categoryta_cnh',
        max_length=250,
        null=False
    )
    validate_cnh = models.DateField(
        db_column='validate_cnh',
        null=False
    )