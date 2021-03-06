# Generated by Django 2.0.5 on 2018-05-09 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.BigIntegerField()),
                ('password', models.TextField()),
                ('phone', models.TextField()),
                ('name', models.TextField()),
                ('birth', models.DateField()),
                ('gender', models.IntegerField()),
                ('major', models.TextField()),
                ('legal_id', models.TextField()),
                ('admission_date', models.DateField()),
                ('graduation_date', models.DateField()),
                ('last_disconnect', models.DateTimeField()),
                ('info', models.TextField(default='{}')),
            ],
        ),
    ]
