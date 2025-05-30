from enum import StrEnum

from {{ package_name }}.schemas.base import BaseResponse


class Status(StrEnum):
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"


class Response(BaseResponse):
    status: Status
