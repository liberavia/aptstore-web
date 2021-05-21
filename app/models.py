from django.db import models


class Category(models.Model):
    name = models.CharField(default='', max_length=50)

    class Meta:
        verbose_name = "Category"

    def __str__(self):
        return self.name


class CategoryRegional(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    region = models.CharField(db_index=True, max_length=7)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Category Regional"

    def __str__(self):
        return self.name


class Tag(models.Model):
    region = models.CharField(null=True, max_length=7)
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Tag "

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Platform"

    def __str__(self):
        return self.name


class App(models.Model):
    ident = models.CharField(db_index=True, max_length=50)
    ident_rating = models.CharField(max_length=100)
    name = models.CharField(db_index=True, max_length=100)
    image_banner = models.CharField(null=True, blank=True, max_length=200)
    image_thumb = models.CharField(null=True, blank=True, max_length=200)
    image_details = models.CharField(null=True, blank=True, max_length=200)
    image_zoom = models.CharField(null=True, blank=True, max_length=200)
    publisher = models.CharField(null=True, blank=True, max_length=50)
    teaser = models.BooleanField(default=False, db_index=True)
    featured = models.BooleanField(default=False, db_index=True)
    required_age_usk = models.IntegerField(default=99)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    platforms = models.ManyToManyField(Platform)

    class Meta:
        verbose_name = "Aptstore App"

    def __str__(self):
        return self.name


class Screenshot(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=200)
    app = models.ForeignKey(App, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Screenshot"

    def __str__(self):
        return self.name


class AppRegional(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE, null=True)
    region = models.CharField(db_index=True, max_length=7)
    description_short = models.CharField(null=True, blank=True, max_length=200)
    description_long = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    price_initial = models.IntegerField(default=0)
    currency = models.CharField(max_length=3)

    class Meta:
        verbose_name = "App Regional"

    def __str__(self):
        return self.region
