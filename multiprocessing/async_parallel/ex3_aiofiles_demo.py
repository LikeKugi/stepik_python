import asyncio

import aiofiles


def read_large_file():
    with open('..\\multiasync_parallel\\16Kints.txt') as inf:
        return inf.read()


async def async_read_large_file():
    async with aiofiles.open('..\\multiasync_parallel\\16Kints.txt') as inf:
        return await inf.read()


def count_numbers(numbers: str) -> int:
    return len(numbers.split())


async def async_main():
    text = await async_read_large_file()
    print(count_numbers(text))


def main():
    text = read_large_file()
    print(count_numbers(text))


if __name__ == '__main__':
    asyncio.run(async_main())
    main()