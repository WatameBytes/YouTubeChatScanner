import asyncio

async def function1():
   print("Inside Function 1")

async def function2():
   print("Inside Function 2")

if __name__ == "__main__":
   loop = asyncio.get_event_loop()
   loop.run_until_complete(asyncio.gather(function1(), function2()))