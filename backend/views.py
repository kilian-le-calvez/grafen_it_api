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
            'videofile': 'string (path to video)',
            'updated': 'date time',
            'created': 'date time'
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
        'body': {
            'title': 'string (title of video)',
            'videofile': 'string (path to video)'
            },
        'description': 'Creates a new video with data sent in Post request',
    },
    {
        'Endpoint': '/videos/id/update',
        'Method': 'PUT',
        'body': {'title': ''},
        'description': 'Update an existing video',
    },
    {
        'Endpoint': '/videos/id/delete',
        'Method': 'DELETE',
        'body': None,
        'description': 'Deletes an existing video by id in url, where id = integer (retrieved in the VIDEO_OBJECT)',
    },
]
    return Response(routes)
