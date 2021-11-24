import socket

from django.http import JsonResponse
from django.utils.timezone import now

from .models import Visit


def home(request):
    # track new visits
    Visit.objects.create(
        user_browser=request.META.get('HTTP_USER_AGENT', 'unknown'),
        user_ip=request.META['REMOTE_ADDR'],
    )

    return JsonResponse({
        'message': 'hello world',
        'server_name': socket.gethostname(),
        'server_time': now(),
        'visit_counter': Visit.objects.count(),
    })
