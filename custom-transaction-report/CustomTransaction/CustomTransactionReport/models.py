from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Student(models.Model):
#     name = models.CharField(max_length = 256)

#     def __str__(self):
#         return f'crazy stuff {self.name}'

# class Marks(models.Model):
#     subject_name = models.CharField(max_length = 128)
#     score = models.IntegerField()
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Transcations(models.Model):

    customer_name = models.CharField(max_length = 256)
    merchant_name = models.ForeignKey(User, on_delete = models.CASCADE)
    pin_Code = models.IntegerField()
    date_field = models.DateField()
    total_Transaction = models.IntegerField()

    def __str__(self):
        return self.customer_name

# class customer(models.Model):
#     full_name = models.CharField(max_length = 256)
#     user = models.ForeignKey(User, on_delete = models.CASCADE)

class Product(models.Model):
    product_name = models.CharField(max_length = 256)
    cost = models.IntegerField()

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    customer = models.ForeignKey(Transcations, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def subtotal(self):
        return self.product.cost * self.quantity
        # return 'hari'

# class Customer_volume_report(models.Model):
#     customer = models.ForeignKey(Transcations, on_delete = models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    # def customer_name(self):
    #     cust_dict_ = {}
    #     name = self.customer.customer_name
        




    

