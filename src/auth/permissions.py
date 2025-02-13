from fastapi import Request

from src.auth.core import Authorization
from src.auth.dependencies import UserProfile
from src.auth.utils import get_resource_from_path, get_action_from_method


async def crud_permission(
    request: Request, db_userprofile: UserProfile, auth: Authorization
):
    user_id = db_userprofile.id
    resource_name = get_resource_from_path(request.url.path)
    action_name = get_action_from_method(request.method)

    await auth.check(user_id, action_name, resource_name)
