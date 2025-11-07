import asyncio
import requests

from util import async_timed


@async_timed()
async def get_example_status() -> int:
    response = requests.get("https://example.com")
    return response.status_code


@async_timed()
async def main():
    tasks = [asyncio.create_task(get_example_status()) for _ in range(5)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())