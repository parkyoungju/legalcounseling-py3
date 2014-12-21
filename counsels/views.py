from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from counsels.models import Post


def index(request):
    posts = Post.objects.order_by('created')
    template = loader.get_template('counsels/index.html')
    context = RequestContext(request, {
        'posts': posts,
    })
    return HttpResponse(template.render(context))

def post(request):
    return HttpResponse("Post")
