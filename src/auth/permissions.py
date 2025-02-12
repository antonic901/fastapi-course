from http import HTTPMethod

from fastapi import Request

from src.auth.core import Authorization
from src.auth.enums import GlobalPermissionAction
from src.auth.dependencies import UserProfile


async def crud_permission(
    request: Request, db_userprofile: UserProfile, auth: Authorization
):
    user_id = db_userprofile.id
    resource_name = request.url.path.strip("/").split("/")[0]

    action_name = GlobalPermissionAction.READ
    if request.method == HTTPMethod.POST:
        action_name = GlobalPermissionAction.CREATE
    elif request.method == HTTPMethod.PATCH or request.method == HTTPMethod.PUT:
        action_name = GlobalPermissionAction.UPDATE
    elif request.method == HTTPMethod.DELETE:
        action_name = GlobalPermissionAction.DELETE

    await auth.check(user_id, action_name, resource_name)
