from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getRoutes(request):
    routes = [
    {
        'VIDEO_OBJECT': 'Represent a video',
        'format' : {
            'id': 'integer',
            'title': 'string',
            'description': 'string',
            'videofile': 'string (path to video)',
            'updated': 'date time',
            'created': 'date time'
        },
        'Endpoint: /videos/': {
            'Method': 'GET',
            'body': None,
            'description': 'Returns an array of [VIDEO_OBJECT]',
        },
        'Endpoint: /videos/create/' : {
            'Method': 'POST',
            'body': {
                'title': 'string',
                'description': 'string',
                'videofile': 'string (path to video)'
            },
            'description': 'Create and returns the data created OR a string with the error message',
        },
        'Endpoint: /videos/delete/': {
            'Method': 'DELETE',
            'body': {
                'id': 'integer'
            },
            'description': 'Deletes an existing video by id in url, where id = integer (retrieved in the VIDEO_OBJECT) AND return a string representing the status of the action',
        },
    },
    {
        'QUESTION_OBJECT': 'Represent a question',
        'format' : {
            'video_id': 'integer',
            'author': 'string',
            'question': 'string',
            'updated': 'date time',
            'created': 'date time'
        },
        'Endpoint: /questions/': {
            'Method': 'POST',
            'body': {
                'video_id': 'integer'
            },
            'description': 'Returns an array of [VIDEO_OBJECT] OR a string with the error message',
        },
        'Endpoint: /questions/create/' : {
            'Method': 'POST',
            'body': {
                'title': 'string (title of video)',
                'videofile': 'string (path to video)'
                },
            'description': 'Creates and returns a new video with data sent in Post request OR a string with the error message',
        },
        'Endpoint: /videos/delete/': {
            'Method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing video by id in url, where id = integer (retrieved in the VIDEO_OBJECT) AND returns a string with the status message of the request',
        },
    },
]
    return Response(routes)
