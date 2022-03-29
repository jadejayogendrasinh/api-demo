from django.contrib import admin
from .models import CardItem, GIFsItem, QuotesItem

# Register your models here.
admin.site.register(CardItem)
admin.site.register(GIFsItem)
admin.site.register(QuotesItem)