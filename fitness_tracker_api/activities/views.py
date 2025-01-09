from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Exercise, User, Activity
from .serializers import ExerciseSerializer, UserSerializer, ActivitySerializer

# View for Exercise model
class ExerciseList(APIView):
    def get(self, request):
        try:
            exercises = Exercise.objects.all()
            serializer = ExerciseSerializer(exercises, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = ExerciseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# View for Activity model
class ActivityList(APIView):
    def get(self, request):
        try:
            activities = Activity.objects.all()
            serializer = ActivitySerializer(activities, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = ActivitySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
