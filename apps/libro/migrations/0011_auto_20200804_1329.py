# Generated by Django 3.1 on 2020-08-04 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0010_libro_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
