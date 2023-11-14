from django.db import models

class Model_kerudung(models.Model):
  tipe = models.CharField(max_length=255)
  warna = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.tipe}"