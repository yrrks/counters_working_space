from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from app_counter.serializers import CounterSerializer
from app_counter.models import Counter
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.db.models import F


class HelloAPIView(APIView):

    def get(self,request):

        content = {
            'message': 'Hello, world'
        }

        return Response(content)


class CounterListView(generics.ListAPIView):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer

class CounterDetailView(generics.RetrieveAPIView):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer


class CounterIncreaseView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        counter = get_object_or_404(Counter,pk=pk,user=request.user)
        counter.value +=1
        counter.save()

        return Response({
            'action': 'increase',
            'isComplete': True,
        })

class CounterDecreaseView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        counter = get_object_or_404(Counter,pk=pk,user=request.user)
        counter.value -=1
        counter.save()

        return Response({
            'action': 'decrease',
            'isComplete': True,
        })

class NewCounter(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        counter = Counter.objects.create(user=request.user)

        return Response({
            'action': 'new counter',
            'isComplete': True,
        })