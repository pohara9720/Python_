from upgrade.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse


#creating,updating,retrieving,deleting Retreiving 1 (since its detail not list)-- UPDATE MODEL

class UpdateModelDetailAPIView(View):
	#retrieve update delete --> obj
	def get(self,request,id,*args,**kwargs):
		obj = UpdateModel.objects.get(id = id)
		data = obj.serialize()
		return HttpResponse(data,content_type='application/json') 

	def post(self,request,*args,**kwargs):

		return HttpResponse({},content_type='application/json')

	def put(self,request,*args,**kwargs):

		return HttpResponse({},content_type='application/json') 

	def delete(self,request,*args,**kwargs):

		return HttpResponse({},content_type='application/json') 

class UpdateModelListAPIView(View):
	# List and create
	def get(self,request,id,*args,**kwargs):
		qs = UpdateModel.objects.all()
		data = qs.serialize()
		return HttpResponse(data,content_type='application/json')

	def post(self,request,*args,**kwargs):

		return HttpResponse({},content_type='application/json')