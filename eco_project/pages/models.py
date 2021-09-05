from django.db import models

# Create your models here.
from django.db import models
from django.db.models import signals


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=255)
    bar_code = models.CharField(max_length=255)
    description = models.TextField()
    gallery_image_path = models.CharField(max_length=255)


class MyUser(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255)

    def check_username_and_password(self, username, password):
        if username == self.username and password == self.password:
            return True
        return False


def product_post_save(sender, instance, created, **kwargs):
    import barcode
    from barcode.writer import ImageWriter
    EAN = barcode.get_barcode_class('ean13')
    ean = EAN(str(instance.bar_code), writer=ImageWriter())
    fullname = ean.save("static/img/" + instance.gallery_image_path + '-barcode')


signals.post_save.connect(receiver=product_post_save, sender=Product)
