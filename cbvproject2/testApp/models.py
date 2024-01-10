from django.db import models
from django.urls import reverse
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    pages = models.IntegerField()
    price = models.FloatField()

    def get_absolute_url(self):
        #return reverse('bookslist') #this method is used to come back to bookslist aftr insetring neww book
        return reverse('bookdetail', kwargs={'pk':self.pk})
