from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title')
    slug = models.SlugField(max_length=300, verbose_name='URL', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ProductDetails(models.Model):
    color = models.CharField(max_length=200, verbose_name='Color')
    size = models.CharField(max_length=200, verbose_name='Size')

    def __str__(self):
        return f'{self.color} - {self.size}'

    class Meta:
        verbose_name = 'Product details'
        verbose_name_plural = 'Product details'


class ProductTag(models.Model):
    tag = models.CharField(max_length=200, verbose_name='Product Tag')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Product Tag'
        verbose_name_plural = 'Product Tags'


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    price = models.IntegerField(verbose_name='Price')
    description = models.CharField(max_length=300, verbose_name='Description')
    slug = models.SlugField(default='', null=False, unique=True,
                            db_index=True, verbose_name='Slug')
    rate = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)],
                               verbose_name='Score')
    is_active = models.BooleanField(verbose_name='Status')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='Category')
    details = models.OneToOneField(ProductDetails, null=True, blank=True, on_delete=models.CASCADE,
                                   verbose_name='Details', related_name='product_details')
    tag = models.ManyToManyField(ProductTag, verbose_name='Product Tag')

    def get_absolute_url(self):
        return reverse('product-details', args={self.title})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} - {self.description} - ${self.price}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Karbaran(models.Model):
    name = models.CharField(max_length=20)
    family = models.CharField(max_length=20)
    age = models.IntegerField()
    is_active = models.BooleanField()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
