import contextlib

from rest_framework_simplejwt.authentication import JWTAuthentication

from abstract.models import BaseModel


class InjectUserObj:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            auth_header = request.headers.get("Authorization", "").split()
            if len(auth_header) == 2 and auth_header[0].lower() == "bearer":
                with contextlib.suppress(Exception):
                    request.user = JWTAuthentication().get_user(
                        JWTAuthentication().get_validated_token(auth_header[1])
                    )
        BaseModel.operating_user = (
            request.user if request.user.is_authenticated else None
        )
        return self.get_response(request)