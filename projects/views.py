from django.shortcuts import render, get_object_or_404

from .models import Project


def project_list(request):
    projects = Project.objects.filter(is_published=True).order_by('-is_featured', '-updated_at')
    return render(request, 'projects/projects_list.html', {'projects': projects})


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, is_published=True)
    return render(request, 'projects/project_detail.html', {'project': project})
