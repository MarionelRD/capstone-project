from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.
#@authentication_classes([TokenAuthentication])
@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message":"This view is protected"})
