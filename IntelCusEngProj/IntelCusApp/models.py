from django.db import models

# Create your models here.
class MainTable(models.Model):
    service_provider_name = models.TextField()
    response_code = models.TextField()
    error_message = models.TextField()
    account_number = models.BigIntegerField()
    threshold = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.service_provider_name


class UsersServiceProvider(models.Model):
    email = models.EmailField()
    phone = models.IntegerField()
    service_provider_name = models.CharField(max_length=100)
