from django.db import models
from django.db.models import Q

from core.models import BaseModel


def category_dir_path(instance, filename):
    return 'category/{0}/{1}/{2}'.format(instance.title, "image", filename)


class Category(BaseModel):

    class Meta:
        verbose_name_plural = 'Categories'

    parent_category = models.ForeignKey(
        'self',
        verbose_name="Parent Category",
        related_name="subcategories",
        null=True,
        blank=True,
    )
    title = models.CharField(
        verbose_name="Category title",
        max_length=1000,
        unique=True
    )
    priority_order = models.IntegerField(
        verbose_name="Priority order",
        default=1,
    )
    description = models.TextField(
        verbose_name="description",
    )
    image = models.ImageField(
        verbose_name="Image",
        null=True,
        blank=True,
        upload_to=category_dir_path
    )

    def __str__(self):
        return self.title


def product_image_dir_path(instance, filename):
    return 'product/{0}/{1}/{2}'.format(instance.product.title, "images", filename)


class ProductImage(BaseModel):

    image = models.ImageField(
        verbose_name="Image",
        upload_to=product_image_dir_path,
    )
    product = models.ForeignKey(
        'Product',
        verbose_name="product",
        related_name="images"
    )
    priority_order = models.IntegerField(
        verbose_name="Priority Order",
        default=1,
    )

    def __str__(self):
        return self.image.name


class Product(BaseModel):

    category = models.ForeignKey(
        Category,
        verbose_name="Category",
        related_name="products",
    )
    priority_order = models.IntegerField(
        verbose_name="Priority Order",
        default=1,
    )
    title = models.CharField(max_length=1000, db_index=True)
    description = models.TextField()
    long_description = models.TextField()

    old_price = models.FloatField(
        verbose_name="Old product price",
        null=True,
        blank=True,
    )
    price = models.FloatField(
        verbose_name="Product price",
        null=True,
        blank=True,
    )
    price_units = models.CharField(
        max_length=100,
        default="руб./секция",
    )

    old_installation_price = models.FloatField(
        verbose_name="Old installation product price",
        null=True,
        blank=True,
    )
    installation_price = models.FloatField(
        verbose_name="Installation product price",
        null=True,
        blank=True,
    )
    installation_price_units = models.CharField(
        max_length=100,
        default="руб./секция",
    )

    old_premium_installation_price = models.FloatField(
        verbose_name="Old premium installation product price",
        null=True,
        blank=True,
    )
    premium_installation_price = models.FloatField(
        verbose_name="Premium installation product price",
        null=True,
        blank=True,
    )
    premium_installation_price_units = models.CharField(
        max_length=100,
        default="руб./секция",
    )
    is_favorite = models.BooleanField(
        "Is favorite product?",
        default=False,
    )

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.category.subcategories.exists():
            raise ValueError("Can't add product to parent category")
        return super(Product, self).save(force_insert, force_update, using,
                                         update_fields)

    def __str__(self):
        return self.title


class Specification(BaseModel):

    product = models.ForeignKey(
        Product,
        verbose_name="Product",
        related_name="specifications",
    )
    priority_order = models.IntegerField(
        verbose_name="Priority order",
        default=1,
    )
    title = models.TextField(
        verbose_name="Title"
    )
    value = models.TextField(
        verbose_name="Value"
    )

    def __str__(self):
        return self.title


class Requisites(BaseModel):

    address = models.CharField(
        verbose_name="Address",
        max_length=1000,
        null=True,
        blank=True,
    )
    phone = models.CharField(
        verbose_name="Phone number",
        max_length=20,
        null=True,
        blank=True,
    )
    additional_phone = models.CharField(
        verbose_name="Additional phone number",
        max_length=20,
        null=True,
        blank=True,
    )
    email = models.CharField(
        verbose_name="Email",
        max_length=100,
        null=True,
        blank=True,
    )
    working_hours = models.CharField(
        verbose_name="Working Hours",
        max_length=100,
        null=True,
        blank=True,
    )
    area = models.TextField(
        verbose_name="Area",
        null=True,
        blank=True,
    )
    additional_area_info = models.TextField(
        verbose_name="Additional area information",
        null=True,
        blank=True,
    )

    requisites = models.TextField(
        verbose_name="Requisites",
        null=True,
        blank=True,
    )

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        result = super(Requisites, self).save(force_insert, force_update,
                                              using, update_fields)
        Requisites.objects.filter(~Q(id=self.id)).delete()
        return result
