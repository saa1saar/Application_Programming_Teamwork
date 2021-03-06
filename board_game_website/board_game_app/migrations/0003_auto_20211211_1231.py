# Generated by Django 3.2.9 on 2021-12-11 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board_game_app', '0002_availablegames'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
        migrations.RenameModel(
            old_name='BoardGame',
            new_name='BG',
        ),
        migrations.DeleteModel(
            name='AvailableGames',
        ),
        migrations.AddField(
            model_name='entry',
            name='bg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board_game_app.bg'),
        ),
    ]
