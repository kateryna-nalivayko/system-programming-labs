import asyncio
import aiohttp

from util import async_timed


@async_timed()
async def get_example_status(session: aiohttp.ClientSession, url: str) -> int:
    async with session.get(url, ssl=False) as response:
        return response.status


@async_timed()
async def main():
    urls = ["https://example.com" for _ in range(5)]

    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_example_status(session, url)) for url in urls]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())