# Generated by Django 2.1.5 on 2019-02-13 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='experience',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
