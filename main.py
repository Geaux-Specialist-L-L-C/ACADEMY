"""
Expose the FastAPI application for Uvicorn using the documented target ``main:app``.

The actual application is defined in ``backend/main.py`` alongside the rest of the
backend modules. This module simply re-exports the ``app`` instance so running::

    uvicorn main:app --reload

behaves as expected from the project root.
"""

from backend.main import app

__all__ = ["app"]
