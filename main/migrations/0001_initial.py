# Generated by Django 2.1.4 on 2018-12-20 23:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('map_lat', models.CharField(max_length=20)),
                ('map_long', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=255)),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('rating', models.IntegerField(default=0)),
                ('review', models.CharField(max_length=255)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reviewed_listing', to='main.Listing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_rating', to='main.Listing')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('tip', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tip_listing', to='main.Listing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_tip', to='main.Listing')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
