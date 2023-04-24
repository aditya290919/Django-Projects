from django.shortcuts import render
from .models import Product, Order
from django.views.generic import ListView
from django.core.paginator import Paginator
# Create your views here.

def index(request):
	product_objects = Product.objects.all()
	product_name = request.GET.get('item_name')
	if product_name !='' and product_name is not None:
		product_objects = product_objects.filter(title__icontains=product_name)

	paginator=Paginator(product_objects,4)
	page = request.GET.get('page')
	product_objects = paginator.get_page(page)

	return render(request,'shop/index.html',{'product_objects':product_objects})

class ClassIndex(ListView):
	model = Product
	template_name = 'shop/index.html'
	context_object_name = 'product_objects'


def detail(request, id):
	product_object = Product.objects.get(id=id)
	return render(request,'shop/detail.html',{'product_object':product_object})

def checkout(request):
	if request.method == "POST":
		items = request.POST.get('items',"")
		name = request.POST.get('name',"")
		email = request.POST.get('email',"")
		address = request.POST.get('address',"")
		city = request.POST.get('city',"")
		state = request.POST.get('state',"")
		zipcode = request.POST.get('zipcode',"")
		total = request.POST.get('total',"")
		order = Order(items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,total=total)
		order.save()

	return render(request,'shop/checkout.html')