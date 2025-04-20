# backend/app/infrastructure/websocket/ws_server.py
import websockets
from app.core.config import WEBSOCKET_PORT

async def handler(websocket):
    async for message in websocket:
        await websocket.send(f"Estado actualizado: {message}")

def iniciar_servidor():
    start_server = websockets.serve(handler, "0.0.0.0", WEBSOCKET_PORT)
    return start_server

if __name__ == "__main__":
    import asyncio
    asyncio.get_event_loop().run_until_complete(iniciar_servidor())
    asyncio.get_event_loop().run_forever()