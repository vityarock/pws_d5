# Generated by Django 3.1.7 on 2021-04-11 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0007_book_reader'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reader',
            name='book',
        ),
        migrations.AddField(
            model_name='reader',
            name='book',
            field=models.TextField(default='anybody'),
            preserve_default=False,
        ),
    ]
