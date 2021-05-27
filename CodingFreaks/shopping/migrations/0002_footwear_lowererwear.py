# Generated by Django 3.2.3 on 2021-05-19 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='footwear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_id', models.TextField()),
                ('footer_id', models.TextField()),
                ('footer_name', models.TextField()),
                ('footer_type', models.TextField()),
                ('price', models.TextField()),
                ('available', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='lowererwear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_id', models.TextField()),
                ('lower_id', models.TextField()),
                ('lower_name', models.TextField()),
                ('lower_type', models.TextField()),
                ('price', models.TextField()),
                ('available', models.TextField()),
            ],
        ),
    ]
