# Generated by Django 3.2.4 on 2021-07-09 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lwt', '0015_alter_grouper_of_same_words_id_string'),
    ]

    operations = [
        migrations.AddField(
            model_name='restore',
            name='import_readlang',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
