from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    pub_date= models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=254)
    post = models.TextField()
    url = models.URLField(blank=False)

    def __str__(self):
        return self.title
