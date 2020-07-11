# Generated by Django 3.0.6 on 2020-07-06 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=254)),
                ('post', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
    ]