from rest_framework import serializers, routers, viewsets

from .models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['email_id', 'name', 'profissao','atuacao_especialidade',
                  'breve_descricao_apresentacao','servicos_oferecidos','watzapp','instagram','facebook','email','localizacao']

class PersonViewSet(viewsets.ModelViewSet):
        queryset = Person.objects.all()   #Seleciona
        serializer_class = PersonSerializer

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet, basename='my_app')