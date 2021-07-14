from rest_framework import serializers
from .models import User, Symptoms, Admin, CovidResult

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SymptomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptoms
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class CovidResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidResult
        fields = '__all__'