# Generated by Django 3.0.6 on 2023-01-02 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth_App', '0002_quesmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuesModelTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
            ],
        ),
    ]
