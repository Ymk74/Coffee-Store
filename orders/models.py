from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.



class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    detail = models.ManyToManyField(Product , through='OrderDetail')
    is_finished = models.BooleanField()

    def __str__(self):
        return 'User :'  + self.user.username + ',order id :' +  str(self.id)
    

class OrderDetail(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6 , decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return 'User:' + self.order.user.username + ',product : ' + self.product.name + 'order id : ' + str(self.order.id)
        