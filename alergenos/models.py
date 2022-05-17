from django.db import models

class Alergeno(models.Model):
    alergeno = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.alergeno

    class Meta:
        verbose_name_plural = "Alergenos"