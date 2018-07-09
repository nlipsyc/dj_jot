from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission
from django.contrib.auth.models import User


# We need to define some custom permissions here
class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_authenticated
        elif view.action == 'create':
            return not request.user.is_authenticated
        elif view.action == 'retrieve':
            return True 
        else:
            return False
    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return obj == request.user
        else:
            return False

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'password')
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)

