from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Genres)
admin.site.register(Keywords)
admin.site.register(MovieGenre)
admin.site.register(MovieKeyword)
admin.site.register(Movies)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

