from io import BytesIO
from django.core.files import File
from django.db import models
from PIL import Image
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('ordering', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/' % (self.slug)

class Spoon(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField (max_length=255)
    price = models.FloatField()
    num_available = models.IntegerField(default=0)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return f'{self.title} - Estoque: {self.num_available}'

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='variants', on_delete=models.CASCADE, blank=True, null=True)
    spoon = models.ForeignKey(Spoon, related_name='spoons', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    price = models.FloatField()
    is_featured = models.BooleanField(default=False)
    num_available = models.IntegerField(default=0)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    # Allergens.html table
    gluten = models.BooleanField(default=False)
    eggs = models.BooleanField(default=False)
    peanuts = models.BooleanField(default=False)
    soya = models.BooleanField(default=False)
    milk = models.BooleanField(default=False)
    nuts = models.BooleanField(default=False)
    oats = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_added', )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.thumbnail = self.make_thumbnail(self.image)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)
        return thumbnail


    def get_rating(self):
        total = sum(int(review['stars']) for review in self.reviews.values())

        if self.reviews.count() > 0:
            return total / self.reviews.count()
        else:
            return 0

class ProductImage(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.thumbnail = self.make_thumbnail(self.image)

        super().save(*args, **kwargs)

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

class ProductReview(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=False)
    stars = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added', )

    if content == '':
        content = 'Usuário não deixou comentário'
        content.save()

    def __str__(self):
        return f'{self.user} - {self.stars} - {self.product}'

class Cat(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added', )

    def __str__(self):
        return f'{self.name}'
