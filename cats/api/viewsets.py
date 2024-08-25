from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from cats.models import Cat, Fact
from cats.api.serializers import CatSerializer, FactSerializer
import requests
import json


class CatViewSet(ModelViewSet):
    queryset=Cat.objects.all()
    serializer_class= CatSerializer


    def create(self, request, *args, **kwargs):

        savedCat = Cat.objects.create(
            breed=request.data.get('breed'),
            coat=request.data.get('coat')
        )

        requisicao = requests.get("https://catfact.ninja/fact?max_length=100").json()


        savedFact = Fact.objects.create(
            cat=savedCat,
            fact=requisicao['fact']
        )

        return Response({"Fact and Cat successfully generated"}, status.HTTP_201_CREATED)

class FactViewSet(ModelViewSet):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer

