# class WebFlags(models.Model):
#     flag = models.CharField(max_length=12);
#     points = models.IntegerField();
#     name = models.CharField(max_length=20);

#     def __str__(self):
#         return f"{self.name}"

# class Score(models.Model):
#     myUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE);
#     name = models.CharField(max_length=20);
#     flag = models.CharField(max_length=12);
#     points = models.IntegerField(); 
#     completed = models.BooleanField(default=False);   

#     def __str__(self):
#         return f"{self.myUser.username} {self.name}"


# class Register(generics.ListCreateAPIView):
#     serializer_class = RegisterSerializer

#     def post(self, request):
#         data_set={}
#         resp = WebFlags.objects.filter(name=self.request.data['name'])
#         if len(resp) == 1:
#             data_set = {"name": resp[0].name, "points": resp[0].points, "flag": resp[0].flag, "myUser": self.request.user.id}
#         serializer = RegisterSerializer(data=data_set)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#class HighscoreView(APIView):
# class HighscoreView(APIView):
    
#     def get(self, request):
#         users = Score.objects.values_list('myUser', flat=True).distinct()
#         rollup = {}
#         print(rollup)
#         for u in users:
#             score = {'user':'', 'score':0}
#             res = Score.objects.filter(completed=True).filter(myUser=u)
#             score['user'] = u
#             for r in res:
#                 score['score'] = r.points + score['score']
#             rollup = score
        
#         print(rollup)
#         queryset = Score.objects.filter(completed=True)
#         serializer_class = HighScoreSerializer(queryset, many=True)
#         print(json.dumps(serializer_class.data, indent=4))

#         #return Response(rollup)
#         return Response(serializer_class.data)

#class Ind_ScoreView(APIView):
# class Ind_ScoreView(generics.ListAPIView):
#     serializer_class = IndividualScoreSerializer

#     def get_queryset(self):
#         return Score.objects.filter(myUser=self.request.user)

    # def get(self, request):
    #      return Response(data={"Authenticated Inside":"Scoring - IndScoreView"}, status=status.HTTP_200_OK)

# class ScoreFlag(generics.ListCreateAPIView):
#     serializer_class = ScoreFlagSerializer

#     def get_queryset(self):
#         return Flags.objects.filter(flag=self.request.data['flag'])

#     def post(self, request):
#         print(self.request.data['flag'])
#         serializer = ScoreFlagSerializer(data=request.data)
#         print(self.request.user)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


    # url(r'score/', ScoreListView.as_view()),
    # url(r'score/?P<pk>\d+)/$', ScoreView.as_view()),
    # url(r'webflag/$', WebFlagListView.as_view()),
    # url(r'webflag/(?P<pk>\d+)/$', WebFlagView.as_view()),
    # path('highscore/', HighscoreView.as_view(), name='highscore_view'),
    # path('ind_score/', Ind_ScoreView.as_view(), name='ind_score_view'),
    # path('register/', Register.as_view(), name='register'),
    #path('score_flag/', ScoreFlag.as_view(), name='score_flag'),


# class WebSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Web  
#         fields = ('name', 'flag', 'points', 'completed')

# class UserWebSerializer(serializers.ModelSerializer):
#     web = WebSerializer()
#     user = serializers.SerializerMethodField()

#     def get_user(self, obj):
#         return obj.myUser.username

#     class Meta:
#         model=Score
#         fields='__all__'

# class RegisterSerializer(serializers.ModelSerializer):
#     user = serializers.SerializerMethodField()
    
#     def get_user(self, obj):
#         return obj.myUser.username

#     class Meta:
#         model=Score
#         fields = '__all__'

#     def create(self, validated_data):
#         instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
#         instance.save()
#         return instance

# class RegisterScoreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Score
#         fields = '__all__'

#     def create(self, validated_data):
#         instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
#         instance.save()
#         return instance

# class HighScoreSerializer(serializers.ModelSerializer):
#     user = serializers.SerializerMethodField()

#     def get_user(self, obj):
#         return obj.myUser.username

#     class Meta:
#         model=Score
#         fields=('user', 'points')

# class HighScoreSerializer(serializers.ModelSerializer):
#     user = serializers.SerializerMethodField()

#     #total_score = serializers.SerializerMethodField()

#     def get_user(self, obj):
#         return obj.myUser.username

#     # def get_total_score(self, obj):
#     #     resp = obj.web + obj.steganography
#     #     return resp

#     class Meta:
#         model = Score
#         fields = ("user", "web")

class IndividualScoreSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    myWeb = serializers.SerializerMethodField()
    #total_score = serializers.SerializerMethodField()

    # def get_total_score(self, obj):
    #     resp = obj.web + obj.steganography
    #     return resp

    def get_user(self, obj):
        return obj.myUser.username

    def get_myWeb(self, obj):
        print("DEBUG: ", obj.myWeb)
        return obj.myWeb.myWeb

    class Meta:
        model = Score
        fields = ("user", "web", "myWeb")
    
# class ScoreFlagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Flags
#         fields = ('flag', 'points')

# class WebFlagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=WebFlags
#         fields = ('flag', 'points', 'name', 'user')

#     def validate_name(self, name):
#         mflag_name = self.context.get('flag_name')
#         print("Context Flag Name: ", mflag_name)
#         if (name == mflag_name):
#             return name
#         else:
#             raise serializers.ValidationError("Not a challeneg name")

#     def validate_points(self, points):
#         mflag_points = self.context.get('flag_points')
#         print("Context Flag Name: ", mflag_points)
#         if (points == mflag_points):
#             return points
#         else:
#             return mflag_points

#     def validate_flag(self, flag):
#         mflag_value = self.context.get('flag_value')
#         print("Context flag value: ", mflag_value)
#         print("Flag Value: ", flag)
#         if (flag == mflag_value):
#             return flag
#         elif (flag == ''):
#             return flag
#         else:
#             raise serializers.ValidationError("Flags is not correct")



# Serialziers for High Score Funcationality
# class HighScoreFlagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=WebFlags
#         fields = ('points', 'name')




    # def to_representation(self, instance):
    #     result = super(HighScoreSerializer, self).to_representation(instance)
    #     test = OrderedDict([(key, result[key]) for key in result if result[key] is not None])
    #     if 'flags' in test:
    #         return test
    #     else:
    #         return


# class Flags(generics.RetrieveUpdateAPIView):
#     permission_classes = (permissions.AllowAny,)
#     queryset = Score.objects.all()
#     serializer_class = ScoreSerializer

#     def get_serializer_context(self):
#         flag_name = Score.objects.filter(slug=self.kwargs['slug']).filter(pk=self.kwargs['pk'])
#         master_flag = WebFlagMaster.objects.filter(name=flag_name[0].flags)
        
#         context = super().get_serializer_context()
#         context.update({
#             "flag_name": master_flag[0].name,
#             "flag_value": master_flag[0].flag,
#             "flag_points": master_flag[0].points,
#         })
#         return context