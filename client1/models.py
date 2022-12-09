from django.db import models
from phonenumber_field.modelfields import PhoneNumberField





class Persone(models.Model):
    name = models.CharField("Name", max_length=30, blank=False)
    second_name = models.CharField("Second name", max_length=35, blank=False, default=str)
    age = models.IntegerField("Age", default=0)
    sum_of_insurence = models.IntegerField("Sum of insurence", default=0)
    
    
    
    
    def __str__(self):
        
        return f'{self.name} {self.second_name} {self.age} {self.sum_of_insurence}'
    
    
    def all_phones_to_string(self):
        return ", ".join([phone.phone for phone in self.phones.all()])


class Phone(models.Model):
    phone = models.CharField(
        verbose_name="Phone",
        max_length=12
    )
    contact = models.ForeignKey(
        Persone,
        related_name="phones",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.phone
    
