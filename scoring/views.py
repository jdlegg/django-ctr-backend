import json
from rest_framework.status import HTTP_412_PRECONDITION_FAILED
from rest_framework.views import APIView
from .models import *
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import *
from django.db.models import Prefetch, query

class ListUserFlags(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class IndividualUserFlags(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserFlagSerializer
    lookup_field = 'slug'
    
    def get_queryset(self):
        return Score.objects.filter(slug=self.kwargs['slug'])

class ListFlags(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = FlagsSerializer
    queryset = Flags.objects.all().order_by('id')

class UpdateFlags(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = FlagsSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Flags.objects.filter(id=self.kwargs['id'])

class HighScoreList(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        data_resp = []
        items = Score.objects.all()
        for i in items:
            data = {}
            data['username'] = i.slug
            data['points'] = i.points_total()
            data_resp.append(data)
        print(data_resp)
        return Response(data_resp, status=status.HTTP_200_OK)

class IndividualScore(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        data_resp = []
        items = Score.objects.filter(user=request.user)
        for i in items:
            data_resp.append(i.points_total())
        print(data_resp)
        return Response(data_resp, status=status.HTTP_200_OK)


class VerifyFlagOld(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserFlagSerializer
    lookup_field = 'slug'
    
    def get_queryset(self):
        return Score.objects.filter(slug=self.kwargs['slug'])
    
    def post(self, request):
        serializer = UserFlagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class VerifyFlag(APIView):   

    def post(self, request):
        # See if challenge exists
        try:
            obj1 = Flags.objects.get(name=request.data['name'])
        except:
            return Response(data={"Challenge does not exist"}, status=status.HTTP_412_PRECONDITION_FAILED)

        # check if flags match
        if (obj1.flag == request.data['flag']):
            # If it does, pull the record and add the flag
            score_obj = Score.objects.get(user=request.user)
            score_obj.flags.add(obj1)
        else:
            return Response(data={"Flag incorrect"}, status=status.HTTP_412_PRECONDITION_FAILED)

        return Response(data={"Already Solved":"DEBUG!!"}, status=status.HTTP_200_OK)


class VerifyChallenge(generics.RetrieveAPIView):   

    def get(self, request, **kwargs):
        print(kwargs.get('name'))
        obj1 = list(Score.objects.get(user=request.user).flags.all())
        for o in obj1:
            print(f"Comparing {o.name} == {kwargs.get('name')}")
            if (o.name == kwargs.get('name')):
                 return Response(data={"Already Solved VerifyChallenge":"DEBUG!!"}, status=status.HTTP_200_OK)
        return Response(data={"Not Solved! VerifyChallenge":"DEBUG!!"}, status=status.HTTP_202_ACCEPTED)