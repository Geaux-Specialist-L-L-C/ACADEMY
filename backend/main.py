"""
Main entrypoint for the FastAPI application.

This module instantiates the FastAPI app, configures middleware, and wires up
all available API routers.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database import init_db
from backend.routes import assessments, auth, chat_history, learning_plans, student_dashboard, users

init_db()

app = FastAPI(title="Geaux Academy API", version="0.1.0")

# CORS configuration to support the frontend during development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routers
app.include_router(auth.router, tags=["auth"])
app.include_router(users.router, tags=["users"])
app.include_router(student_dashboard.router, tags=["students"])
app.include_router(learning_plans.router, tags=["learning-plans"])
app.include_router(assessments.router, tags=["assessments"])
app.include_router(chat_history.router, tags=["chats"])


@app.get("/health", tags=["health"])
async def health_check() -> dict[str, str]:
    """Simple health check endpoint."""
    return {"status": "ok"}
