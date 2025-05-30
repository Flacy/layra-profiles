from fastapi import APIRouter

from {{ package_name }}.api.v1.routes import health

router = APIRouter(prefix="/v1")
router.include_router(health.router)
