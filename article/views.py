from django.shortcuts import render,get_object_or_404,redirect
from  .models import  Article
from .forms import ArticleForm
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import  login_required
# from django.template import loader
# Create your views here.
# articles'list
def article_list(request):
    posts = Article.objects.all()
    pageinator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = pageinator.page(page)
    except PageNotAnInteger:
        posts = pageinator.page(1)
    except EmptyPage:
        posts = pageinator(pageinator.num_pages)

    return render(request,'article/article_list.html',{'posts':posts})


# article's detail
def article_detail(request,pk):
    post = get_object_or_404(Article,pk = pk)
    return render(request,'article/article_detail.html',{'post':post})


@login_required
def article_new(request):
    if request.method =='POST':
        form=ArticleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.save()
            return  redirect('article.views.article_detail',pk = post.pk)
    else:
        form = ArticleForm()
    return render(request,'article/article_edit.html',{'form':form})

def article_edit(request, pk):
    post = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('article.views.article_detail', pk=post.pk)
    else:
        form = ArticleForm(instance=post)
    return render(request, 'article/article_edit.html', {'form': form})

def post_draft_list(request):
    posts = Article.objects.filter(published_date__isnull=True).order_by('-create_date')
    return render(request, 'article/post_draft_list.html', {'posts': posts})

def article_publish(request, pk):
    post = get_object_or_404(Article,pk = pk)
    post.publish()
    return redirect('article.views.article_detail',pk=pk)

def article_remove(request,pk):
    post = get_object_or_404(Article,pk=pk)
    post.delete()
    return  redirect('article.views.article_list')