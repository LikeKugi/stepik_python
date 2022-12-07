import asyncio

import aiohttp

from Learning.Python.multiprocessing.decorators import async_measure_time


class Photo:
    def __init__(self, album_id, photo_id, title, url, thumbnail_url):
        self.thumbnail_url = thumbnail_url
        self.url = url
        self.title = title
        self.photo_id = photo_id
        self.album_id = album_id

    @classmethod
    def from_json(cls, obj):
        return Photo(obj.get('albumId'), obj.get('id'), obj['title'], obj['url'], obj.get('thumbnailUrl', 'null'))


def print_photo_titles(photos):
    for photo in photos:
        print(f'{photo.title}', end='\n')


async def photos_by_album(task_name, album, session):
    print(f'{task_name=}')
    url = f'https://jsonplaceholder.typicode.com/photos?albumId={album}'

    response = await session.get(url)
    photos_json = await response.json()

    return [Photo.from_json(photo) for photo in photos_json]


@async_measure_time
async def single_response():
    async with aiohttp.ClientSession() as session:
        photos = await photos_by_album('Task 1', 3, session)
        print_photo_titles(photos)


@async_measure_time
async def couple_responses():
    async with aiohttp.ClientSession() as session:
        photos_in_albums = await asyncio.gather(*(photos_by_album(f'Task {i + 1}', album, session)
                                                  for i, album in enumerate(range(2, 30))))

        photos_count = sum([len(cur) for cur in photos_in_albums])
        print(f'total count: {photos_count}')


async def main():
    await single_response()
    await couple_responses()


if __name__ == '__main__':
    asyncio.run(main())
