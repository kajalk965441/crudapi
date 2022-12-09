from rest_framework import serializers
from .models import studentlist

class studentdataserializers(serializers.ModelSerializer):
     class Meta:
          model = studentlist
          fields = '__all__'