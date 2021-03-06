# Generated by Django 3.2.7 on 2021-10-24 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0010_auto_20211023_2132'),
        ('asks', '0007_auto_20211021_2149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Pergunta', 'verbose_name_plural': 'Perguntas'},
        ),
        migrations.AlterField(
            model_name='question',
            name='answered',
            field=models.BooleanField(default=False, verbose_name='Respondida'),
        ),
        migrations.AlterField(
            model_name='question',
            name='creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de criação'),
        ),
        migrations.AlterField(
            model_name='question',
            name='creator',
            field=models.CharField(max_length=128, verbose_name='Criador'),
        ),
        migrations.AlterField(
            model_name='question',
            name='down_votes',
            field=models.PositiveIntegerField(default=0, verbose_name='Votos Negativos'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(max_length=512, verbose_name='Texto'),
        ),
        migrations.AlterField(
            model_name='question',
            name='theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='room.theme', verbose_name='Tema'),
        ),
        migrations.AlterField(
            model_name='question',
            name='up_votes',
            field=models.PositiveIntegerField(default=0, verbose_name='Votos Positivos'),
        ),
    ]
