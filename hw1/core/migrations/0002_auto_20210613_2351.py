# Generated by Django 3.2.4 on 2021-06-13 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(default='example@email.com', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_no',
            field=models.CharField(default='0000000000', max_length=300),
            preserve_default=False,
        ),
    ]
