
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import job,createjob,Vote
from rest_framework.authtoken.models import Token


class Voteserializer(serializers.ModelSerializer):
    class  Meta:
        model=Vote
        fields='__all__'
        
        
class Choiceserializer(serializers.ModelSerializer):
    votes= Voteserializer(many=True,required=False)
    class Meta:
        model=createjob
        fields='__all__'  
        
class Pollserializer(serializers.ModelSerializer):
    choices=  Choiceserializer(many=True,read_only=True,required=False)
    class Meta:
        model=job
        fields='__all__'      



class UserSerializer(serializers.ModelSerializer):
    class Meta:
       model = User
       fields = ('username', 'email', 'password')
       extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User(
        email=validated_data['email'],
        username=validated_data['username']
         )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user 


