# Generated by Django 4.2.7 on 2023-12-24 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_problem_letter_answer_alter_problem_num_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='letter_answer',
            field=models.CharField(default='a', max_length=1, null=True),
        ),
    ]
