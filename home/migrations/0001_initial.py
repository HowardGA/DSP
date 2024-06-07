# Generated by Django 5.0.4 on 2024-05-29 02:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0003_alter_goal_state_alter_grantgoal_state_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(default='I love Plesem System', max_length=128)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=8)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.area')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
