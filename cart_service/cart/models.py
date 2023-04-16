from django.db import models

class Cart(models.Model):
    user_id = models.IntegerField()
    cart_id = models.CharField(max_length=255)
    items = models.JSONField()

    def __str__(self):
        return self.cart_id
