from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=180)
    last_name = models.CharField(max_length=180)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Autor: {self.first_name} {self.last_name}"
    def __repr__(self):
        return f"Autor: {self.first_name} {self.last_name}"
