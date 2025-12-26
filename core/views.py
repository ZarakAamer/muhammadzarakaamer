from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone

from blog.models import Post
from projects.models import Project
from .forms import ContactForm
from .models import ContactMessage


def index(request):
    latest_projects = Project.objects.filter(is_published=True).order_by('-updated_at')[:4]
    latest_posts = Post.objects.filter(is_published=True).order_by('-published_at')[:4]
    context = {
        'latest_projects': latest_projects,
        'latest_posts': latest_posts,
        'site_name': getattr(settings, 'SITE_NAME', 'My Site'),
        'profile_name': getattr(settings, 'PROFILE_NAME', 'Your Name'),
    }
    return render(request, 'core/index.html', context)


def about(request):
    return render(request, 'core/about.html', {'site_name': getattr(settings, 'SITE_NAME', 'My Site')})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ContactMessage.objects.create(**data)

            # Email if configured
            if settings.CONTACT_TO_EMAIL and settings.EMAIL_HOST:
                subject = f"Website contact from {data['name']}"
                body = f"From: {data['name']} <{data['email']}>\n\n{data['message']}"
                send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_TO_EMAIL], fail_silently=True)

            messages.success(request, 'Thanks! Your message has been sent.')
            return redirect(reverse('core:contact'))
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form, 'site_name': getattr(settings, 'SITE_NAME', 'My Site')})


def robots_txt(request):
    content = "\n".join([
        "User-agent: *",
        "Allow: /",
        f"Sitemap: {request.build_absolute_uri('/sitemap.xml')}",
    ]) + "\n"
    return HttpResponse(content, content_type='text/plain')


def sitemap_xml(request):
    # Basic sitemap without django.contrib.sitemaps
    pages = [
        ('core:index', {}),
        ('core:about', {}),
        ('core:contact', {}),
        ('projects:list', {}),
        ('blog:list', {}),
    ]

    project_urls = [request.build_absolute_uri(p.get_absolute_url()) for p in Project.objects.filter(is_published=True)]
    post_urls = [request.build_absolute_uri(p.get_absolute_url()) for p in Post.objects.filter(is_published=True)]

    urls = [request.build_absolute_uri(reverse(name, kwargs=kwargs)) for name, kwargs in pages] + project_urls + post_urls

    lastmod = timezone.now().date().isoformat()

    xml_items = "\n".join([
        f"  <url><loc>{u}</loc><lastmod>{lastmod}</lastmod></url>" for u in urls
    ])

    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{items}
</urlset>
""".format(items=xml_items)

    return HttpResponse(xml, content_type='application/xml')
