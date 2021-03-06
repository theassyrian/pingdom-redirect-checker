# Generated by Django 2.0.5 on 2018-09-10 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Responsetime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_time', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Urllist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_url', models.URLField()),
                ('team', models.CharField(max_length=60)),
                ('target_url', models.URLField(default='')),
                ('enable', models.BooleanField(default=True)),
                ('broken_redirect', models.BooleanField(default=False)),
                ('actual_target', models.URLField(default='')),
                ('slack_sent', models.BooleanField(default=False)),
            ],
        ),
    ]
