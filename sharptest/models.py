from django.db import models
import uuid
# Create your models here.
class BaseModel(models.Model):

    """Abstract base model for all entities."""

    id = models.UUIDField(primary_key= True,default=uuid.uuid4,editable=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    is_active= models.BooleanField(default=True)

    class Meta:
        abstract= True


class Brand(BaseModel):
    """Represents a barbershop brand (tenant)."""

    name= models.CharField(max_length= 200)
    slug= models.SlugField(unique= True)
    logo= models.URLField(blank= True,null= True)
    descriptions= models.TextField(blank= True)
    primary_color= models.CharField(max_length= 7, default='000000')
    secondary_color= models.CharField(max_length= 7,default= 'FFFFFF')
    contact_email= models.EmailField()
    contact_phone=models.CharField(max_length=20)
    website= models.URLField(blank= True,null= True)

    class Meta:
        db_table = "brands"
        ordering = ["name"]

    def __str__(self):
        return self.name


class ServiceCategory(BaseModel):
    """Categories for services (e.g., Haircuts, Shaves, Coloring)."""
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="service_categories")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    display_order = models.PositiveIntegerField(default=0)
    class Meta:
        db_table = "service_categories"
        ordering = ["display_order", "name"]
        unique_together = ["brand", "name"]
    def __str__(self):
        return f"{self.brand.name} - {self.name}"

class Service(BaseModel):
    """Individual service offered by the brand."""
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name="services")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    duration_minutes = models.PositiveIntegerField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(blank=True, null=True)
    class Meta:
        db_table = "services"
        ordering = ["category", "name"]
    def __str__(self):
        return self.name


class Package(BaseModel):
    """Bundle of services at discounted price."""
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="packages")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    # services = models.ManyToManyField(Service, related_name="packages")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    image = models.URLField(blank=True, null=True)

    class Meta:
        db_table = "packages"

    def __str__(self):
        return self.name


class Product(BaseModel):
    """Retail products sold at stores."""
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    sku = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    stock_quantity = models.PositiveIntegerField(default=0)
    image = models.URLField(blank=True, null=True)
    class Meta:
        db_table = "products"
    def __str__(self):
        return self.name

class Store(BaseModel):
    """Physical store location."""
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="stores")

    # city = models.ForeignKey(City, on_delete=models.PROTECT, related_name="stores")
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    image = models.URLField(blank=True, null=True)
    class Meta:
        db_table = "stores"
        unique_together = ["brand", "slug"]
    def __str__(self):
        return f"{self.brand.name} - {self.name}"

class Review(BaseModel):

    store = models.ForeignKey(Store,on_delete=models.CASCADE,related_name="store")
    rating = models.IntegerField(max_length=5)
    title = models.CharField(max_length=200)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=True)

    def __str__(self):
        return self.title

