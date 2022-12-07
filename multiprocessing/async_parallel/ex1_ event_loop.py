import asyncio


async def tick():
    print('Tick')
    await asyncio.sleep(1)  # возвращает управление вызывающему коду
    print('Tock')

    loop = asyncio.get_running_loop()
    if loop.is_running():
        print('Loop is still running')


async def main_coroutine():

    awaitable_object = asyncio.gather(tick(), tick(), tick())

    for task in asyncio.all_tasks():
        print(task)

    await awaitable_object


def coroutines_loop():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main_coroutine())
        print('loop is closed')
    finally:
        loop.close()
        print('loop closed')


def main():
    coroutines_loop()  # примерно так действует asyncio.run()

    asyncio.run(main_coroutine())


if __name__ == '__main__':
    main()
