import random
from django.core.management.base import BaseCommand
from employees_management.models import Employee, Address, Contact, ContactType, AddressType, Country, City

class Command(BaseCommand):
    help = 'Create big dummy data for testing and development'

    def handle(self, *args, **kwargs):
        # Create country and city
        country = Country.objects.create(name='United States')
        city = City.objects.create(name='New York', country=country)

        # Create contact types
        contact_type_email = ContactType.objects.create(name='Email', code='CT001')
        contact_type_phone = ContactType.objects.create(name='Phone', code='CT002')

        # Create address types
        address_type_home = AddressType.objects.create(name='Home', code='AT001')
        address_type_work = AddressType.objects.create(name='Work', code='AT002')

        # Generate 1000 dummy employee records
        for i in range(1, 1001):
            employee = Employee.objects.create(
                code=f'EMP{i:04}',
                name=f'Employee {i}',
                birthday='1990-01-01',  # Assign a dummy birthdate
                remarks=f'This is a remark for employee {i}'
            )

            # Create addresses for the employee
            Address.objects.create(
                employee=employee,
                address_type=address_type_home,
                city=city,
                country=country,
                remarks=f'Home address for Employee {i}'
            )
            Address.objects.create(
                employee=employee,
                address_type=address_type_work,
                city=city,
                country=country,
                remarks=f'Work address for Employee {i}'
            )

            # Create contacts for the employee
            Contact.objects.create(
                employee=employee,
                contact_type=contact_type_email,
                value=f'employee{i}@example.com'
            )
            Contact.objects.create(
                employee=employee,
                contact_type=contact_type_phone,
                value=f'+1555000{i:04}'  # Dummy phone number
            )

        self.stdout.write(self.style.SUCCESS('Successfully created 1000 employees with associated addresses and contacts'))
