import sys
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuestionSerializer
from .models import Question

@api_view(['POST'])
def getQuestions(request):
    data = request.data

    questions = Question.objects.filter(video_id=data['video_id'])
    if len(questions) > 0:
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
    else: 
        return Response({'status': 'No comments attached to this video id'})

@api_view(['POST'])
def createQuestion(request):
    data = request.data
    if data['question'] and data['author'] and data['video_id']:
        question = Question.objects.create(question=data['question'] , author=data['author'], video_id=data['video_id'])
        serializer = QuestionSerializer(question, many=False)
        return Response(serializer.data)
    else:
        return Response({})

@api_view(['POST'])
def deleteQuestion(request):
    data = request.data
    if data['id']:
        question = Question.objects.get(id=data['id'])
        question.delete()
        return Response({'status': 'Question was deleted or does not exists but the request is valid'})
    else:
        return Response({'status': 'Question id is unvalid or corrupted'})