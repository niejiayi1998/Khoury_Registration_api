from django.db import models


# Department Model
class Department(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "1. Departments"

    def __str__(self):
        return self.name
