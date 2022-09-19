from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from project.models import Project
from project.api.serializers import ProjectSerializer

# permission classes for authentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def api_detail_project_view(request, pk):
    try:
        project = Project.objects.get(id=pk)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def api_project_view(request):
    try:
        project = Project.objects.all()
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def api_update_project_view(request,pk):
    try:
        project = Project.objects.get(id=pk)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # # For making sure the one who can access the project
    user = request.user
    if project.employee != user:
        return Response({'response':'You do not have permission to edit it'})

    if request.method == 'PUT':
        serializer = ProjectSerializer(project, data=request.data)
        data ={}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data = data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
@permission_classes((IsAuthenticated,))
def api_delete_project_view(request,pk):
    try:
        project = Project.objects.get(id=pk)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # For making sure the one who can access the project

    user = request.user
    if project.employee != user:                 
        return Response({'response': 'You do not have permission to delete it'})

    if request.method == 'DELETE':
        operation = project.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)

@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def api_post_project_view(request):
    account = request.user

    project = Project(employee=account)

    if request.method == "POST":
        serializer = ProjectSerializer(project, data=request.data)

        # data ={}
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
