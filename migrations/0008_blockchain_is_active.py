# Generated by Django 2.2.8 on 2019-12-03 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djblockchain', '0007_blockchain_confirmation_blocks'),
    ]

    operations = [
        migrations.AddField(
            model_name='blockchain',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='blockchain',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
