# Generated by Django 3.2.9 on 2021-11-25 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_contact_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='messages',
            field=models.TextField(blank=True, default='message', null=True),
        ),
    ]