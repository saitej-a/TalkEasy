# Generated by Django 4.2.7 on 2023-11-26 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_chat_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='name',
        ),
        migrations.AlterField(
            model_name='messages',
            name='body',
            field=models.TextField(),
        ),
    ]
