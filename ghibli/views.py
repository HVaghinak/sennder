# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ghibli.serializers import FetchGhibliMovieSerializer


class FetchGhibliMovieAPIView(APIView):
    serializer_class = FetchGhibliMovieSerializer

    def get(self, request):
        serializer = self.serializer_class(data=request.query_params, context={'request': request})

        response = serializer.response

        return Response(response, status=status.HTTP_200_OK)
