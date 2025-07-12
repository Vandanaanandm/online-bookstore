from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    stock=models.IntegerField()
    description=models.TextField
    created_at=models.DateTimeField()
class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    boook=models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    ordered_at=models.DateTimeField()


# Create your models here.
