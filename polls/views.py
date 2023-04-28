from django.shortcuts import render ,get_object_or_404
from django.http import JsonResponse
from .models import job
# Create your views here.

def polls_list(request):
    max_objects=20
    polls= job.objects.all()[:max_objects]
    data= {"results": list(job.values("question", "created_by__username", "pub_date"))}
    return JsonResponse(data)
    
def polls_detail(request,pk):
    poll=get_object_or_404(job,pk=pk)
    data={"results":{
        "question":job.question,
        "created_by":job.created_by.username,
          "pub_date": job.pub_date 
        
    }}
    return JsonResponse(data)
    