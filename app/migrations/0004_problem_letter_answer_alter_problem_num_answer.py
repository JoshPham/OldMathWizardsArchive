# Generated by Django 4.2.7 on 2023-12-24 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_problem_letter_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='letter_answer',
            field=models.CharField(default='a', max_length=1),
        ),
        migrations.AlterField(
            model_name='problem',
            name='num_answer',
            field=models.IntegerField(null=True),
        ),
    ]