# Generated by Django 2.0.5 on 2018-05-26 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20180526_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admission_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='graduation_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='wechat_openid',
            field=models.TextField(null=True),
        ),
    ]