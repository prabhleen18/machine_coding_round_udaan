from django.shortcuts import render
from .models import User, Symptoms, Admin,CovidResult
from .serializers import UserSerializer, SymptomsSerializer, AdminSerializer, CovidResultSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    def create(self, request):
        request_data = request.data
        serializer = UserSerializer(data = request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'userId': serializer.data.get('id')}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SymptomsViewSet(viewsets.ModelViewSet):
    def create(self, request):
        request_data = request.data
        response_data = dict()

        valid_data = self.validate_request_body(request_data)
        if valid_data is None:
            symptoms = request_data.get('symptoms')
            travel_history = request_data.get('travelHistory')
            contact_with_covid_patient = request_data.get('contactWithCovidPatient')
            # calculating the risk factor
            if len(symptoms) == 0 and not travel_history and not contact_with_covid_patient:
                response_data['riskPercentage'] = 5

            if len(symptoms) == 1 and (travel_history or contact_with_covid_patient):
                response_data['riskPercentage'] = 50

            if len(symptoms) == 2 and (travel_history or contact_with_covid_patient):
                response_data['riskPercentage'] = 75

            if len(symptoms) > 2 and (travel_history or contact_with_covid_patient):
                response_data['riskPercentage'] = 95

            return Response(response_data, status=status.HTTP_200_OK)

        else:
            return Response(valid_data, status=status.HTTP_400_BAD_REQUEST)

    def validate_request_body(self, request_body):
        errors = {}
        required_data_items = ['userId', 'symptoms', 'travelHistory', 'contactWithCovidPatient']

        # checking for missing request body fields
        for item in required_data_items:
            if not request_body.get(item):
                errors[item] = 'Field Required' + ' ' + item

        if len(errors) > 0:
            return errors

        # checking for invalid data
        # userid
        try:
            user_instance = User.objects.get(id=request_body.get('userId'))
            if not isinstance(request_body.get('symptoms'), list):
                errors['symptoms'] = 'Field Invalid  - symptoms'

            if not isinstance(request_body['travelHistory'], bool):
                errors['travelHistory'] = 'Field Invalid  - travelHistory'

            if not isinstance(request_body['contactWithCovidPatient'], bool):
                errors['contactWithCovidPatient'] = 'Field Invalid  - contactWithCovidPatient'

        except:
            errors['userId'] = 'Field Invalid  - userId'

        if len(errors) > 0:
            return errors
        else:
            return None

class AdminViewSet(viewsets.ModelViewSet):
    def create(self, request):
        request_data = request.data
        serializer = AdminSerializer(data = request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'adminId': serializer.data.get('id')}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CovidResultViewSet(viewsets.ModelViewSet):
    def create(self, request):
        request_data = request.data
        serializer = CovidResultSerializer(data=request_data)
        if serializer.is_valid():
            return Response({'updated': True}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)