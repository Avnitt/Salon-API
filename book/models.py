from django.db import models
from django.contrib.auth import get_user_model
import time
from datetime import datetime

class Service(models.Model):
    image_url = models.ImageField(upload_to='service')
    title = models.CharField(max_length=200,
                             null=False, 
                             blank=False)
    desc = models.TextField()

    def __str__(self):
        return self.title

class Subservice(models.Model):
    service = models.ForeignKey(Service,
                                on_delete=models.CASCADE,
                                related_name='subservices')
    image_url = models.ImageField(upload_to='subservice')
    title = models.CharField(max_length=200,
                             null=False,
                             blank=False)
    price = models.IntegerField()

    def __str__(self):
        return self.title

class Professional(models.Model):
    image_url = models.ImageField(upload_to='professional')
    name = models.CharField(max_length=200)
    desc = models.TextField()
    subservice = models.ManyToManyField(Subservice,
                                   related_name="professionals")

    def __str__(self):
        return self.name

class Slot(models.Model):
    professional = models.ForeignKey(Professional,
                              on_delete=models.CASCADE,
                              related_name="slots")
    time = models.DateTimeField()

    def __str__(self):
        return self.time

class Order(models.Model):
    STATUS = [
        ('C', 'Completed'),
        ('X', 'Cancelled'),
        ('I', 'Incomplete'),
    ]
    customer = models.ForeignKey("auth_api.User",
                                 on_delete=models.CASCADE,
                                 related_name="orders")
    professional = models.ForeignKey(Professional,
                                     on_delete=models.CASCADE,
                                     related_name="orders")
    ordered_at = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)
    status = models.CharField(default='I',
                              max_length=1,
                              choices=STATUS)

class Item(models.Model):
    order = models.ForeignKey("Order",
                              on_delete=models.CASCADE,
                              related_name="items")
    subservice = models.OneToOneField("Subservice",
                                      on_delete=models.CASCADE)
    slot = models.OneToOneField(Slot,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.subservice.title
