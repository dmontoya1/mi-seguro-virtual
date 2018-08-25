from rest_framework.views import APIView
from rest_framework.response import Response


from ...serializers import ClientSerializer
from credits_webapp.users.models import Client

class ClientViewSet(APIView):

    def post(self, request, format=None):

        serializer = ClientSerializer(data=request.data)

        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()

                return Response(dict(status='done', details=serializer.data), status=200)

        except Exception as e:

            return Response(dict(status='error', details=str(e)), status=400)