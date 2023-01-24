from django.db import models
from django.urls import reverse
from datetime import date

WALKS = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night')
)

class Clothes(models.Model):
    category = models.CharField(max_length=50)
    color= models.CharField(max_length=30)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('clothes_detail', kwargs={'pk': self.id})

class Puppy(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField()
    clothing = models.ManyToManyField(Clothes)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'puppy_id': self.id}) 

    def walked_for_today(self):
        return self.walkings_set.filter(date=date.today()).count() >= len(WALKS)

class Walkings(models.Model):
    date = models.DateField('Date of walkings')
    walk = models.CharField(
        max_length=1,
        choices=WALKS,
        default=WALKS[0][0]
    )
    
    puppy = models.ForeignKey(Puppy, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.get_walk_display()} on {self.date}'
        
    class Meta:
        ordering= ['-date']


