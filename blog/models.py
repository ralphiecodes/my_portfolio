from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    description = models.CharField(max_length=300)
    body = models.TextField(null=True)

    def __str__(self):
        return self.title, self.date

