# Generated by Django 4.2.7 on 2023-11-19 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_watchlaterlist_history_favoritelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='movie',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='movies.movie'),
        ),
    ]
