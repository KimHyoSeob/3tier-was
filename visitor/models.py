from django.db import models

# Create your models here.

class Visitor(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField()
    email = models.CharField(max_length=100)
    day = models.CharField(max_length=30)

    def __str__(self):
        return f"작성자 : {self.name}\n내용 : {self.content}\nemail : {self.eamil}\n작성일 : {self.day}"