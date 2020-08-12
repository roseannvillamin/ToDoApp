# Generated by Django 3.1 on 2020-08-11 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='content',
            field=models.CharField(max_length=200),
        ),
    ]
