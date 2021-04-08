from django.db import models

class empdata(models.Model):

    name=models.CharField(max_length=10)
    department=models.CharField(max_length=10)
    rollno=models.IntegerField()
    


    def __str__(self):
        return self.name
