from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Member
from .serializers import MemberSerializer

class MemberListAPI(APIView):
    def get(self, request):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)