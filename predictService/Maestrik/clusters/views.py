# Create your views here.
import os
import threading

from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from maestrik.serializers import *
#from elecciones_2019.serializers import *
from .process.calculateClusters.clusterHelper import ClusterHelper
from .process.recomendationEngines.recomendationHelper import RecomendationHelper

# CLASS cluster =================================================
cluserHelper = ClusterHelper()
recomendationHelper = RecomendationHelper()

def __init__(self,*args,**kwargs):
	super(threading.Thread,self).__init__(*args,**kwargs)
	self._stop = threading.Event()


# LIST ===========================================================
@api_view(['GET'])
def index(request):

	if request.method == 'GET':
		return Response({'message': 'Api process ok'})

@api_view(['GET','POST'])
@authentication_classes([])
@permission_classes([])
def clusterUser(request):
	if request.method == 'GET':
		return Response({'message': 'Api process ok'})
	else:
		serializer = UserSerializer(data = request.data)
		if serializer.is_valid():
			return JsonResponse(cluserHelper.calculateCluster(serializer.data))
		else:
			return JsonResponse({'status':'failed'})


@api_view(['GET','POST'])
@authentication_classes([])
@permission_classes([])
def upSellingProduct(request):
	if request.method == 'GET':
		return Response({'message': 'Api process ok'})
	else:
		serializer = UpSellingSerializer(data = request.data)
		if serializer.is_valid():
			return JsonResponse(recomendationHelper.getUpsellingRecomendation(serializer.data))
		else:
			return JsonResponse({'status':'failed'})