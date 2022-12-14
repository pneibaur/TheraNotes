# Generated by Django 4.1.2 on 2022-10-22 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_therapist_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='road_map',
            field=models.TextField(default='No current road map', max_length=250),
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(default='No bio added', max_length=250),
        ),
        migrations.AddField(
            model_name='user',
            name='interests',
            field=models.TextField(default='None added', max_length=250),
        ),
        migrations.AlterField(
            model_name='patient',
            name='desired_treatment',
            field=models.TextField(default="Patient didn't specify...", max_length=250),
        ),
    ]
