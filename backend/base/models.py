# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Genres(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
      db_table = 'genres'

    def __str__(self):
        return self.name


class Keywords(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
      db_table = 'keywords'


class MovieGenre(models.Model):
    movie_id = models.IntegerField(blank=True, null=True)
    genre_id = models.IntegerField(blank=True, null=True)

    class Meta:
      db_table = 'movie_genre'


class MovieKeyword(models.Model):
    movie_id = models.IntegerField(blank=True, null=True)
    keyword_id = models.IntegerField(blank=True, null=True)

    class Meta:
      db_table = 'movie_keyword'


class Movies(models.Model):
    adult = models.IntegerField(blank=True, null=True)
    budget = models.BigIntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    imdb_id = models.CharField(max_length=255, blank=True, null=True)
    original_language = models.CharField(max_length=255, blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    release_date = models.CharField(max_length=255, blank=True, null=True)
    revenue = models.BigIntegerField(blank=True, null=True)
    runtime = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tagline = models.TextField(blank=True, null=True)
    vote_average = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    vote_count = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    poster_path = models.CharField(max_length=255, blank=True, null=True)
    popularity = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    homepage = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    count_in_stock = models.IntegerField()
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    class Meta:
      db_table = 'movies'

    def __str__(self):
        return str(self.id)

class Review(models.Model):
  movie = models.ForeignKey(Movies, on_delete=models.SET_NULL, null=True)
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=200, null=True, blank=True)
  rating = models.IntegerField(null=True, blank=True, default=0)
  comment = models.TextField(null=True, blank=True)
  createdAt = models.DateTimeField(auto_now_add=True)
  id = models.AutoField(primary_key=True, editable=False)

  class Meta:
    db_table = 'reviews'

  def __str__(self):
      return str(self.rating)

class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  paymentMethod = models.CharField(max_length=200, null=True, blank=True)
  itemsPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
  taxPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
  shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)  
  totalPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)      
  isPaid = models.BooleanField(default=False)
  paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
  isDelivered = models.BooleanField(default=False)
  deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
  createdAt = models.DateTimeField(auto_now_add=True)
  id = models.AutoField(primary_key=True, editable=False)

  class Meta:
      db_table = 'orders'

  def __str__(self):
      return str(self.createdAt)

class OrderItem(models.Model):
  movie = models.ForeignKey(Movies, on_delete=models.SET_NULL, null=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=200, null=True, blank=True)  
  qty = models.IntegerField(null=True, blank=True, default=0)
  price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
  image = models.CharField(max_length=200, null=True, blank=True) 
  id = models.AutoField(primary_key=True, editable=False)

  class Meta:
    db_table = 'order_item'

  def __str__(self):
      return str(self.name)

class ShippingAddress(models.Model):
  order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
  address = models.CharField(max_length=200, null=True, blank=True) 
  city = models.CharField(max_length=200, null=True, blank=True) 
  postalCode = models.CharField(max_length=200, null=True, blank=True) 
  country = models.CharField(max_length=200, null=True, blank=True) 
  shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
  id = models.AutoField(primary_key=True, editable=False)

  class Meta:
    db_table = 'shipping_address'

  def __str__(self):
    return str(self.address)  