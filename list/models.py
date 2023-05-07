from django.db import models

# Create your models here.
class Person(models.Model):
    # 이미지는 일단 생략
    # image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100) # 이름
    gender = models.CharField(max_length=10) # 성별 
    nationality = models.CharField(max_length=100) # 국적
    representataive_work = models.CharField(max_length=200) # 대표작

    def __str__(self):
        return self.name