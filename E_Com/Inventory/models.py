from autoslug import AutoSlugField
from django.db import models
# Create your models here.
from rest_framework.reverse import reverse


class Size(models.Model):
    size_name = models.CharField(max_length=200, help_text="Size (XL/L/M/S/XS)")
    size_length = models.IntegerField(default=0)
    size_UK = models.IntegerField(default=0)
    size_US = models.IntegerField(default=0)

    def __str__(self):
        return self.size_name


class Product(models.Model):
    pr_name = models.CharField(max_length=200, help_text="Product Name")
    sku = AutoSlugField(populate_from='pr_name')
    act_price = models.CharField(max_length=200, help_text="Actual Price")
    disc_price = models.IntegerField(default=0, help_text="Discounted Price")
    pr_fabric = models.CharField(max_length=200, help_text="Fabric")
    pr_colour = models.CharField(max_length=200, help_text="Colour")
    pr_size = models.ForeignKey(Size, on_delete=models.CASCADE, help_text="Size of Product")
    pr_description = models.TextField(default=None, help_text="Product Descriptions")
    publish_status = models.BooleanField(default=False)

    def __str__(self):
        return self.pr_name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Family.
        """
        return reverse('family-detail-view', args=[str(self.pr_name)])
