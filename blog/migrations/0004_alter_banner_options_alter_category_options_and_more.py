# Generated by Django 4.2.1 on 2023-05-14 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_banner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name_plural': 'Banner'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categorias'},
        ),
        migrations.AlterModelOptions(
            name='popular',
            options={'verbose_name_plural': 'Populares'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Postagens'},
        ),
    ]