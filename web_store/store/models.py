from django.db import models

# Logos Class
class storeItem(models.Model):
    """"This is a class that store info about the 
    shoes in the database

    :param image: Shoe image
    :param info: Shoe info
    :param brand: Shoe brand
    """"

    image = models.ImageField(upload_to='images/')
    info = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, default='brand')

    def __str__(self):
        """Return a str version of an object
        """
        return self.info
    
# Stock Class
class stockItem(models.Model):
    """"This is a class that stores info about the 
    stock in the database

    :param image: Shoe image
    :param info: Shoe info
    :param brand: Shoe brand
    """"
    image = models.ImageField(upload_to='images/')
    info = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, default='brand')
    price = models.CharField(max_length=200, default='price')

    def __str__(self):
        """Return a str version of an object
        """
        return self.info
    
