from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_joining = models.DateField()

    def __str__(self):
        return self.name

class VestingSchedule(models.Model):
    date = models.DateField()
    share_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    year_of_working = models.PositiveIntegerField()
    annual_salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Salary for {self.employee.name} in year {self.year_of_working}"

