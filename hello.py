import asyncio

async def fetch_data(id):

    print(f"fetching data consecutively from {id}")
    await asyncio.sleep(2)
    print(f"Hello From{id}")

async def main():
    results = await asyncio.gather(
        fetch_data('Api 1'),
        fetch_data('Api 2'),
        fetch_data('Api 3')
    )

    return results

if __name__ == "__main__":

    asyncio.run(main()) 
