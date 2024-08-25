from django.db import models

class Cat(models.Model):
    breed= models.CharField(max_length=100, null=True, blank=True)
    coat= models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return  f"{self.breed} - {self.coat}"

class Fact(models.Model):
    cat = models.OneToOneField(Cat, on_delete=models.CASCADE)
    fact = models.TextField()

    def __str__(self):
        return f"{self.fact}"
