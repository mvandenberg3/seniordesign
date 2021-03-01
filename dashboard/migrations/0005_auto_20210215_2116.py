# Generated by Django 3.1.6 on 2021-02-16 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210211_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('permalink', models.CharField(max_length=12, unique=True)),
                ('update_date', models.DateTimeField(verbose_name='Last Updated')),
                ('bodytext', models.TextField(blank=True, verbose_name='Page Content')),
            ],
        ),
        migrations.DeleteModel(
            name='Graph',
        ),
    ]
