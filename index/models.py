from django.db import models
# Create your models here.

#type commands below first
#pip install Pillow --user
#python manage.py makemigrations index
#python manage.py migrate

class Avatar(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    update_date = models.DateTimeField('date updated')
    image = models.ImageField(upload_to='avatars/',blank=True,null=True)
    image_hover = models.ImageField(upload_to='avatars/',blank=True,null=True)

class Project(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200,null=True)
    link = models.CharField(max_length=200,null=True)
    desc = models.TextField()
    update_date = models.DateTimeField('date updated')
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    bgimage = models.ImageField(upload_to='projects/', blank=True, null=True)

class Linkexchange(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='links/', blank=True, null=True)

class Hr(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()

class Seo(models.Model):
    keywords = models.TextField()
    desc = models.TextField(null=True)
    title = models.CharField(max_length=200,null=True)