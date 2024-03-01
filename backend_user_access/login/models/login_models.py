from django.db import models

# Create your models here.

class People(models.Model):
    person_id = models.AutoField(primary_key=True, db_column='person_id')
    first_name = models.CharField(max_length=100, db_column='first_name')
    second_name = models.CharField(max_length=100, blank=True, null=True, db_column='second_name')
    first_last_name = models.CharField(max_length=100, db_column='first_last_name')
    second_last_name = models.CharField(max_length=100, blank=True, null=True, db_column='second_last_name')
    date_of_birth = models.DateField(db_column='date_of_birth')
    gender = models.CharField(max_length=1, blank=True, null=True, db_column='gender')
    address = models.CharField(max_length=100, db_column='address')
    city = models.CharField(max_length=100, db_column='city')
    state = models.CharField(max_length=100, db_column='state')
    country = models.CharField(max_length=100, db_column='country')
    phone_number = models.CharField(max_length=100, db_column='phone_number')
    email = models.EmailField(db_column='email')

    def __str__(self):
        return self.first_name + ' ' + self.first_last_name
    
    class Meta:
        db_table = 'People'
        verbose_name = 'Person'
        verbose_name_plural = 'People'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True, db_column='user_id')
    username = models.CharField(max_length=100, db_column='username')
    password_hash = models.CharField(max_length=255, db_column='password_hash')
    is_locked = models.BooleanField(default=False, db_column='is_locked')
    is_active = models.BooleanField(default=False, db_column='is_active')
    person_id = models.ForeignKey(People, on_delete=models.CASCADE, db_column='person_id')

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'Users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Roles(models.Model):
    role_id = models.AutoField(primary_key=True, db_column='role_id')
    role_name = models.CharField(max_length=100, db_column='role_name')
    role_description = models.CharField(max_length=255, db_column='role_description')

    def __str__(self):
        return self.role_name
    
    class Meta:
        db_table = 'Roles'
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'


class UserRoles(models.Model):
    user_role_id = models.AutoField(primary_key=True, db_column='user_role_id')
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='user_id')
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE, db_column='role_id')

    class Meta:
        db_table = 'UserRoles'
        verbose_name = 'User Role'
        verbose_name_plural = 'User Roles'


class Permissions(models.Model):
    permission_cod = models.CharField(max_length=3, primary_key=True, db_column='permission_cod')
    permission_name = models.CharField(max_length=100, db_column='permission_name')

    def __str__(self):
        return self.permission_name
    
    class Meta:
        db_table = 'Permissions'
        verbose_name = 'Permission'
        verbose_name_plural = 'Permissions'


class RolePermissions(models.Model):
    role_permission_id = models.AutoField(primary_key=True, db_column='role_permission_id')
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE, db_column='role_id')
    permission_id = models.ForeignKey(Permissions, on_delete=models.CASCADE, db_column='permission_id')

    class Meta:
        db_table = 'RolePermissions'
        verbose_name = 'Role Permission'
        verbose_name_plural = 'Role Permissions'


class AuditLogs(models.Model):
    audit_log_id = models.AutoField(primary_key=True, db_column='audit_log_id')
    action_type = models.CharField(max_length=255, db_column='action_type')
    action_timestamp = models.DateTimeField(auto_now_add=True, db_column='action_date')
    additional_details = models.CharField(max_length=255, db_column='additional_details')
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='user_id')

    class Meta:
        db_table = 'AuditLogs'
        verbose_name = 'Audit Log'
        verbose_name_plural = 'Audit Logs'