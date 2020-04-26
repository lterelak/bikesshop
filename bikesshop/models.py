from django.db import models

class Colour(models.Model):
    colour = models.CharField(max_length=50)

    def __str__(self):
        return self.colour

class Frame(models.Model):
    frame = models.CharField(max_length=50)
    def __str__(self):
        return self.frame

class Bike(models.Model):
    model = models.CharField(max_length=50)
    description = models.TextField()
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE)
    tyres = models.CharField(max_length=50)
    total_weight = models.CharField(max_length=50)
    chain = models.CharField(max_length=50)
    fork = models.CharField(max_length=50)
    pedals = models.CharField(max_length=50)
    seat = models.CharField(max_length=50)

    def __str__(self):
        return self.model