from django.contrib import admin
from ut.models import uniq

# Register your models here.


class green(admin.ModelAdmin):
    table=["PRODUCT_NAME","PRODUCT_NAME","PRICE","GST","FOODPRODECT"]

admin.site.register(uniq,green)
