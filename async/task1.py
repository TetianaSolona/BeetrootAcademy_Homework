import asyncio


async def fibbonachi(n):
    if 0 == n or 1 == n:
        return n
    return await fibbonachi(n-1) + await fibbonachi(n-2)


async def factorial(n):
    rez = 1
    for num in range(2, n + 1):
        rez = rez * num
    return rez


async def squares(n):
    return n ** 2


async def cubic(n):
    return n ** 3


async def main():
    result = []
    for num in range(10):
        rez = await asyncio.gather(fibbonachi(num), factorial(num), squares(num), cubic(num))
        result.append(rez)
    print(result)


if __name__ == '__main__':
    asyncio.run(main())