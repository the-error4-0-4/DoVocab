# Generated by Django 4.1.5 on 2023-02-04 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vocab', '0007_userdetail_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task_result',
            name='points',
        ),
        migrations.RemoveField(
            model_name='task_result',
            name='test_status',
        ),
        migrations.RemoveField(
            model_name='task_result',
            name='test_unlock',
        ),
    ]
