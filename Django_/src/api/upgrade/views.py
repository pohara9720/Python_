from django.http import JsonResponse,HttpResponse
from api.mixins import JsonResponseMixin
from django.shortcuts import render
from django.views.generic import View
from django.core.serializers import serialize
from .models import Update

# Create your views here.

#def detail_view(request):
	#return render() #return JSON data
	#return render is the same as return HttpResponse(get_template().render({}))

def json_example_view(request):
	data = {
		"count":1000,
		"content": "EXAMPLE"
	}
	return JsonResponse(data)


class JsonCBV(View):
	def get(self,request,*args,**kwargs):
		data = {
			"count":2000,
			"content": "CBV"
		}
		return JsonResponse(data)


class JsonCBV2(JsonResponseMixin,View):
	def get(self,request,*args,**kwargs):
		data = {
			"count":3000,
			"content": "CBV2"
		}
		return self.render_to_json(data)


class SerializedDetailView(View):
	def get(self,request,*args,**kwargs):
		obj = Update.objects.get(id=1)

		## Without serializer from model you can do it this way
		# data = serialize('json',[obj]) #can pass in fields parameter as well 
		# print(obj)
		# return HttpResponse(data,content_type='application/json')

		## With serializer being used in the model you can do it this way
		data = obj.serialize()
		return HttpResponse(data,content_type='application/json')

class SerializedListView(View):
	def get(self,request,*args,**kwargs):
		## Without serializer from model you can do it this way
		# qs = Update.objects.all()
		# data = serialize('json',qs,fields=('user','content'))
		# # return JsonResponse(data) #this errors 
		# return HttpResponse(data,content_type='application/json')

		## With serializer being used in the model you can do it this way
		data = Update.objects.all().serialize()
		return HttpResponse(data,content_type='application/json')

