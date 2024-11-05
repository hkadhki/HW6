import aiohttp
import asyncio

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json() 
                print('Body: \n',data, '\n')
                print('Headers: \n',response.headers, '\n')
                
            else:
                print(f'Ошибка: {response.status}')
                return None

async def main():
    url = 'https://jsonplaceholder.typicode.com/posts/'

    for i in range(1,6):
        await fetch_data(url + str(i))


if __name__ == '__main__':
    asyncio.run(main())