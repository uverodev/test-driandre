# Generated by Django 3.1 on 2020-08-06 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0011_auto_20200804_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]