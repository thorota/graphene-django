# Generated by Django 2.2.3 on 2019-07-29 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=3000)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
