# Generated by Django 5.0.7 on 2024-07-29 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cid', models.IntegerField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('pno', models.CharField(max_length=50)),
                ('un', models.CharField(max_length=50)),
                ('pw', models.CharField(max_length=50)),
            ],
        ),
    ]
