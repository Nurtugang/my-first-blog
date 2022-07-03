from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Article, Comment, User
from django.urls import reverse

def index(request):
	latest_articles_list = Article.objects.order_by('-article_date')[:5]
	return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id):
	try:
		a = Article.objects.get(id=article_id)
	except:
		raise Http404('Статья не найдена')

	#latest_comment_list = a.comment_set.order_by(-id)[:10]	
	latest_comment_list = Comment.objects.filter(article_id=article_id).order_by('-id')


	return render(request, 'articles/detail.html', {'article': a, 'latest_comment_list':latest_comment_list})

def leave_comment(request, article_id):
	try:
		a = Article.objects.get(id=article_id)
	except:
		raise Http404('Статья не найдена')

	Comment(article_id=article_id, 
						user_id=User.objects.get(user_name=request.POST['name']).id, 
						comment_author = request.POST['name'], 
						comment_text=request.POST['text']).save()

	return HttpResponseRedirect(reverse('articles:detail', args=(a.id, ) )) 