from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import Job
from django.contrib.auth.models import User
from .serializers import JobSerializer, UserSerializer

from .TopFive import TopFive
from django.forms.models import model_to_dict
import json
import sqlite3 as lite

# Create your views here.

def index(request):
    return HttpResponse("Just some text")

@api_view(['GET', 'POST'])
def job_list(request, format=None):
    """
    List all code jobs, or create a new job.
    """

    # Mock input
    info = dict()
    info['First Name'] = 'Jeongyeon'
    info['Last Name'] = 'Kim'
    info['Email'] = 'imurs4825@gmail.com'
    info['interests'] = ['Driver', 'Events']

    if request.method == 'GET':
        jobs = Job.objects.all()

        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)

        print("?")

        if serializer.is_valid():
            serializer.save()
            print("??")
            print(serializer.data)
            return Response()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)

        print(serializer.error_messages)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        con = lite.connect('jobs.sqlite3')
        with con:
            cursor = con.cursor()
            cursor.execute("CREATE TABLE rest_user(Id INTEGER PRIMARY KEY AUTOINCREMENT, FirstName TEXT, LastName TEXT, Email TEXT, interest1 TEXT, interest2 TEXT)")
            #cursor.execute("INSERT INTO User (FirstName, Lastname, Email) VALUES(?, ?, ?)", (info['First Name'], info['Last Name'], info['Email'], info['Email']))
        return Response()


@api_view(['GET', 'PUT', 'DELETE'])
def job_detail(request, format=None):
    """
    Retrieve, update or delete a job instance.
    """

    # Mock input
    info = dict()
    info['First Name'] = 'Jeongyeon'
    info['Last Name'] = 'Kim'
    info['Email'] = 'imurs4825@gmail.com'
    info['interests'] = ['Driver', 'Events']



    try:
        pass
        # job = Job.objects.get(pk=pk)
        #job = Job.objects.filter(category=interests[0])

    except Job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        # Return top 5 recommendation
        rankings = TopFive(info['interests'], list(Job.objects.values()) , 2)
        rankings_json = json.dumps(rankings)
        print(rankings_json)

        '''
        serializer = JobSerializer(rankings_json, many=True)
        return Response(serializer.data)
        '''

        return Response(rankings_json)




    elif request.method == 'PUT':
        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
