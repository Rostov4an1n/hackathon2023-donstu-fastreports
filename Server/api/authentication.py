from rest_framework import authentication
from rest_framework import exceptions
from .models import ApiKey


class ApiKeyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        api_key = request.META.get('HTTP_API_KEY')

        if not api_key:
            return None

        try:
            api_key = ApiKey.objects.get(key=api_key)
        except ApiKey.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid API Key')

        return (api_key.user, None)
