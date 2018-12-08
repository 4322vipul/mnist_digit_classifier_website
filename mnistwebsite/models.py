from django.db import models

# Create your models here.


class given_image(models.Model):
    image_given=models.ImageField(max_length=64)
    
class image_name(models.Model):
    name_of_image=models.CharField(max_length=64)
    
    def __str__(self):
        return self.name_of_image
        
    

class predicted_label(models.Model):
    label=models.CharField(max_length=8)
    
    def __str__(self):
        return self.label
    
    
    
    
    
