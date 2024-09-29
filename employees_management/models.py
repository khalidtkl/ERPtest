from django.db import models

# Country model
class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# City model
class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# AddressType model
class AddressType(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# ContactType model
class ContactType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Employee model
class Employee(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

# Address model
class Address(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    address_type = models.ForeignKey(AddressType, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    remarks = models.TextField(null=True, blank=True)

# Contact model
class Contact(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    contact_type = models.ForeignKey(ContactType, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)

# Document model
class Document(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    file_description = models.CharField(max_length=255)
    remarks = models.TextField(null=True, blank=True)
