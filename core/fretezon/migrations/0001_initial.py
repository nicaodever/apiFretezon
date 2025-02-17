# Generated by Django 5.1.6 on 2025-02-16 21:08

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cnh',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('status_cnh', models.CharField(db_column='status_cnh', max_length=250)),
                ('data_emicao_cnh', models.DateField(db_column='data_emicao_cnh')),
                ('categoryta_cnh', models.CharField(db_column='categoryta_cnh', max_length=250)),
                ('validate_cnh', models.DateField(db_column='validate_cnh')),
            ],
        ),
        migrations.CreateModel(
            name='Frete',
            fields=[
                ('id', models.IntegerField(db_column='id_post', primary_key=True, serialize=False, unique=True)),
                ('tp_veiculo', models.CharField(db_column='tp_veiculo', max_length=255)),
                ('local_partida', models.CharField(db_column='local_partida', max_length=255)),
                ('destino', models.CharField(db_column='destino', max_length=255)),
                ('horario_retir', models.DateField(db_column='horario_retir')),
                ('sugerir_tarifa', models.FloatField(db_column='sugerir_tarifa')),
                ('foto_carga', models.DateField(db_column='foto_carga')),
                ('data_entrega', models.DateField(db_column='data_entrega')),
                ('descricao_carga', models.CharField(db_column='descricao_carga', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_column='name', max_length=250)),
                ('data_nascimento', models.DateField(db_column='data_nascimento')),
                ('cpf', models.IntegerField(db_column='cpf')),
                ('telefone', models.IntegerField(db_column='Telefone')),
                ('email', models.CharField(db_column='email', max_length=250)),
                ('cidade', models.CharField(db_column='cidade', max_length=250)),
                ('estado', models.CharField(db_column='estado', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('modelo', models.CharField(db_column='Modelo', max_length=50)),
                ('placa', models.CharField(db_column='placa', max_length=6)),
                ('marca', models.CharField(db_column='marca', max_length=30)),
                ('ano', models.IntegerField(db_column='ano')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.IntegerField(db_column='id_user', primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(db_column='password', max_length=64)),
                ('name', models.CharField(db_column='name', max_length=255)),
                ('email', models.EmailField(db_column='email', max_length=254, unique=True)),
                ('phone', models.CharField(db_column='phone', max_length=25)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
