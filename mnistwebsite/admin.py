from django.contrib import admin
from .models import given_image,predicted_label,image_name
# Register your models here.

admin.site.register(given_image)
admin.site.register(predicted_label)
admin.site.register(image_name)