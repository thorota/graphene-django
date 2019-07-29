# Generated by Django 2.2.3 on 2019-07-29 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190729_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]