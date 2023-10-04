from django.db import models

# Create your models here.
class Education(models.Model):
    title= models.CharField(max_length=100)
    start_year= models.CharField(max_length=100)
    end_year= models.CharField(max_length=100)
    institute= models.CharField(max_length=100)
    university= models.CharField(max_length=100)
    grade= models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Skills(models.Model):
    skill= models.CharField(max_length=100)

    def __str__(self):
        return self.skill
    
class Project(models.Model):
    project= models.CharField(max_length=100)
    link = models.CharField(max_length=2048, default='')

    def __str__(self):
        return self.project


class Certificate(models.Model):
    title= models.CharField(max_length=100)
    certificate= models.ImageField(upload_to='certificateimg/', blank=True, null=True)

    def __str__(self):
        return self.title
    

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    title= models.CharField(max_length=100)
    remark = models.TextField()

    def __str__(self):
        return self.email