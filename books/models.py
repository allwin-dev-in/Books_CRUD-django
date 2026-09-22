from django.db import models


# Books[id,title,auther,price,pages,publication]
class Books(models.Model):
    title=models.CharField(max_length=200)
    auther=models.CharField(max_length=200)
    price=models.PositiveIntegerField(default=0)
    pages=models.PositiveIntegerField(default=0)
    publication=models.CharField(max_length=200)

    