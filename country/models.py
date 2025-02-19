from django.db import models

# Create your models here.
# class Country(models.Model):
#     name = models.CharField(max_length=100)
#     top_level_domain = models.JSONField()
#     alpha2_code = models.CharField(max_length=20)
#     alpha3_code = models.CharField(max_length=20)
#     calling_codes = models.JSONField()
#     capital = models.CharField(max_length=100)
#     alt_spellings = models.JSONField()
#     region = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)
    cca2 = models.CharField(max_length=30)
    capital = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100)
    language = models.CharField(max_length=200, blank=True, null=True)
    population = models.IntegerField()
    timezone = models.CharField(max_length=200)
    flag = models.URLField()

    def __str__(self):
        return self.name
