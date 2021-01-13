import datetime
import jwt
from django.conf import settings


def generate_access_token(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }

    return jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm='HS256').encode(encoding='utf-8')
