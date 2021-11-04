import sys
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuestionSerializer
from .models import Question

@api_view(['GET'])
def getQuestions(request, video_id):
    questions = Question.objects.filter(video_id=video_id)
    if questions == []:
        return Response({})
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createQuestion(request, video_id):
    data = request.data
    question = Question.objects.create(question=data['question'], author=data['author'], video_id=video_id)
    serializer = QuestionSerializer(question, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteQuestion(request, video_id, id_question):
    question = Question.objects.get(id=id_question)
    question.delete()
    return Response('Question was deleted')
