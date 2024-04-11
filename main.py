# DeprecationWarning: There is no current event loop

import asyncio


async def func(index):
    print(f'Before {index}')
    await asyncio.sleep(0.1)
    print(f'After {index}...')

# 1) Create an event loop object ✅
loop = asyncio.new_event_loop()

# 2) Set the current event loop for the current OS thread ✅
asyncio.set_event_loop(loop)


async def create_tasks_func():
    tasks = []

    for idx in range(3):
        tasks.append(asyncio.create_task(func(idx)))
    await asyncio.wait(tasks)

loop.run_until_complete(create_tasks_func())
loop.close()