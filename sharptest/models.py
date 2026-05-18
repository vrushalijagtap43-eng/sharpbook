from django.db import models
import uuid
# Create your models here.
class BaseModel(models.Model):

    """Abstract base model for all entities."""

    id = models.UUIDField(primary_key= True,default=uuid.uuid4(),editable=False)
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



