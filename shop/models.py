from django.db import models

class Furniture(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='furniture_images/')

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Cart"
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.furniture.name} in {self.cart.user.username}'s Cart"    
# Create your models here.
