# Generated by Django 5.1.2 on 2024-12-22 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_alter_activity_activity_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_type',
            field=models.CharField(choices=[('Running', 'Running'), ('Cycling', 'Cycling'), ('Weightlifting', 'Weightlifting')], default='Running', max_length=100),
        ),
    ]
