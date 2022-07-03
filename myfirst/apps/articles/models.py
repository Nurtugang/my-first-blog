import datetime
from django.utils import timezone
from django.db import models

class User(models.Model):
	user_name = models.CharField('имя пользователя', max_length=200)
	user_date = models.DateTimeField('день рождения пользователя')

	def __str__(self):
		return self.user_name

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'
		
class Article(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	article_title = models.CharField('название статьи', max_length=200)
	article_text = models.TextField('текст статьи')
	article_date = models.DateTimeField('дата публикации')

	def __str__(self):
		return self.article_title

	def was_published_recently(self):
		return self.article_date >= (timezone.now() - datetime.timedelta(days=7))

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	comment_author = models.CharField('автор комментария', max_length=50)
	comment_text = models.CharField('текст комментария', max_length=200)

	def __str__(self):
		return self.comment_text

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'

