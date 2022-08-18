from django.db import models

class Drink(models.Model):
    task = models.CharField(max_length=100)
    dueDate = models.CharField(max_length=10)
    urgency = models.DecimalField(decimal_places=2,max_digits=4)
    def __str__(self) -> str:
        return self.task + "  " + self.dueDate