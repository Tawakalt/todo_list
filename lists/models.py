from django.urls import reverse
from django.db import models

# Create your models here.
class List(models.Model):
    
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

    @staticmethod
    def create_new(first_item_text):
        list_ = List.objects.create()
        Item.objects.create(text=first_item_text, list=list_)


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')

    
    def __str__(self):
        return self.text