from django.shortcuts import render
from sm_app.models import*
from sm_app.serializers import*
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RegisterView(CreateAPIView):
    serializer_class=UserSerializer
    queryset=CustomUser.objects.all()

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserPostListView(ListAPIView):
    serializer_class=PostSerializer

    def get_queryset(self):
        user_id=self.kwargs['user_id']
        return Post.objects.filter(owner_id=user_id)

class AllPostListView(ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class PostEditDeleteView(RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    lookup_field='id'

class CommentViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset=Like.objects.all()
    serializer_class=LikeSerializer



    