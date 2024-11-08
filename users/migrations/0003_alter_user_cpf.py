# Generated by Django 5.1.2 on 2024-11-05 20:34

import users.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=models.CharField(max_length=14, unique=True, validators=[users.validators.validate_cpf]),
        ),
    ]
