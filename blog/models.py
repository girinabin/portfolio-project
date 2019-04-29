from django.db import models

# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def summary(self):
        return self.body[:50]

    def P_date(self):
        return self.pub_date.strftime("%m/%d/%Y")

    def __str__(self):
        return self.title



