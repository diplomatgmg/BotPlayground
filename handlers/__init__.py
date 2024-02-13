from aiogram import Router


def setup_routers() -> Router:
    from handlers import start, reply

    router = Router()
    router.include_router(start.router)
    router.include_router(reply.router)

    return router
