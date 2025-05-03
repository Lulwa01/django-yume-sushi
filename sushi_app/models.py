from django.db import models
from django.urls import reverse

INGREDIENTS = (
    ('Tuna', 'Tuna'),
    ('Salmon', 'Salmon'),
    ('Crab Stick', 'Crab Stick'),
    ('Shrimp Tempura', 'Shrimp Tempura'),
    ('Eel', 'Eel'),
    ('Avocado', 'Avocado'),
    ('Cucumber', 'Cucumber'),
    ('Cream Cheese', 'Cream Cheese'),
    ('Spicy Mayo', 'Spicy Mayo'),
    ('Wasabi', 'Wasabi'),
    ('Pickled Ginger', 'Pickled Ginger'),
    ('Tamago (Sweet Egg)', 'Tamago (Sweet Egg)'),
    ('Tobiko (Fish Roe)', 'Tobiko (Fish Roe)'),
    ('Sesame Seeds', 'Sesame Seeds'),
    ('Chili Flakes', 'Chili Flakes'),
    ('Spring Onion', 'Spring Onion'),
    ('Carrot', 'Carrot'),
    ('Lettuce', 'Lettuce'),
    ('Radish', 'Radish'),
    ('Seaweed Salad', 'Seaweed Salad'),
    ('Teriyaki Sauce', 'Teriyaki Sauce'),
    ('Soy Sauce', 'Soy Sauce'),
    ('Rice Vinegar', 'Rice Vinegar'),
    ('Sriracha', 'Sriracha'),
)

DRINKS = (
    ('Green Tea', 'Green Tea'),
    ('Matcha Latte', 'Matcha Latte'),
    ('Ramune Soda', 'Ramune Soda'),
    ('Yuzu Juice', 'Yuzu Juice'),
    ('Calpico', 'Calpico'),
    ('Iced Genmaicha', 'Iced Genmaicha'),
    ('Sparkling Water', 'Sparkling Water'),
    ('Cold Brewed Hojicha', 'Cold Brewed Hojicha'),
    ('Plum Juice', 'Plum Juice'),
)

STARTER = (
    ('Edamame', 'Edamame'),
    ('Miso Soup', 'Miso Soup'),
    ('Seaweed Salad', 'Seaweed Salad'),
    ('Gyoza', 'Gyoza'),
    ('Takoyaki', 'Takoyaki'),
    ('Agedashi Tofu', 'Agedashi Tofu'),
    ('Sunomono', 'Sunomono'),
    ('Shishito Peppers', 'Shishito Peppers'),
    ('Chawanmushi', 'Chawanmushi'),
)

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=100, choices=INGREDIENTS)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__ (self):
        return self.name 
    
    def get_absolute_url(self):
        return reverse('order-detail', kwargs={'order_id': self.id})
    
class Side(models.Model):
    drinks = models.CharField(max_length=100, choices=DRINKS)    
    starter = models.CharField(max_length=100, choices=STARTER)

    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.drinks} on {self.starter}"