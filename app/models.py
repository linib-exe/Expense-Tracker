from django.db import models

# Create your models here
class Entry(models.Model):
    title = models.CharField(max_length = 20)
    amount = models.FloatField()
    tx_choices = (('in','IN'),
                  ('out','OUT'))
    tx_type = models.CharField(choices=tx_choices,max_length = 3)
    remarks = models.TextField()
    category_choices = (('Petrol','Petrol'),
                        ('Food','Food'),
                        ('Fees','Fees'),
                        ('Recreation','Recreation'))
    category = models.CharField(max_length = 20,choices=category_choices)
    proof = models.ImageField(null=True,blank=True,upload_to='images/')

    def __str__(self):
        return self.title
