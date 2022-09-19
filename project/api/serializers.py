from rest_framework import serializers
from project.models import *

#ModelSerializer
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'date_joined']


class DepartmentSerializer(serializers.ModelSerializer):
    emp_name = EmployeeSerializer(read_only=True)
    class Meta:
        model = Department
        fields = ['department','emp_name']


class ProjectSerializer(serializers.ModelSerializer):
    manager_details = serializers.SerializerMethodField('get_all_about_manager')
    employee = DepartmentSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'start_date', 'end_date', 'manager_details', 'employee']

    def get_all_about_manager(self, Project):
        id = Project.manager.pk
        name = Project.manager.name
        email = Project.manager.email
        manager = {'id':id, 'Manager Name':name, 'Email':email}
        return manager





