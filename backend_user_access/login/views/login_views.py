from rest_framework import permissions, generics
from rest_framework.response import Response

from login.models.login_models import Users, People, Roles, Permissions
from login.serializers.login_serializers import (
    UsersSerializer, 
    PeopleSerializer,
    RolesSerializer,
    PermissionsSerializer,
    PeopleUpdateSerializer,
    UsersUpdateSerializer,

)
from rest_framework import status
from rest_framework.exceptions import ValidationError, NotFound, PermissionDenied


@staticmethod
def get_person_id(person_id):

    try:
        person = People.objects.get(person_id=person_id)
        return person
    except People.DoesNotExist:
        raise NotFound({'success': False, 'message': 'Person not found', 'data': None})
    

@staticmethod
def get_user_id(user_id):

    try:
        user = Users.objects.get(user_id=user_id)
        return user
    except Users.DoesNotExist:
        raise NotFound({'success': False, 'message': 'Person not found', 'data': None})
    

class PeopleCreateView(generics.CreateAPIView):
    serializer_class = PeopleSerializer

    def create_person(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':True, 'message': 'Person created successfully', 'data':serializer.data}, status=status.HTTP_201_CREATED)
        raise ValidationError({'success': False, 'message': 'Invalid data', 'errors': serializer.errors})

    def post(self, request, *args, **kwargs):
        return self.create_person(request)


class PeopleListView(generics.ListAPIView):
    serializer_class = PeopleSerializer

    def get(self, request, *args, **kwargs):
        people = People.objects.all()
        serializer = PeopleSerializer(people, many=True)
        return Response({'success':True, 'message': 'People list', 'data':serializer.data}, status=status.HTTP_200_OK)


class PeopleByIdView(generics.RetrieveAPIView):
    serializer_class = PeopleSerializer

    def get(self, request, person_id):

        person = get_person_id(person_id)
        serializador = self.serializer_class(person, many=False)

        return Response({'success':True, 'message':'Person found', 'data':serializador.data}, status=status.HTTP_200_OK)


class PeopleUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = PeopleUpdateSerializer

    def update_person(self, request, person_id):
        person = get_person_id(person_id)
        serializer = self.serializer_class(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        raise ValidationError({'success': False, 'message': 'Invalid data', 'errors': serializer.errors})
    
    def put(self, request, person_id, *args, **kwargs):

        data = self.update_person(request, person_id)
        return Response({'success':True, 'message':'Person updated successfully', 'data':data}, status=status.HTTP_200_OK)
    

class PeopleDeleteView(generics.DestroyAPIView):
    serializer_class = PeopleSerializer

    def delete(self, request, person_id):

        person = get_person_id(person_id)
        person.delete()
        return Response({'success':True, 'message':'Person deleted successfully', 'data':None}, status=status.HTTP_200_OK)


class UsersCreateView(generics.CreateAPIView):
    serializer_class = UsersSerializer

    def create_user(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':True, 'message': 'user created successfully', 'data':serializer.data}, status=status.HTTP_201_CREATED)
        raise ValidationError({'success': False, 'message': 'Invalid data', 'errors': serializer.errors})

    def post(self, request, *args, **kwargs):
        return self.create_user(request)


class UsersListView(generics.ListAPIView):
    serializer_class = UsersSerializer

    def get(self, request, *args, **kwargs):
        Users = Users.objects.all()
        serializer = UsersSerializer(Users, many=True)
        return Response({'success':True, 'message': 'Users list', 'data':serializer.data}, status=status.HTTP_200_OK)
    

class UsersByIdView(generics.RetrieveAPIView):
    serializer_class = UsersSerializer

    def get(self, request, user_id):

        user = get_user_id(user_id)
        serializador = self.serializer_class(user, many=False)

        return Response({'success':True, 'message':'user found', 'data':serializador.data}, status=status.HTTP_200_OK)


class UsersUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UsersUpdateSerializer

    def update_user(self, request, user_id):
        user = get_user_id(user_id)
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        raise ValidationError({'success': False, 'message': 'Invalid data', 'errors': serializer.errors})
    
    def put(self, request, user_id, *args, **kwargs):

        data = self.update_user(request, user_id)
        return Response({'success':True, 'message':'user updated successfully', 'data':data}, status=status.HTTP_200_OK)
    

class UsersDeleteView(generics.DestroyAPIView):
    serializer_class = UsersSerializer

    def delete(self, request, user_id):

        user = get_user_id(user_id)
        user.delete()
        return Response({'success':True, 'message':'user deleted successfully', 'data':None}, status=status.HTTP_200_OK)


