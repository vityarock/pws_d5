# Generated by Django 3.1.7 on 2021-04-09 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0006_auto_20210409_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='reader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='get_book', to='p_library.reader'),
        ),
    ]
