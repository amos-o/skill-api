from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=80, blank=False, default='')
    description = models.TextField(blank=False, default='')

    def __str__(self):
        return self.name
