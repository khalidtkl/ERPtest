from django.shortcuts import render, redirect
from .forms import EmployeeForm, AddressFormSet, ContactFormSet, DocumentFormSet
from django.views.generic import ListView
from .models import Employee

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/employee_list.html'  # Specify your template here
    context_object_name = 'employees'  # Name the list to use in the template
    paginate_by = 10
    ordering = ['name']


def employee_create(request):
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST)
        address_formset = AddressFormSet(request.POST)
        contact_formset = ContactFormSet(request.POST)
        document_formset = DocumentFormSet(request.POST, request.FILES)
        if employee_form.is_valid() and address_formset.is_valid() and contact_formset.is_valid() and document_formset.is_valid():
            employee = employee_form.save()  # Save the employee
            address_formset.instance = employee
            contact_formset.instance = employee
            document_formset.instance = employee
            addresses = address_formset.save(commit=False)
            for address in addresses:
                address.employee = employee  # Link the address to the employee
                address.save()  # Save related addresses
            contacts = contact_formset.save(commit=False)
            for contact in contacts:
                contact.employee = employee  # Link the address to the employee
                contact.save()
            documents = document_formset.save(commit=False)
            for document in documents:
                document.employee = employee  # Link the address to the employee
                document.save()  # Save related addresses
        return redirect('employee_list')# Redirect to the employee list after saving
    else:
        employee_form = EmployeeForm()
        address_formset = AddressFormSet(instance=None)
        contact_formset = ContactFormSet(instance=None)
        document_formset = DocumentFormSet(instance=None)

    return render(request, 'employees/employee_form.html', {
        'employee_form': employee_form,
        'address_formset': address_formset,
        'contact_formset': contact_formset,
        'document_formset': document_formset
    })


def employee_update(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, instance=employee)
        address_formset = AddressFormSet(request.POST, instance=employee)
        contact_formset = ContactFormSet(request.POST, instance=employee)
        document_formset = DocumentFormSet(request.POST, request.FILES, instance=employee)
        valid_employee = employee_form.is_valid()
        valid_address = address_formset.is_valid()
        valid_contact = contact_formset.is_valid()
        valid_document = document_formset.is_valid()
        if employee_form.is_valid() and address_formset.is_valid() and contact_formset.is_valid() and document_formset.is_valid():
            employee = employee_form.save()
            address_formset.save()
            contact_formset.save()
            document_formset.save()
            return redirect('employee_list')
    else:
        employee_form = EmployeeForm(instance=employee)
        address_formset = AddressFormSet(instance=employee)
        contact_formset = ContactFormSet(instance=employee)
        document_formset = DocumentFormSet(instance=employee)

    return render(request, 'employees/employee_form.html', {
        'employee_form': employee_form,
        'address_formset': address_formset,
        'contact_formset': contact_formset,
        'document_formset': document_formset
    })