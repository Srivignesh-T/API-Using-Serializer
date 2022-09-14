from django.db import models


# Create your models here.
class Employee(models.Model):
    e_id = models.IntegerField()
    e_name = models.CharField(max_length=200)
    e_dept = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    # def __str__(self):
    #     return f"{self.e_id}--{self.e_name}"
