# -*- coding: utf-8 -*-
import pycep_correios
from django.db import models
from math import pow
from datetime import date

# Create your models here.


class Endereco(models.Model):
    u"""
    Classe Endereço.

    Classe registra endereço de todos os registros do sistema

    """

    endereco = models.CharField(max_length=60)
    complemento = models.CharField(max_length=45)
    numero = models.CharField(max_length=5)
    cidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    uf = models.CharField(max_length=2)


class Pessoa(models.Model):
    """

    Classe pessoa.

    Classe para registro de pessoas.

    """

    MEDICO = 0
    FUNCIONARIO = 1
    PACIENTE = 2
    SOLTEIRO = 10
    CASADO = 11
    VIUVO = 12
    UNIAO_ESTAVEL = 13

    TIPO_PESSOA = (
        ('MEDICO', 'Médico'),
        ('FUNCIONARIO', 'Funcionário'),
        ('PACIENTE', 'Paciente'),
    )

    ESTADO_CIVIL = (
        ('CASADO', 'Casado (a)'),
        ('SOLTEIRO', 'Solteiro (a)'),
        ('VIUVO', 'Viúvo (a)'),
        ('UNIAO_ESTAVEL', 'União Estável')
    )

    nome = models.CharField(max_length=70)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=20)
    rg_estado = models.CharField(max_length=2)
    data_nascimento = models.DateField
    telefone_fixo = models.CharField(max_length=10)
    telefone_celular = models.CharField(max_length=11)
    is_whatzapp = models.BooleanField
    tipo_paciente = models.IntegerField(choices=TIPO_PESSOA,
                                        default=FUNCIONARIO)
    estadoCivil = models.IntegerField(choices=ESTADO_CIVIL,
                                      default=SOLTEIRO)
    endereco_pessoa = models.ForeignKey('Endereco', on_delete=models.SET_NULL,
                                        null=True)

    @property
    def idade(self):
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) <                                                        (self.data_nascimento.month, self.data_nascimento.day))

    def __str__(self):
        return self.nome


class Medico(Pessoa):
    """
    Classe Medico.

    Informacoes do Medico.
    """

    especialidadeMd = models.CharField(max_length=30)
    nrConselho = models.CharField(max_length=40)


class Paciente(Pessoa):
    """
    Classe Paciente.

    Informacoes do paciente.
    """

    ATIVIDADE_FISICA = (
        ('0', 'Sedentária'),
        ('1', 'Moderada'),
        ('2', 'Intensa')
    )

    alturaPaciente = models.DecimalField(max_digits=4, decimal_places=2)
    pesoPaciente = models.DecimalField(max_digits=4, decimal_places=2)
    imcPaciente = models.DecimalField(max_digits=4, decimal_places=2)
    atividadeFisica = models.CharField(max_length=8)
    imcPaciente = models.DecimalField(max_digits=4, decimal_places=2)
    idadePaciente = models.IntegerField()
    dataAvaliacao = models.DateField()
    etnia = models.CharField(max_length=20)
    responsavelPaciente = models.ForeignKey('Pessoa',
                                            on_delete=models.SET_NULL,
                                            null=True,
                                            related_name='Paciente.responsavelPaciente+')

    def calculaIMC(self):
        return self.pesoPaciente / pow(self.alturaPaciente, 2)
