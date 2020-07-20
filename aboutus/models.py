from django.db import models

# Create your models here.

class AboutUs(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    #image=models.ImageField(upload_to='about_us/')

    class Meta:
        verbose_name ='about us'
        verbose_name_plural ='about us'
        
    def __str__(self):
        return self.title



class Why_Choose_US(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()

    class Meta:
        verbose_name ='Why Choose us'
        verbose_name_plural ='Why Choose us'

    
    def __str__(self):
        return self.title

    

