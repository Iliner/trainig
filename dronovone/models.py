from django.db import models
# Create your models here.

class Category(models.Model):
	"""docstring for Category"""
	name = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return self.name


class Good(models.Model):
	name = models.CharField(max_length=30, unique=True, verbose_name = 'Название')
	in_stock = models.BooleanField(default=True, db_index=True, verbose_name='В наличии')
	description = models.TextField()
	price = models.IntegerField()
	category = models.ForeignKey(Category, null=True, blank=True)
	# CATEGORIES	= ((1, 'Метлы'), (2,'Веник'), (3,'Щетки'))
	# categor = models.IntegerField(choices=CATEGORIES, default=1, db_indes=True) 


	def get_is_stock(self):
		if self.in_stock:
			return "+"
		else:
			return ""

	def __str__(self):
		s = self.name
		if not self.in_stock:
			s = s + ' (нет в наличии)'
		return self.name

	def save(self, *args, **kwargs):
		super(Good, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		super(Good, self).delete(*args, **kwargs)

	class Meta:
		ordering = ['-price', 'name'] #Сортироваться по умолчанию по убыванию и по имени 
		unique_together = ('category', 'name', 'price') # Данная комбинация доджна быть уникальная для каждой записи 
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

	
class BlogArticle(models.Model):
	title = models.CharField(max_length=100, unique_for_month='pubdate')
	pubdate = models.DateField()
	update = models.DateField(auto_now=True)



