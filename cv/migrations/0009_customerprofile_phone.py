# Generated by Django 3.2 on 2022-09-14 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0008_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
