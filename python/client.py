import asyncio
import argparse
import websockets
import time

parser = argparse.ArgumentParser(description="simple websocket client")
parser.add_argument(
    "-s", "--server", help="server ws://addr:port", default="ws://192.168.2.1:8765")

args = parser.parse_args()


async def senddata(data, websocket):
    await websocket.send(data)


async def main():
    async with websockets.connect(args.server, max_size=5 ** 20, ping_interval=None, compression=None, ping_timeout=None) as websocket:
        file_handle = open("frame.raw", "rb")
        message = bytearray(file_handle.read())

        frame_counter = 0
        while True:
            try:
                before_send = time.time()
                await websocket.send(message)
                after_send = time.time()
                send_time = after_send - before_send
                frame_counter += 1
                if frame_counter == 30:
                    print(
                        f"FPS = {1 / send_time:.2f}, websocket send time = {send_time*1000:.1f}ms")
                    frame_counter = 0

            except websockets.ConnectionClosed as err:
                print(
                    f"Connection Closed: code = {err.code}, reason = {err.reason}")
                quit()

            except KeyboardInterrupt:
                quit()

if __name__ == "__main__":
    asyncio.run(main())
