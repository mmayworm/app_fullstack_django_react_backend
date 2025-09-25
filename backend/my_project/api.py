from rest_framework import routers, viewsets, serializers

from django.contrib.auth.models import User
from my_app.api import router as my_app_router

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.registry.extend(my_app_router.registry)  




   
    
