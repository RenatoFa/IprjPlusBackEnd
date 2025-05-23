import random

from django.core.mail import send_mail

from models.otp import OTP
from models.user import User

from rest_framework.response import Response
from rest_framework.views import APIView

from serializers.email import EmailSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']  # type: ignore

        try:
            user = User.objects.get(email=email, is_active=True)
        except User.DoesNotExist:
            return Response({'error': 'Usuário inativo ou \
                             não encontrado.'}, status=404)

        otp_code = ''.join(random.choices('0123456789', k=6))
        OTP.objects.create(user=user, code=otp_code)

        send_mail(
            'Seu código OTP - IPRJ Plus',
            f'Seu código de login é: {otp_code}\n\nEle expira em 10 minutos.',
            None,
            [user.email],
        )
        return Response({'message': 'Código OTP \
                         enviado por e-mail.'}, status=200)
