# Generated by Django 3.1 on 2020-08-30 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tubify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_id', models.CharField(max_length=64)),
                ('v_title', models.CharField(max_length=128)),
                ('v_views', models.IntegerField()),
                ('v_thumb', models.CharField(max_length=64)),
                ('v_url_suffix', models.CharField(max_length=128)),
            ],
        ),
    ]
