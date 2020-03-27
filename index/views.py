from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

from .models import Avatar, Project, Linkexchange, Hr, Seo

# Create your views here.


def index(request):

    staffs_list_origin = Avatar.objects.all()
    step = 5
    staffs_list = [staffs_list_origin[i:i + step] for i in range(0, len(staffs_list_origin), step)]

    projects = Project.objects.all()

    links_origin = Linkexchange.objects.all()
    links = [links_origin[i:i + step] for i in range(0, len(links_origin), step)]

    hrs = Hr.objects.all()

    seo = Seo.objects.order_by('desc')[0]

    context = {'staffs_list': staffs_list, 'projects': projects, 'links': links, 'hrs': hrs, 'seo': seo}

    return render(request, 'index/index.html', context)


def ajax_project(request,project_id):

    project = Project.objects.get(id=project_id)
    project_dict = {'id': project_id, 'name': project.name, 'author': project.author, 'desc': project.desc, 'link': project.link, 'image': project.image.url, 'bgimage': project.bgimage.url}

    return JsonResponse(project_dict)