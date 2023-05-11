from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Person
from .serializer import PersonSerializer
#from django.http import HttpResponse

def index(request):
    allPeople = Person.objects.all()
    context = {'allPeople':allPeople}
    return render(request, 'people/index.html', context=context, status=200)

@api_view(['POST'])
def people_create_view(request, *args, **kwargs):
	serializer = PersonSerializer(data=request.data)
	if serializer.is_valid(raise_exception=True):
		serializer.save()
		return Response(serializer.data, status=201)
	return Response({}, status=400)

@api_view(['GET'])
def people_list_view(request, *args, **kwargs):
	queryset = Person.objects.all()
	serializer = PersonSerializer(queryset, many=True)
	return Response(serializer.data, status=200)

@api_view(['GET'])
def people_detail_view(request, person_id, *args, **kwargs):
	try:
		person_obj = Person.objects.get(id=person_id)
	except:
		return Response({"message" : "Not Found"}, status=404)
	serializer = PersonSerializer(person_obj)	
	return Response(serializer.data, status=200)
