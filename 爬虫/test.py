import asyncio
import httpx

async def my_get():
    async with httpx.AsyncClient() as client:
        r = await client.get("https://www.baidu.com")
        print(r.text)

if __name__ == '__main__':
    asyncio.run(my_get())

