# Generated by Django 2.2 on 2019-06-14 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20190613_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linkexchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='links/')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='bgimage',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
