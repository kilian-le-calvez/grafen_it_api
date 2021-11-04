from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuestionSerializer
from .models import Question

@api_view(['GET'])
def getQuestions(request, id_video):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createQuestion(request, id_video):
    data = request.data
    question = Question.objects.create(question=data['question'], author=data['author'])
    serializer = QuestionSerializer(question, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteQuestion(request, id_video, id_question):
    question = Question.objects.get(id=id_question)
    question.delete()
    return Response('Question was deleted')
