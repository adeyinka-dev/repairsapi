from django.db import models


class Repair(models.Model):
    type = models.CharField(max_length=50)
    subtype = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.type}-{self.subtype}"
