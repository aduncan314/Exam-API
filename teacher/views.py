from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from teacher.models import Teacher
from teacher.serializers import TeacherSerializer


@api_view(['GET', 'POST'])
def teacher_list(request):
    """
    Full list
    :param request:
    :return:
    """
    if request.method == 'GET':
        snippets = Teacher.objects.all()
        serializer = TeacherSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def teacher_detail(request, pk):
    try:
        snippet = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeacherSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TeacherSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
