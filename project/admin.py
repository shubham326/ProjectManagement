from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from project.models import Employee, Department, Project

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    exclude = ['is_admin', 'is_staff', 'is_superuser', 'is_active']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'department', 'emp_name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'project_name', 'start_date', 'end_date', 'manager', 'get_employee']