from django.db import models

class Manicurist(models.Model):
    name = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
        return f"Name: {self.name} Last name: {self.lastName}"

class Client_n(models.Model):
    name = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField()
    job = models.CharField(max_length=40)
    def __str__(self):
        return f"Name: {self.name} Last name: {self.lastName} Work to be performed: {self.job}"

class Turn(models.Model):
    date = models.DateTimeField()
    def __str__(self):
        return f"Turn: {self.date}"