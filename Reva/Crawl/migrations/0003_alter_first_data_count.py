# Generated by Django 4.1.7 on 2023-03-24 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crawl', '0002_alter_first_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='first',
            name='data_count',
            field=models.IntegerField(blank=True),
        ),
    ]