from accounts.models.otp import Otp
from accounts.models.user import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.serializers.otp import OTPSerializer


class OTPView(APIView):
    def post(self, request):
        serializer = OTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        code = serializer.validated_data['otp']

        try:
            user = User.objects.get(email=email)
            otp = Otp.objects.filter(user=user).latest('created_at')
        except (User.DoesNotExist, Otp.DoesNotExist):
            return Response({'error':
                             'Usuário não existe ou Otp não existe.'},
                            status=400)

        if not otp.is_valid():
            return Response({'error': 'Código expirado.'}, status=400)

        if not otp.check_code(code):
            return Response({'error': 'Código inválido.'}, status=401)

        token = RefreshToken.for_user(user)
        return Response({
            'refresh': str(token),
            'access': str(token.access_token),
            'name': user.name,
            'date_of_birth': user.date_of_birth,
            'avatar_url': user.avatar.url,
        })
