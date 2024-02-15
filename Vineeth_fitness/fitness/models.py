from django.db import models

# Create your models here.

class clients(models.Model):
    name = models.CharField(max_length = 256)
    def __str__(self):
        return f"{self.name}"




class clients_data(models.Model):
    # name = models.CharField(max_length = 256)
    clients_name = models.ForeignKey(clients, on_delete=models.CASCADE)
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.FloatField()
    gender = models.BooleanField()
    # email = models.EmailField(unique = True)
    phone_number = models.CharField(max_length = 30)
    # address = models.TextField()
    # date_of_birth = models.DateField()
    Note = models.CharField(max_length = 256)
    # created_at = models.DateTimeField(auto_now_add = True)
    # updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return f"{self.clients_name} - {self.age}"
        # class services(models.Model):
        #     service_name = models.CharField(max_length = 256)
        #     description = models.TextField()
        #     cost = models.DecimalField(decimal_places=2, max_digits=7)
        #     duration = models.TimeField()
        #     created_at = models.DateTimeField(auto_now_add = True)
        #     updated_at = models.DateTimeField(auto_now = True)
        #     def __str__(self):
        #         return f"{self.service_name} - ${self.cost}"

class food_table(models.Model):
    item_name = models.CharField(max_length = 256)
    calories = models.IntegerField()
    fat = models.FloatField()
    carbs = models.FloatField()
    protein = models.FloatField()
    price = models.DecimalField(decimal_places=2, max_digits=7)
    # created_at = models.DateTimeField(auto_now_add = True)
    # updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return f"{self.item_name} - {self.calories}"
    
class diet_table(models.Model):
    clients = models.ForeignKey(clients, on_delete = models.CASCADE)
    food_table = models.ForeignKey(food_table, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=100)
    # total = models.DecimalField(decimal_places=2, max_digits=7)

    # def sub_protein(self):
        # self.total -= (self.quantity * self.calories / 4)

    def sub_calories(self):
        return self.food_table.calories * self.quantity/100
    
    def sub_protein(self):
        return self.food_table.protein * self.quantity/100

    def sub_carbs(self):
        return self.food_table.carbs * self.quantity/100
    
    def sub_fat(self):
        return self.food_table.fat * self.quantity/100

    def __str__(self):
        return f"{self.clients.name} - {self.food_table.item_name}"