from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=180)
    last_name = models.CharField(max_length=180)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='authors', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

class Bio(models.Model):
    author = models.OneToOneField('authors.Author', on_delete=models.CASCADE)
    bio = models.TextField()
