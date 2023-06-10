from django.db import models
from django.utils import timezone as tz
from django.urls import reverse

# Create your models here.

def one_week_hence():
    return tz.now() + tz.timedelta(days=7) # This function will allow to get the date 7 days after

class ToDoList(models.Model): # Creating the table
    title = models.CharField(max_length=100, unique=True) # This is making the value unique aka pk

    def get_absolute_url(self):
        return reverse(list, args=[self.id])
    
    def __str__(self):
        return self.title
    
class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('item-update', args=[self.todo_list.id, str(self.id)])
    
    def __str__(self):
        return f"{self.title}: {self.due_date}"


