from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import *
from django.core.paginator import Paginator, InvalidPage
# Create your views here.

# def index(request, id):
# 	cats = Category.objects.all().order_by('name')
# 	if id == None:
# 		cat = Category.objects.first()
# 	else:
# 		try: 
# 			cat = Category.objects.get(pk=id)
# 		except Category.DoesNotExist:
# 			raise Http404
# 	goods = Good.objects.filter(category = cat).order_by('name')
# 	s = "Категория: " + cat.name + "<br><br>"
# 	for good in goods:
# 		s = s + "(" + str(good.pk) + ") " + good.name + "<br>"
# 	return render(request, 'dronovone/index.html', {"category": cat, 'cats': cats, 'goods': goods})

# def index(request, id):
# 	try:
# 		page_num = request.GET['page']
# 	except KeyError:
# 		page_num = 1
# 	cats = Category.objects.all().order_by('name')
# 	if id == None:
# 		cat = Category.objects.first()
# 	else:
# 		cat = Category.objects.get(pk=id)
# 	paginator = Paginator(Good.objects.filter(category=cat).order_by('name'), 1)
# 	try:
# 		goods = paginator.page(page_num)
# 	except InvalidPage:
# 		goods = paginator.page(1)
# 	return render(request, 'dronovone/index.html', {"category": cat, 'cats': cats, 'goods': goods})




# def good(request, id):
# 	try:
# 		page_num = request.GET['page']
# 	except KeyError:
# 		page_num = 1
# 	cats = Category.objects.all().order_by('name')
# 	try:
# 		good = Good.objects.get(pk=id)
# 	except Good.DoesNotExist:
# 		raise Http404
# 	#good = Good.objects.get(pk=id)		
# 	return render(request, 'dronovone/good.html', {'good': good, 'cats': cats, 'pn': page_num})

# def categories(request):
# 	categories = Category.objects.all()
# 	list_categories = "<h1>Cписок категорий:</h1>"
# 	for category in categories:
# 		list_categories  += "<h2>№{} {}".format(category.pk, category.name)
# 	return HttpResponse(list_categories)