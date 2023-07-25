# api/views.py

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Party
from .serializers import PartySerializer


@api_view(['GET', 'POST'])
def party_list_create_view(request):
    if request.method == 'GET':
        parties = Party.objects.all()
        serializer = PartySerializer(parties, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PartySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


def index(request):
    return render(request, 'index.html')
