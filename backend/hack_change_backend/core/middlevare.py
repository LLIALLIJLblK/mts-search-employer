import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from hack_change_backend.core.logger import logger


class TimeMiddleware(BaseHTTPMiddleware):

    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):

        start_time = time.time()
        response = await call_next(request)
        execute_time = str(round((time.time() - start_time), 4))
        response.headers["X-execute-time"] = execute_time
        logger.debug(
            f"[ET] Request: {request.url.path}, Execution Time: {execute_time} seconds, path: {request.url.path}, method: {request.method}",
        )
        return response
