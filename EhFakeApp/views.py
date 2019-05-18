from rest_framework import viewsets

from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response


class PoliticianViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Politician.objects.all().order_by('id')
    serializer_class = PoliticianSerializer


@api_view()
def non_voted(request):
    lawProjects = LawProject.objects.filter(voted=False)
    id_list = []

    for project in lawProjects:
        id_list.append(project.foreign_id)

    return Response(id_list)


@api_view()
def send_push(request):
    data_manager.send_notification()

    return Response("ok")


@api_view()
def get_followed_politicians(request):
    username = request.user.username
    politicians = Politician.objects.filter(followers__username=username)
    serializer = PoliticianSerializer(politicians, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def add_expo_token(request):
    username = request.user.username


    return Response("ok")





