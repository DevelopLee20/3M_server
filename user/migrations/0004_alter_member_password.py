# Generated by Django 4.2.3 on 2023-07-26 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_password_member_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='Password',
            field=models.CharField(max_length=100),
        ),
    ]
