from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField
from django.db.models.lookups import In


class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    menu_id = models.ForeignKey('Menu', on_delete=models.CASCADE)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()
    nutrition_id = models.ForeignKey('Nutrition', on_delete=CASCADE)

    class Meta:
        db_table = 'products'

class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    product_id = models.ForeignKey('Product', on_delete=CASCADE)

    class Meta:
        db_table = 'images'

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sodium_mg = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    saturated_fat_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sugars_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    protein_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    caffeine_mg = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    size_ml = models.CharField(max_length=45, null=True)
    size_fluid_ounce = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'nutritions'

class Allergy(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'allergy'

class Allergy_product(models.Model):
    allergy_id = models.ForeignKey('Allergy', on_delete=CASCADE)
    product_id = models.ForeignKey('Product', on_delete=CASCADE)

    class Meta:
        db_table = 'allergy_products'