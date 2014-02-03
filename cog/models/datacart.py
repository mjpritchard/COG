from django.db import models
from constants import APPLICATION_LABEL
from django.contrib.auth.models import User

class DataCart(models.Model):
    
    user = models.OneToOneField(User, related_name='datacart')
    
    class Meta:
        app_label= APPLICATION_LABEL
        
class DataCartItem(models.Model):
    
    cart = models.ForeignKey(DataCart, related_name="items", blank=False, null=False)
    
    # used to enforce uniqueness within a single user datacart
    identifier =  models.CharField(max_length=200, blank=False, null=False)
    
    name =  models.CharField(max_length=200, blank=False, null=False)
    type =  models.CharField(max_length=50, blank=False, null=False)
    
    class Meta:
        app_label= APPLICATION_LABEL
        
class DataCartItemMetadataKey(models.Model):

    item = models.ForeignKey(DataCartItem, blank=False, null=False)
    key =  models.CharField(max_length=200, blank=False, null=False)
    
    class Meta:
        app_label= APPLICATION_LABEL
    
class DataCartItemMetadataValue(models.Model):

    key = models.ForeignKey(DataCartItemMetadataKey, blank=False, null=False)
    value =  models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        app_label= APPLICATION_LABEL