# Generated by Django 3.2.7 on 2021-09-09 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('backgroundImg', models.IntegerField()),
                ('avatar', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('gmail', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
