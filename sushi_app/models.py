from django.db import models

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


# Create your models here.
class Sushi(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=100, choices=INGREDIENTS)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__ (self):
        return self.name 
