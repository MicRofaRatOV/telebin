# Generated by Django 5.0.6 on 2024-06-18 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bin', '0003_alter_note_ip_alter_note_link_alter_note_note_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='ip',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='note',
            name='link',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='note',
            name='password',
            field=models.CharField(max_length=64),
        ),
    ]
