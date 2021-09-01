from rest_framework.views import APIView
from .models import *
from rest_framework import generics, permissions, response
from .serializers import *
from django.db.models import Prefetch

class ScoreList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VerifyFlag(APIView):
    def post(self, request):
        #print("DEBUG request Flag: ", request.data['flag'])
        #print("DEBUG request name: ", request.data['name'])
        obj = WebFlagMaster.objects.filter(flag=request.data['flag'])
        #print("DEBUG FlagMaster Name: ", obj[0].name)
        #print("DEBUG FlagMaster points: ",obj[0].points)
        #print("DEBUG FlagMaster flag: ",obj[0].flag)
        user = Score.objects.get(user=request.user)
        #print(user)
        #print(user.points)
        user.points = user.points + obj[0].points
        user.save()
        #print(user.points)

        return response.Response(data={"Authenticated Inside":"Scoring - IndScoreView"}, status=status.HTTP_200_OK)

class UserScore(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ScoreSerializer
    lookup_field = 'slug'
    
    def get_queryset(self):
        return Score.objects.filter(slug=self.kwargs['slug'])

class HighScoreList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Score.objects.all()
    serializer_class = HighScoreSerializer

class UserHighScoreList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = HighScoreSerializer

    def get_queryset(self):
        return Score.objects.filter(user=self.request.user)
