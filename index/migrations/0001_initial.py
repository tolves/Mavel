# Generated by Django 2.2 on 2019-06-13 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=400)),
                ('update_date', models.DateTimeField(verbose_name='date updated')),
                ('image', models.ImageField(blank=True, null=True, upload_to='avatars/')),
            ],
        ),
    ]
