from rest_framework.views import APIView
from rest_framework.response import Response


from ...serializers import CustomerSerializer
from users.models import Customer

class CustomerViewSet(APIView):
    permission_classes = ()

    def post(self, request, format=None):

        user = dict(username=request.data['username'], first_name=request.data['first_name'], last_name=request.data['last_name'], email=request.data['email'], password=request.data['password'])
        user_data = dict(document_number=request.data['document_number'], cellphone_number=request.data['cellphone_number'], user=user)
        ip = get_client_ip(request)

        serializer = CustomerSerializer(data=user_data)

        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()

                return Response(dict(status='done', details=serializer.data), status=200)

        except Exception as e:

            return Response(dict(status='error', details=str(e)), status=400)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip