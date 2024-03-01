from rest_framework import serializers
from login.models.login_models import Users, Roles, UserRoles, Permissions, RolePermissions, AuditLogs, People

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'


class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = '__all__'


class AuditLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLogs
        fields = '__all__'


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'


class PeopleUpdateSerializer(serializers.ModelSerializer):
     class Meta:
        model = People
        fields = ['first_name', 
                  'second_name',
                  'first_last_name',
                  'second_last_name',
                  'email',
                  'phone_number',
                  'address',
                  'city',
                  'state',
                  'country',
                  'date_of_birth']
        
class UsersUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'password', 'email', 'is_active', 'is_superuser', 'is_staff']


