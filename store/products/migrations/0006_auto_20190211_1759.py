# Generated by Django 2.1.5 on 2019-02-11 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
