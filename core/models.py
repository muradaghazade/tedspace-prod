from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=550)
    description = models.TextField()
    text = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Partner(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    email = models.EmailField()
    position = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name + ' ' + self.surname