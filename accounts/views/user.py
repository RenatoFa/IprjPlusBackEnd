from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
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
            f'Olá {user.name}, sua conta no IPRJ Plus foi criada \
                com sucesso!\n\
                Aguarde a ativação pelo administrador.',
            None,
            [user.email],
        )
        return Response({'message': 'Usuário criado com sucesso. \
                         Aguarde aprovação.'}, status=201)


class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request):
        user = request.user
        name = request.data.get('name')
        date_of_birth = request.data.get('date_of_birth')
        avatar = request.FILES.get('avatar')

        if name:
            user.name = name
        if date_of_birth:
            user.date_of_birth = date_of_birth
        if avatar:
            user.avatar = avatar

        user.save()

        return Response({
            'message': 'Perfil atualizado com sucesso.',
            'name': user.name,
            'date_of_birth': user.date_of_birth,
            'avatar_url': user.avatar.url if user.avatar else None
        }, status=status.HTTP_200_OK)
