# Generated by Django 4.1.5 on 2023-02-04 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocab', '0008_remove_task_result_points_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_opt',
            field=models.IntegerField(),
        ),
    ]
