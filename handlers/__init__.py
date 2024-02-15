from aiogram import Router
from handlers import start, on_edit

def setup_routers() -> Router:


    router = Router()
    router.include_router(start.router)
    router.include_router(reply.router)

    return router
