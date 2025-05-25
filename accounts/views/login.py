import random

from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.hashers import make_password

from accounts.models.otp import Otp
from accounts.models.user import User

from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers.email import EmailSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        try:
            user = User.objects.get(email=email, is_active=True)
        except User.DoesNotExist:
            return Response({'error': 'Usuário inativo ou não encontrado.'},
                            status=404)

        otp_code = ''.join(random.choices('0123456789', k=6))
        hashed_otp = make_password(otp_code)

        Otp.objects.update_or_create(user=user, defaults={
            'code': hashed_otp,
            'created_at': timezone.now()
        }
        )

        # send_mail(
        #     'Seu código OTP - IPRJ Plus',
        #     f'Seu código de login é: {otp_code}\n\nEle expira em 10 minutos.',
        #     None,
        #     [user.email],
        # )
        print(otp_code)
        return Response({'message': 'Código OTP enviado por e-mail.'},
                        status=200)
