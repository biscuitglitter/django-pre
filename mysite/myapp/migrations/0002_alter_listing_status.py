# Generated by Django 4.1.2 on 2022-10-10 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='status',
            field=models.CharField(choices=[('rent', 'rent'), ('sell', 'sell')], max_length=20, null=True),
        ),
    ]
