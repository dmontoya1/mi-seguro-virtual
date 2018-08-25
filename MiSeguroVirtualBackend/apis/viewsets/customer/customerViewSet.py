from rest_framework.views import APIView
from rest_framework.response import Response


from ...serializers import CustomerSerializer
from users.models import Customer

class CustomerViewSet(APIView):

    def post(self, request, format=None):

        serializer = CustomerSerializer(data=request.data)

        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()

                return Response(dict(status='done', details=serializer.data), status=200)

        except Exception as e:

            return Response(dict(status='error', details=str(e)), status=400)