import ssl
import jwt
from typing import Annotated

from fastapi import Request, Depends

from .core import Authorization
from .exceptions import AuthException, Unauthorized
from .enums import UserRole

from src.user.service import get, create
from src.user.schemas import UserProfileCreate
from src.user.models import DBUserProfile
from src.database.core_async import DbAsyncSession
from src.config import get_settings

settings = get_settings()


def validate_token(request: Request) -> str:
    token = request.cookies.get("hanko")
    if not token:
        raise Unauthorized()

    try:
        # disable SSL certificate verification while in development
        if settings.environment != "prod":
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE

        jwks_client = jwt.PyJWKClient(
            settings.hanko_api_url + "/.well-known/jwks.json", ssl_context=ssl_context
        )
        signing_key = jwks_client.get_signing_key_from_jwt(token)
        data = jwt.decode(
            token,
            signing_key.key,
            algorithms=["RS256"],
            audience="localhost",
        )
        if data:
            return data

    except (jwt.DecodeError, Exception):
        raise AuthException()

    raise Unauthorized()


ValidToken = Annotated[dict, Depends(validate_token)]


async def get_userprofile(
    hanko_data: ValidToken,
    db_session: DbAsyncSession,
    auth: Authorization,
):
    user_id = hanko_data["sub"]
    user_email = hanko_data["email"]["address"]

    db_userprofile = await get(db_session, user_id)
    if not db_userprofile:
        userprofile = UserProfileCreate.model_validate(
            {"id": user_id, "role": UserRole.NORMAL, "first_name": "", "last_name": ""}
        )
        db_userprofile = await create(db_session, userprofile)
        await auth.api.sync_user(
            {
                "key": user_id,
                "email": user_email,
                "attributes": {
                    "roles": ["viewer"],
                },
            },
        )
        await auth.api.assign_role(user_id, "viewer", "default")

    return db_userprofile


UserProfile = Annotated[DBUserProfile, Depends(get_userprofile)]
