from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ListGrandGoalSerializer, DetailGrantGoalSerializer


from core.models import GrantGoal

# Create your views here.

######### API GRANT GOAL

####Create


##### RETRIEVE

########## LIST
class ListGrantGoalAPIView(APIView):
    
    def get(self, request):
        queryset = GrantGoal.objects.all()
        data = ListGrandGoalSerializer(queryset, many=True).data
        return Response (data)

# DETAIL
class DetailGrantGoalAPIView(APIView):
    def get(self, request, pk):
        queryset = GrantGoal.objects.get(pk=pk)
        data = DetailGrantGoalSerializer(queryset, many=False).data
        return Response (data)

#UPDATE

# DELTE