from django.db import models


class Blogspot(models.Model):
    postal_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    headA = models.CharField(max_length=500, default="")
    cheadA = models.CharField(max_length=5000, default="")
    headB = models.CharField(max_length=500, default="")
    cheadB = models.CharField(max_length=5000, default="")
    headC = models.CharField(max_length=500, default="")
    cheadC = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()
    images = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.title
