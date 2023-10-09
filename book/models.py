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
        return self.title[:20]

class Subservice(models.Model):
    service = models.ForeignKey("Service",
                                on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to='subservice')
    title = models.CharField(max_length=200,
                             null=False,
                             blank=False)
    price = models.CharField(max_length=10,
                             null=True,
                             blank=True)

    def __str__(self):
        return title[:20]

class Slot(models.Model):
    staff = models.ForeignKey("auth_api.User",
                              on_delete=models.CASCADE,
                              related_name="slots")
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return f'{self.start_time} - {self.end_time}'
 #      return datetime.combine(datetime.now().date(), self.start_time) - datetime.combine(datetime.now().date(), self.end_time) 

class Order(models.Model):
    customer = models.ForeignKey("auth_api.User",
                                 on_delete=models.CASCADE,
                                 related_name="orders")
    staff = models.ForeignKey("auth_api.User",
                                 on_delete=models.CASCADE)
    slot = models.OneToOneField("Slot",
                             on_delete=models.CASCADE)

    ordered = models.DateTimeField(auto_now_add=True)

    def total(self):
        sum = 0
        for item in self.items:
            sum += item.price()


class Item(models.Model):
    order = models.ForeignKey("Order",
                              on_delete=models.CASCADE,
                              related_name="items")
    subservice = models.OneToOneField("Subservice",
                                      on_delete=models.CASCADE)

    def price(self):
        return int(self.subservice.price)
