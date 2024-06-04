import asyncio
from aiohttp import web
import socketio

localhost = "0.0.0.0"
port = 8080

sio = socketio.AsyncServer()

app = web.Application()

sio.attach(app)


async def index(request):
    with open("index.html") as f:
        return web.Response(text=f.read(), content_type="text/html")


@sio.on("message")
async def print_message(sid, message, name):
    print("Socket ID", sid)
    print(name)
    print(message)
    data = {"name": name, "message": message}
    await sio.emit("add_msg", data)


app.router.add_get("/", index)


if __name__ == "__main__":
    web.run_app(app, host=localhost, port=port)
