# Generated by Django 3.0.6 on 2023-01-02 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth_App', '0003_quesmodeltwo'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='quesmodel',
            table='Quiz_One_Questions',
        ),
        migrations.AlterModelTable(
            name='quesmodeltwo',
            table='Quiz_Two_Questions',
        ),
    ]
