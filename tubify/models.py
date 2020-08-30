from django.db import models

# Create your models here.
class Tubify(models.Model):
    v_id = models.CharField(max_length=128, null=False)
    v_title = models.CharField(max_length=128)
    v_views = models.CharField(max_length=128)
    v_thumb = models.CharField(max_length=128)
    v_url_suffix = models.CharField(max_length=128)

    def __str__(self):
        return f"Video title: {self.v_title}+Video id: {self.v_id}"