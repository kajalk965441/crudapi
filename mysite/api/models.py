from django.db import models

class studentlist(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name