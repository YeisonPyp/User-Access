from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from login.views import login_views as views

urlpatterns = [

    # People
    path('people/create/', views.PeopleCreateView.as_view(), name='people-create'),
    path('people/list/', views.PeopleListView.as_view(), name='people-list'),
    path('people/get/<int:person_id>/', views.PeopleByIdView.as_view(), name='people-by-id'),
    path('people/update/<int:person_id>/', views.PeopleUpdateView.as_view(), name='people-update'),
    path('people/delete/<int:person_id>/', views.PeopleDeleteView.as_view(), name='people-delete'),

    # Users
    path('users/create/', views.UsersCreateView.as_view(), name='users-create'),
    path('users/list/', views.UsersListView.as_view(), name='users-list'),
    path('users/get/<int:user_id>/', views.UsersByIdView.as_view(), name='users-by-id'),
    path('users/update/<int:user_id>/', views.UsersUpdateView.as_view(), name='users-update'),
    path('users/delete/<int:user_id>/', views.UsersDeleteView.as_view(), name='users-delete'),

    # # Roles
    # path('roles/create/', views.RolesCreateView.as_view(), name='roles-create'),
    # path('roles/list/', views.RolesListView.as_view(), name='roles-list'),
    # path('roles/get/<int:role_id>/', views.RolesByIdView.as_view(), name='roles-by-id'),
    # path('roles/update/<int:role_id>/', views.RolesUpdateView.as_view(), name='roles-update'),
    # path('roles/delete/<int:role_id>/', views.RolesDeleteView.as_view(), name='roles-delete'),

    # # Permissions
    # path('permissions/create/', views.PermissionsCreateView.as_view(), name='permissions-create'),
    # path('permissions/list/', views.PermissionsListView.as_view(), name='permissions-list'),
    # path('permissions/get/<int:permission_id>/', views.PermissionsByIdView.as_view(), name='permissions-by-id'),
    # path('permissions/update/<int:permission_id>/', views.PermissionsUpdateView.as_view(), name='permissions-update'),
    # path('permissions/delete/<int:permission_id>/', views.PermissionsDeleteView.as_view(), name='permissions-delete'),




]

