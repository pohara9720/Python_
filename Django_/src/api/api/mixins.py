from django.http import JsonResponse

class JsonResponseMixin(object):
	def render_to_json(self,context,**response_kwargs):
		return JsonResponse(self.get_data(context),**response_kwargs)

	#Need this to ensure that context can be turned into json
	def get_data(self,context):
		return context