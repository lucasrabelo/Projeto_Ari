# Generated by Django 2.0.3 on 2018-04-03 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=60)),
                ('complemento', models.CharField(max_length=45)),
                ('numero', models.CharField(max_length=5)),
                ('cidade', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=8)),
                ('uf', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=20)),
                ('rg_estado', models.CharField(max_length=2)),
                ('telefone_fixo', models.CharField(max_length=10)),
                ('telefone_celular', models.CharField(max_length=11)),
                ('tipo_paciente', models.IntegerField(choices=[('MEDICO', 'Médico'), ('FUNCIONARIO', 'Funcionário'), ('PACIENTE', 'Paciente')], default=1)),
                ('estadoCivil', models.IntegerField(choices=[('CASADO', 'Casado (a)'), ('SOLTEIRO', 'Solteiro (a)'), ('VIUVO', 'Viúvo (a)'), ('UNIAO_ESTAVEL', 'União Estável')], default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='appbase.Pessoa')),
                ('especialidadeMd', models.CharField(max_length=30)),
                ('nrConselho', models.CharField(max_length=40)),
            ],
            bases=('appbase.pessoa',),
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='appbase.Pessoa')),
                ('alturaPaciente', models.DecimalField(decimal_places=2, max_digits=4)),
                ('pesoPaciente', models.DecimalField(decimal_places=2, max_digits=4)),
                ('atividadeFisica', models.CharField(max_length=8)),
                ('imcPaciente', models.DecimalField(decimal_places=2, max_digits=4)),
                ('idadePaciente', models.IntegerField()),
                ('dataAvaliacao', models.DateField()),
                ('etnia', models.CharField(max_length=20)),
            ],
            bases=('appbase.pessoa',),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='endereco_pessoa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appbase.Endereco'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='responsavelPaciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Paciente.responsavelPaciente+', to='appbase.Pessoa'),
        ),
    ]
