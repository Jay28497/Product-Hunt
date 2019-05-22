from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 150)
    image = models.ImageField(upload_to = 'images/')
    icon = models.ImageField(upload_to = 'images/')
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default = 1)
    body = models.TextField()
    url = models.TextField()
    hunter = models.ForeignKey(User, on_delete = models.CASCADE)


    def summary(self):
        return self.body[ :250]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')

    def __str__(self):
        return self.title
