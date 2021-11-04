from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import VideoSerializer
from .models import Video

@api_view(['GET'])
def getRoutes(request):
    routes = [
    {
        'VIDEO_OBJECT': 'Represent a video',
        'format' : {
            
        }
    },
    {
        'Endpoint': '/videos',
        'Method': 'GET',
        'body': None,
        'description': 'Returns an array of [VIDEO_OBJECT]',
    },
    {
        'Endpoint': '/videos/create',
        'Method': 'POST',
        'body': {'title': ""},
        'description': 'Creates a new video with data sent in Post request',
    },
    {
        'Endpoint': '/videos/id/update',
        'Method': 'PUT',
        'body': {'title': ""},
        'description': 'Update an existing video',
    },
    {
        'Endpoint': '/videos/id/delete',
        'Method': 'DELETE',
        'body': None,
        'description': 'Deletes an existing video',
    },
]
    return Response(routes)

@api_view(['GET'])
def getVideos(request):
    videos = Video.objects.all()
    serializer = VideoSerializer(videos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createVideo(request):
    data = request.data
    video = Video.objects.create(title=data["title"], videofile=data["videofile"])
    serializer = VideoSerializer(video, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateVideo(request, pk):
    data = request.data
    video = Video.objects.get(id=pk)
    serializer = VideoSerializer(video, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteVideo(request, pk):
    video = Video.objects.get(id=pk)
    video.delete()
    return Response('Note was deleted')
