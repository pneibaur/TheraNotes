# Generated by Django 4.1.2 on 2022-10-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='therapist',
            name='patient',
            field=models.ManyToManyField(to='main_app.patient'),
        ),
    ]
