from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serialzers import AdvocateSerializer
from . models import Advocate
from django.db.models import Q

# Create your views here.
@api_view(['GET', 'POST'])
def advocates_list(request):
    
   if request.method == 'GET':
       query = request.GET.get('query')
       if query == None:
            query = ''
        
       advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
       seializer = AdvocateSerializer(advocates, many=True)
    
       return Response(seializer.data)
   
   # post request
   
   if request.method == "POST":
       advocate = Advocate.objects.create(
           username = request.data['username'],
           bio = request.data['bio']
       )
       
       serializer = AdvocateSerializer(advocate, many=False)
       return Response(serializer.data)
    

@api_view(['GET', 'PUT', "DELETE"])
def advocate_details(request, username):
    advocate = Advocate.objects.get(username=username)
    
    if request.method == 'GET':
        serializer = AdvocateSerializer(advocate)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        
        advocate.save()
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)
    
    if request.method == "DELETE":
        advocate.delete()
        return Response("user deleted.")
        
    