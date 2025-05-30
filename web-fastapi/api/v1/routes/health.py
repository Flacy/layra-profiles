from fastapi import APIRouter

from {{ package_name }}.schemas.health import Status, Response

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/check")
async def health_check() -> Response:
    return Response(status=Status.HEALTHY, message="Service is running")
