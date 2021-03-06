# Generated by Django 2.2.7 on 2019-11-11 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djblockchain', '0003_auto_20191110_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockchain',
            name='provider_class',
            field=models.CharField(choices=[('eqs_sft.ethereum.Provider', 'Ethereum'), ('eqs_sft.tezos.Provider', 'Tezos')], max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='account',
            unique_together=set(),
        ),
    ]
