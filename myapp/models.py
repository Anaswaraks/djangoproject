from django.db import models

# Create your models here.
class details(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    phone=models.IntegerField(null=True)
    grade=models.CharField(max_length=1,null=True)

class student(models.Model):
    student_name=models.CharField(max_length=60)
    place=models.CharField(max_length=60)
    mark=models.IntegerField()    

class myuser(models.Model):
    name=models.CharField(max_length=60)
    age=models.IntegerField()

    def __str__(self):
        return self.name    