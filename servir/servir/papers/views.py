from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from .models import Paper
from .serializer import PaperSerializer
from django.http import HttpResponse

def index(request):
    allPapers = Paper.objects.all()
    context = {'allPapers':allPapers}
    return render(request, 'papers/index.html', context=context, status=200)


@api_view(['POST'])
def paper_create_view(request, *args, **kwargs):
    serializer = PaperSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)
    return Response({}, status=400)

@api_view(['GET'])
def paper_list_view(request, *args, **kwargs):
	queryset = Paper.objects.all()
	serializer = PaperSerializer(queryset, many=True)
	return Response(serializer.data, status=200)

@api_view(['GET'])
def paper_detail_view(request, paper_id, *args, **kwargs):
	try:
		paper_obj = Paper.objects.get(id=paper_id)
	except:
		return Response({"message" : "Not Found"}, status=404)
	serializer = PaperSerializer(paper_obj)
	return Response(serializer.data, status=200)

@api_view(['DELETE'])
def paper_delete(request, paper_id, *args, **kwargs):
    paper1 = Paper.objects.filter(id=paper_id)
    paper1.delete()
    return Response({}, status=204)
