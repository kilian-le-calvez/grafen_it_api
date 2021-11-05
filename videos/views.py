import sys
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import VideoSerializer
from .models import Video
sys.path.append("..")
from questions.models import Question

@api_view(['GET'])
def getVideos(request):
    videos = Video.objects.all()
    serializer = VideoSerializer(videos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createVideo(request):
    data = request.data
    
    if data['title'] and data['description'] and data['file']:
        video = Video.objects.create(title=data['title'], description=data['description'], file=data['file'])
        serializer = VideoSerializer(video, many=False)
        return Response(serializer.data)
    else:
        return Response("One of the fields is missing or corrupted")

@api_view(['DELETE'])
def deleteVideo(request):
    data = request.data
    if (data['id']):
        questions = Question.objects.filter(video_id=data['id'])
        questions.delete()
        video = Video.objects.get(id=data['id'])
        video.delete()
        return Response('Video was deleted or does not exists but the request is valid')
    else:
        return Response('Incomplete request')