from contextlib import asynccontextmanager
from typing import AsyncGenerator

from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from {{ package_name }}.api.router import router as api_router
from {{ package_name }}.settings import config


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Manage application lifespan events.
    """
    # Startup.
    yield
    # Shutdown.
    pass


def create_app() -> FastAPI:
    app = FastAPI(
        title=config.project_name,
        version=config.version,
        description=config.description,
        openapi_url="/openapi.json" if config.environment != "production" else None,
        docs_url="/docs" if config.environment != "production" else None,
        redoc_url="/redoc" if config.environment != "production" else None,
        lifespan=lifespan,
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    app.include_router(api_router)

    return app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        create_app(),
        host="0.0.0.0",
        port=config.port,
        reload=config.environment == "development",
    )
