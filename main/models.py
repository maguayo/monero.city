import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Listing(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField()

    map_lat = models.CharField(max_length=20)
    map_long = models.CharField(max_length=20)

    # Meta
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=50)
    country = models.CharField(max_length=255)

    approved = models.BooleanField(default=False)


class Review(BaseModel):
    listing = models.ForeignKey(Listing, related_name="reviewed_listing", on_delete=models.PROTECT)
    user = models.ForeignKey(Listing, related_name="user_rating", on_delete=models.PROTECT)
    rating = models.IntegerField(default=0)
    review = models.CharField(max_length=255)


class Tip(BaseModel):
    listing = models.ForeignKey(Listing, related_name="tip_listing", on_delete=models.PROTECT)
    user = models.ForeignKey(Listing, related_name="user_tip", on_delete=models.PROTECT)
    tip = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

