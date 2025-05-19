from fastapi import APIRouter

# Create a router for each API group
hashtag_router = APIRouter(prefix="/api/hashtags", tags=["hashtags"])

# Import routes
# from .hashtag_routes import *  # Uncomment if you add specific route modules

# Export routers
__all__ = ["hashtag_router"]