# Generated by Django 3.2 on 2022-09-14 23:12

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0010_alter_customerprofile_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cv.user')),
                ('phone', models.CharField(blank=True, default='Phone', max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cv.user',),
            managers=[
                ('Company', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='password',
            field=models.CharField(blank=True, default='Password', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='phone',
            field=models.CharField(blank=True, default='Phone', max_length=50, null=True),
        ),
    ]
