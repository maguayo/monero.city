import uuid
from django.db import models
from django.contrib.auth.models import User
from slugify import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Listing(BaseModel):
    name = models.CharField(max_length=55)
    slug = models.SlugField()
    image = models.FileField()
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    website = models.URLField(max_length=254)

    map_lat = models.CharField(max_length=20)
    map_long = models.CharField(max_length=20)

    # Meta
    address = models.CharField(max_length=254)
    city = models.CharField(max_length=189)
    zip_code = models.CharField(max_length=18)
    country = models.CharField(max_length=90)

    approved = models.BooleanField(default=False)


@receiver(pre_save, sender=Listing)
def create_slug(sender, instance=None, created=False, **kwargs):
    slug_location = ''
    if instance.city and instance.city != '-' or instance.city != '':
        slug_location = slug_location + instance.city

    if instance.country and instance.country != '-' or instance.country != '':
        slug_location = slug_location + '-' + instance.country

    instance.slug = slugify(instance.name) + '-in-' + slugify(slug_location)


class Review(BaseModel):
    listing = models.ForeignKey(Listing, related_name="reviewed_listing", on_delete=models.PROTECT)
    user = models.ForeignKey(Listing, related_name="user_rating", on_delete=models.PROTECT)
    rating = models.IntegerField(default=0)
    review = models.CharField(max_length=254)


class Tip(BaseModel):
    listing = models.ForeignKey(Listing, related_name="tip_listing", on_delete=models.PROTECT)
    user = models.ForeignKey(Listing, related_name="user_tip", on_delete=models.PROTECT)
    tip = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

