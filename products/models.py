from django.db import models
import uuid
# Create your models here.

# DRY => Donot repeat yourself

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    created_at = models.DateField(auto_created=True)
    updated_at = models.DateField(auto_created=True)

    class Meta:
        abstract = True #Django now treats the above code as class not model

class Product(BaseModel):
    product_name = models.CharField(max_length=150)
    product_slug = models.SlugField(unique=True)
    product_description = models.TextField()
    product_price = models.FloatField(default=0.00)
    actual_product_price = models.FloatField(default=0)


class ProductMetaInformation(BaseModel):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name = "meta_info")
    product_measurement = models.CharField(max_length = 100,null = True , blank = True, choices = (("KG","KG"),("L","L"),("ML","ML"),("G","G"),(None,None)))
    product_quantity = models.CharField(null = True , blank = True)
    is_restrict = models.BooleanField(default=False)
    restrict_quantity = models.IntegerField()


class ProductImages(BaseModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name = "images")
    product_image = models.ImageField(upload_to='products')