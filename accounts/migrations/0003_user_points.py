# Generated by Django 3.0.5 on 2020-04-10 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190326_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='points',
            field=models.IntegerField(blank=True, default=200),
            preserve_default=False,
        ),
    ]