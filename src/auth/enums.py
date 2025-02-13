from enum import Enum, StrEnum


class UserRole(Enum):
    NORMAL = "NORMAL"
    ADMIN = "ADMIN"
    SUPER_ADMIN = "SUPER_ADMIN"


class GlobalPermissionAction(StrEnum):
    CREATE = "create"
    READ = "read"
    UPDATE = "update"
    DELETE = "delete"
