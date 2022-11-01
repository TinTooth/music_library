from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Song
from .serializer import SongSerializer
# Create your views here.

@api_view(['GET','POST'])
def songs_list(request):
    if request.method == 'GET':
        query_set = Song.objects.all()
        serializer = SongSerializer(query_set,many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = SongSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def song_detail(request,pk):
    query = get_object_or_404(Song,pk = pk)

    if request.method == 'GET':
        serializer = SongSerializer(query)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SongSerializer(query,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'DELETE':
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)