from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import NoteSerializer
from .models import Note
# Create your views here.


@api_view(['GET'])
def getroute(request):
    getrout = [{
        'Endpoint': '/notes/',
        'method': 'Get',
        'body': None,
        'description': 'this is description of some jason resopnse'
    },
        {
        'Endpoint': '/notes/',
        'method': 'Get',
        'body': None,
        'description': 'this is description of some jason resopnse'
    }, ]
    return Response(getrout)


@api_view(['GET'])
def getnotes(request):
    notes = Note.objects.all()
    serializ = NoteSerializer(notes, many=True)

    return Response(serializ.data)


@api_view(['GET'])
def getnote(request, pk):
    note = Note.objects.get(id=pk)
    serializ = NoteSerializer(note, many=False)

    return Response(serializ.data)


@api_view(['POST'])
def createnote(request):
    data = request.data

    note = Note.objects.create(
        body=data["body"]
    )
    serializ = NoteSerializer(note, many=False)
    return Response(serializ.data)


@api_view(['PUT'])
def editnote(request, pk):
    note = Note.objects.get(id=pk)
    serializ = NoteSerializer(note, data=request.data)
    if serializ.is_valid():
        serializ.save()

    return Response(serializ.data)


@api_view(['DELETE'])
def deletenote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("deleted very well")
