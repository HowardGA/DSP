# Generated by Django 5.0.4 on 2024-05-29 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_goal_state_alter_grantgoal_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='state',
            field=models.CharField(choices=[('PENDING', 'PD'), ('DONE', 'DN'), ('IN PROGRESS', 'IP')], max_length=16),
        ),
        migrations.AlterField(
            model_name='grantgoal',
            name='state',
            field=models.CharField(choices=[('PENDING', 'PD'), ('DONE', 'DN'), ('IN PROGRESS', 'IP')], max_length=16),
        ),
        migrations.AlterField(
            model_name='issue',
            name='state',
            field=models.CharField(choices=[('PENDING', 'PD'), ('DONE', 'DN'), ('IN PROGRESS', 'IP')], max_length=16),
        ),
        migrations.AlterField(
            model_name='subgrantgoal',
            name='state',
            field=models.CharField(choices=[('PENDING', 'PD'), ('DONE', 'DN'), ('IN PROGRESS', 'IP')], max_length=16),
        ),
    ]