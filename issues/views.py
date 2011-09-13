# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from issues.models import Issue, Status, Project

def index(request):
    issues = Issue.objects.all()
    return HttpResponse(issues)


def new_issue(request):
    projects = Project.objects.all().order_by('-order','name')
    return render_to_response('new_ticket.html', {'projects': projects })
    
    