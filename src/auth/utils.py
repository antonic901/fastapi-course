from http import HTTPMethod

from .enums import GlobalPermissionAction


def get_resource_from_path(path: str):
    try:
        return path.strip("/").split("/")[0]
    except Exception:
        return None


def get_action_from_method(method: HTTPMethod):
    action_name = GlobalPermissionAction.READ
    if method == HTTPMethod.POST:
        action_name = GlobalPermissionAction.CREATE
    elif method == HTTPMethod.PATCH or method == HTTPMethod.PUT:
        action_name = GlobalPermissionAction.UPDATE
    elif method == HTTPMethod.DELETE:
        action_name = GlobalPermissionAction.DELETE

    return action_name
