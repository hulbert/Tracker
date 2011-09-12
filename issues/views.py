# Create your views here.

from django.http import HttpResponse
from issues.models import Issue, Status

def index(request):
    issues = Issue.objects.all()
    return HttpResponse(issues)
