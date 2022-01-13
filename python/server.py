import asyncio
import websockets
import argparse

parser = argparse.ArgumentParser(description="simple websocket server")
parser.add_argument(
    "-w", "--write", help="Writes the last frame to output.raw", default=True, type=bool)
parser.add_argument(
    "-i", "--ip", help="ip interface to listen on", default="192.168.2.1")
parser.add_argument("-p", "--port", help="port", default=8765, type=int)
args = parser.parse_args()


async def echo(websocket):
    async for message in websocket:
        if args.write == True:
            f = open("output.raw", "wb")
            f.write(message)
            f.close()


async def main():
    async with websockets.serve(echo, args.ip, args.port, max_size=None, ping_timeout=None, compression=None):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
