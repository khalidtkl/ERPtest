from django.test import TestCase
from django.urls import reverse
from employees_management.models import Document

from .models import Employee, AddressType, Address, Country, City, ContactType, Contact, Document
from .forms import EmployeeForm

# class CountryModelTests(TestCase):
#     def setUp(self):
#         self.country = Country.objects.create(
#             name='United States'
#         )
#
#     def test_country_str(self):
#         self.assertEqual(str(self.country), 'United States')
#
# class CityModelTests(TestCase):
#     def setUp(self):
#         self.country = Country.objects.create(
#             name='United States'
#         )
#         self.city = City.objects.create(
#             name='New York',
#             country=self.country
#         )
#
#     def test_city_str(self):
#         self.assertEqual(str(self.city), 'New York')
#
# class EmployeeModelTests(TestCase):
#     def setUp(self):
#         self.country = Country.objects.create(
#             name='United States'
#         )
#         self.city = City.objects.create(
#             name='New York',
#             country=self.country
#         )
#         self.address_type = AddressType.objects.create(
#             code='AT001',
#             name='Home'
#         )
#         self.employee = Employee.objects.create(
#             code='EMP001',
#             name='John Doe',
#             birthday='1990-01-01',
#             remarks='Test employee'
#         )
#         self.address = Address.objects.create(
#             employee=self.employee,
#             address_type=self.address_type,
#             remarks='123 Main St',
#             country=self.country,
#             city=self.city
#         )
#
#     def test_employee_str(self):
#         self.assertEqual(str(self.employee), 'John Doe')
#
# class AddressTypeModelTests(TestCase):
#     def setUp(self):
#         self.address_type = AddressType.objects.create(
#             code='AT001',
#             name='Home'
#         )
#
#     def test_address_type_str(self):
#         self.assertEqual(str(self.address_type), 'Home')
#
# class EmployeeViewTests(TestCase):
#     def setUp(self):
#         self.country = Country.objects.create(name='United States')
#         self.city = City.objects.create(name='New York', country=self.country)
#         self.address_type = AddressType.objects.create(
#             code='AT001',
#             name='Home'
#         )
#         self.employee = Employee.objects.create(
#             code='EMP001',
#             name='John Doe',
#             birthday='1990-01-01',
#             remarks='Test employee'
#         )
#         self.address = Address.objects.create(
#             employee=self.employee,
#             address_type=self.address_type,
#             remarks='123 Main St',
#             country=self.country,
#             city=self.city
#         )
#
#     def test_employee_list_view(self):
#         response = self.client.get(reverse('employee_list'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'employees/employee_list.html')  # Updated template path
#         self.assertContains(response, 'John Doe')
#
#     # def test_employee_detail_view(self):
#     #     response = self.client.get(reverse('employee_detail', kwargs={'pk': self.employee.pk}))
#     #     self.assertEqual(response.status_code, 200)
#     #     self.assertTemplateUsed(response, 'employees/employee_detail.html')  # Updated template path
#     #     self.assertContains(response, 'John Doe')
#
#     def test_employee_create_view(self):
#         response = self.client.post(reverse('employee_create'), {
#             'code': 'EMP002',
#             'name': 'Jane Doe 2',
#             'birthday': '1995-05-05',
#             'remarks': 'New employee',
#             'address_set-0-address_type': self.address_type.id,
#             'address_set-0-remarks': '456 Elm St',
#             'address_set-0-country': self.country.id,
#             'address_set-0-city': self.city.id,
#         })
#         self.assertEqual(response.status_code, 302)  # Check for redirect
#         # self.assertTrue(Employee.objects.filter(name='Jane Doe 2').exists())
#
#     def test_employee_update_view(self):
#         response = self.client.post(reverse('employee_update', kwargs={'pk': self.employee.pk}), {
#             'code': 'EMP001',
#             'name': 'John Smith',
#             'birthday': '1990-01-01',
#             'remarks': 'Updated employee'
#         })
#         self.assertEqual(response.status_code, 200)  # Check for redirect
#         self.employee.refresh_from_db()
        # self.assertEqual(self.employee.name, 'John Smith')

    # def test_employee_delete_view(self):
    #     response = self.client.post(reverse('employee_delete', kwargs={'pk': self.employee.pk}))
    #     self.assertEqual(response.status_code, 302)  # Check for redirect
    #     self.assertFalse(Employee.objects.filter(pk=self.employee.pk).exists())

# class EmployeeFormTests(TestCase):
#     def test_employee_form_valid(self):
#         form_data = {
#             'code': 'EMP003',
#             'name': 'Alice',
#             'birthday': '1992-02-02',
#             'remarks': 'Another employee'
#         }
#         form = EmployeeForm(data=form_data)
#         self.assertTrue(form.is_valid())
#
#     def test_employee_form_invalid(self):
#         form_data = {
#             'code': '',
#             'name': 'Alice',
#             'birthday': '1992-02-02',
#             'remarks': 'Another employee'
#         }
#         form = EmployeeForm(data=form_data)
#         self.assertFalse(form.is_valid())
#         self.assertIn('code', form.errors)


class BigDataTests(TestCase):
    def setUp(self):
        # Create a country and a city for testing
        self.country = Country.objects.create(name='United States')
        self.city = City.objects.create(name='New York', country=self.country)
        self.address_type = AddressType.objects.create(
            code='AT001',
            name='Work'
        )
        self.contact_type = ContactType.objects.create(
            code='CT001',
            name='Phone'
        )

    def test_large_data_insertion_and_view(self):
        # Create a large number of employees
        for i in range(1, 11):  # Adjust the range for more records
            employee = Employee.objects.create(
                code=f'EMP{i:03}',
                name=f'Employee {i}',
                birthday='1990-01-01',
                remarks=f'Test employee {i}'
            )
            # Address.objects.create(
            #     employee=employee,
            #     address_type=self.address_type,
            #     remarks=f'Address for employee {i}',
            #     country=self.country,
            #     city=self.city
            # )
            # Contact.objects.create(
            #     employee=employee,
            #     contact_type=self.contact_type,
            #     value=f'123-456-{i:03}')
            # Document.objects.create(
            #     employee=employee,
            #     file_description='Resume',
            #     remarks=f'Resume for employee {i}',
            #     file=f'file{i:03}.txt'
            # )

        # Check that 1000 employees were created
        self.assertEqual(Employee.objects.count(), 10)

        # Now check if the view can display these employees
        response = self.client.get(reverse('employee_list'))
        self.assertEqual(response.status_code, 200)
        # print(response.content.decode())
        # Check for the presence of some specific employee names in the response
        self.assertContains(response, 'Employee 5')  # Check for a specific employee in the list
        # self.assertContains(response, 'Employee 1000')  # Check for the last employee created
        # self.assertContains(response, 'Employee 1')  # Check for the first employee created

    def test_large_data_performance(self):
        import time
        start_time = time.time()

        # Simulate fetching all employees
        response = self.client.get(reverse('employee_list'))
        self.assertEqual(response.status_code, 200)

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'Time taken to load employee list: {elapsed_time:.2f} seconds')

class AddressTypeViewTests(TestCase):
    def setUp(self):
        self.address_type = AddressType.objects.create(
            code='AT002',
            name='Office'
        )

    # def test_address_type_list_view(self):
    #     response = self.client.get(reverse('address_type_list'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'employees/address_type_list.html')
    #     self.assertContains(response, 'Office')
