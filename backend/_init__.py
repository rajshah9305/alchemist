# backend/__init__.py
from .main import app
from .api import router
from .models import Interaction
from .database import init_db

__all__ = ["app", "router", "Interaction", "init_db"]