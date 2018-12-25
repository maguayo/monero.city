# Generated by Django 2.1.4 on 2018-12-25 11:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_listing_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.CharField(max_length=254)),
                ('name', models.CharField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='listing',
            name='categories',
            field=models.ManyToManyField(to='main.Category'),
        ),
    ]
