from django.db import models

class Shipping(models.Model):
    place = models.CharField(max_length=100, unique=True)
    value = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.place} - {self.active}'

    def can_ship(self):
        is_active = True

        if self.active == False:
            is_active = False

        return is_active
