from rest_framework import serializers
from drf_api.models import Status

class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status
		fields = ['user','content','image']
		