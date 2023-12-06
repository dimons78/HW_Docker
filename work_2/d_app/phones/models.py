from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.TextField(max_length=100)

    price = models.FloatField(max_length=100)

    image = models.URLField(max_length=100)
    release_date = models.DateField(max_length=100)

    lte_exists = models.BooleanField(max_length=100)

    slug = models.SlugField(max_length=100)






