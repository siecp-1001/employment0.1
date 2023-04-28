from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from .models import job,createjob
from .serializers import  Pollserializer,Choiceserializer,Voteserializer,UserSerializer

class PollList(generics.ListCreateAPIView):
        queryset= job.objects.all()
        serializer_class=Pollserializer

class PollDetail(generics.ListCreateAPIView):
    queryset=job.objects.all()
    serializer_class= Pollserializer
    
    
class Choicelist(generics.ListCreateAPIView):
   def get_queryset(self):
       queryset=Choice.objects.filter(job_id=self.kwargs["pk"])
       return queryset
   serializer_class=Choiceserializer
       
 #make post code   
class Createvote(APIView):
    serializer_class=Voteserializer
    def post(self,request,pk,choice_pk):
        voted_by=request.data.get("voted_by")
        data= {"choice":choice_pk,"poll":pk,"voted_by":voted_by}
        serializer=Voteserializer(data=data)
        if serializer.is_valid():
            vote=serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
           
class PollViewSet(viewsets.ModelViewSet):
     queryset = job.objects.all()
     serializer_class = Pollserializer      
        
class UserCreate(generics.CreateAPIView):
     authentication_classes = ()
     permission_classes = ()
     serializer_class = UserSerializer         


class LoginView(APIView):
      permission_classes = ()
      def post(self, request,):
         username = request.data.get("username")
         password = request.data.get("password")
         user = authenticate(username=username, password=password)
         if user:
             return Response({"token": user.auth_token.key} )
         else:
              return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)