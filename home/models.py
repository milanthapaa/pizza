from django.db import models
from django.contrib.auth.models import User
import uuid


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PizzaCategory(BaseModel):
    category_name = models.CharField(max_length=100)


class Pizza(BaseModel):
    pizza_category = models.ForeignKey(PizzaCategory, on_delete=models.CASCADE, related_name="pizzas")
    pizza_name = models.CharField(max_length=100)
    price = models.IntegerField(default=100)
    image = models.ImageField(upload_to='pizza', blank=True)


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="carts", null=True, blank=True)
    is_paid = models.BooleanField(default=False)


class CartItems(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
