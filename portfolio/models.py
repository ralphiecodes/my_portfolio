from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='portfolio/images/')
    github_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)
    detail_one = models.CharField(blank=True,max_length=100)
    detail_two = models.CharField(blank=True,max_length=100)
    detail_three = models.CharField(blank=True,max_length=100)
    detail_four = models.CharField(blank=True,max_length=100)
    detail_five = models.CharField(blank=True,max_length=100)
    detail_six = models.CharField(blank=True,max_length=100)


    def __str__(self):
        return self.title