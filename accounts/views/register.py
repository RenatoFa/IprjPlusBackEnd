from rest_framework.views import APIView
from rest_framework.response import Response

from django.core.mail import send_mail

from accounts.serializers.register import RegisterSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        send_mail(
            'Conta criada - IPRJ Plus',
            f'Olá {user.name}, sua conta foi criada com sucesso!\n\
                Aguarde a ativação pelo administrador.',
            None,
            [user.email],
        )
        return Response({'message': 'Usuário criado com sucesso. \
                         Aguarde aprovação.'}, status=201)
