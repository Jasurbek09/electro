from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')
    is_main = models.BooleanField()

    def __str__(self):
        return self.title

class Size(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class Color(models.Model):
    title = models.CharField(max_length=300)
    code = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class Product (models.Model):
    title = models.CharField(max_length=300)
    reating = models.FloatField(default=0.0)
    views = models.IntegerField(default=0)
    old_price = models.IntegerField(default=0)
    new_price = models.IntegerField(default=0)
    short_description = models.TextField()
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    details = models.TextField()
    logo = models.ImageField(upload_to='upload')
    discount = models.IntegerField(default=0)
    is_new = models.BooleanField()
    is_best_saler = models.BooleanField()

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class CommentItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    author_name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    rating = models.IntegerField(default=0)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.text