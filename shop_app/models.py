from django.db import models




class BrandModel(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250, blank=True)
    res1 = models.CharField(max_length=250, blank=True)
    res2 = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f'{self.name}'


class CategoryModel(models.Model):
    name = models.CharField(max_length=250)
    res1 = models.CharField(max_length=250, blank=True)
    res2 = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f'{self.name}'


class WearModel(models.Model):
    brand = models.ForeignKey('BrandModel', on_delete=models.CASCADE)
    category = models.ForeignKey('CategoryModel', on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/%Y/%m/%d')
    price = models.PositiveIntegerField(blank=True)
    discount = models.PositiveIntegerField(blank=True, default=0)
    discount_image = models.ImageField(upload_to='%Y/%m/%d', blank=True, null=True)
    popular = models.BooleanField(default=True)
    res2 = models.CharField(max_length=250, blank=True)
    res3 = models.CharField(max_length=250, blank=True)
    res4 = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f'{self.description}'
