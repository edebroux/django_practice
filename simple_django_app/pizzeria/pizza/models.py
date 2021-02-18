from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=200)  # Should hold name of pizza, such as Hawaiian or Deep Dish
    date_added = models.DateTimeField(auto_now_add=True)  # Probably relevent if running FIFO/LIFO system at the pizzeria

    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200) # don't need long blocks of text to describe toppings either

    def __str__(self):
        return self.name
        