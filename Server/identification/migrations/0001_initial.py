# Generated by Django 2.0.5 on 2018-05-26 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Identification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification_code', models.TextField()),
                ('wx_open_id', models.TextField()),
                ('expire_at', models.BigIntegerField()),
            ],
        ),
    ]
