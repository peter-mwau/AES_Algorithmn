# Generated by Django 4.2.3 on 2023-07-05 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aes_algorithm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='salt',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
