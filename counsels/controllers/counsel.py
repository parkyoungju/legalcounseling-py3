from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from counsels.models import Post
from django.shortcuts import render


def index(request):
    posts = Post.objects.order_by('created')
    context = {'posts': posts}

    return render(request, 'counsels/index.html', context)


def post(request):
    category_name = {
        'COUNSELING': u'간편 법률 상담',
        'CERTIFICATION': u'내용증명, 고소장 작성',
        'CAR_ACCIDENT': u'교통사고 과실 비율 추정',
        'REQUEST_ADVICE': u'법률 상담 의뢰',
    }

    category = request.GET.get('category', 'COUNSELING')
    context = {'category_name': category_name[category]}

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        user = request.user
        post = Post.objects.create(user=user, title=title, content=content, category=category)
        post.save()

    return render(request, 'counsels/post.html', context)

