import os
import uvloop
import asyncio

uvloop.install()

if __name__ == "__main__":
    from hydrogram import Client, idle
    from environment import api_id, api_hash, bot_token

    bot = Client(
        "writer", api_id, api_hash, bot_token=bot_token, plugins=dict(root="plugins")
    )

    async def main():
        await bot.start()
        if os.path.exists("reset.txt"):
            with open("reset.txt", "r") as f:
                await bot.send_message(int(f.read()), "Chương trình đã được khởi động")
            os.remove("reset.txt")
        print("V2Writer", flush=True)
        os.system("chmod +x ./lite")
        await idle()
        return

    asyncio.run(main())
