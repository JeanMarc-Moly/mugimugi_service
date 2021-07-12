Mugimugi (doujinshi.org) services client

# How to use

## Context
It is possible not to use `MugiMugi` as context, but it is advised if you have many queries to make.

Will work
```python
from mugimugi_client_api import MugiMugi
print(await MugiMugi(MUGIMUGI_API_KEY).author.get(924))
```
when you got a lot
```python
from mugimugi_service import MugiMugi
from datetime import date, timedelta

# Get last hundred days worth of conventions.
async with MugiMugi(MUGIMUGI_API_KEY) as c:
    today = date.today()
    for offset in range(100):
        day = today - timedelta(days=offset)
        async for cv in c.convention.search(date_=day):
            print(list(cv.names))
```
## Get authors by ID
```python
from mugimugi_client_api import MugiMugi
async with MugiMugi(MUGIMUGI_API_KEY) as c:
    print(await c.author.get(924))
```
```python
Author(
    english_name='Nakajima Yuka',
    japanese_name='なかじまゆか',
    katakana_name='ナカジマユカ',
    other_names=['かなじまゆか', 'Digital Lover'],
    version=15,
    objects_count=490,
    parent=0,
    _id='A924',
    _type=<Type.TYPE: <ItemType.AUTHOR: 'author'>>,
    _links=Author.Linker(items=[
        SubContent(
            english_name='Stockings',
            japanese_name='ストッキング',
            katakana_name='',
            other_names=[],
            version=1,
            objects_count=29604
            _id='K121',
            _type=<Type.TYPE: <ItemType.CONTENT: 'contents'>>,
        ),
        SubContent(
            english_name='Loli',
            japanese_name='ロリ',
            katakana_name='',
            other_names=['lolicon', 'lolikon', 'rorikon', 'ロリコン'],
            version=3,
            objects_count=75482
            _id='K15',
            _type=<Type.TYPE: <ItemType.CONTENT: 'contents'>>,
        )
    ])
)
```

## Get characters by ID
```python
from mugimugi_service import MugiMugi
async with MugiMugi(MUGIMUGI_API_KEY) as c:
    async for char in c.character.get(list(range(10))):
        print(list(char.names))
```
```python
['不詳', '(unknown)']
['ヴィータ', 'ヴィータ', 'Vita']
['フェイト・テスタロッサ', 'フェイトテスタロッサ', 'Fate Testarossa', 'フェイト・T・ハラオウン', 'Fate T. Harlaown']
['高町なのは', 'タカマチナノハ', 'Takamachi Nanoha']
['八神はやて', 'ヤガミハヤテ', 'Yagami Hayate']
['九重りん', 'ココノエリン', 'Kokonoe Rin']
['鏡黒', 'カガミクロ', 'Kagami Kuro']
['宇佐美々', 'ウサミミ', 'Usa Mimi']
['クー', 'クー', 'Kooh']
```

## Search convention by date
```python
from mugimugi_service import MugiMugi
async with MugiMugi(MUGIMUGI_API_KEY) as c:
    async for cv in c.convention.search(date_=date(2018,12,31)):
        print(list(cv.names))
```
```python
['コミックマーケット95', 'コミックマーケット95', 'Comic Market 95', 'C95', 'Comiket 95', 'Komike 95', 'コミケ95', 'コミケット95']
```

## Get books covers
```python
from mugimugi_service import MugiMugi
MugiMugi(MUGIMUGI_API_KEY).book.get_cover(100)
```
Will return the raw bytes of the image.
```python
from mugimugi_service import MugiMugi
from io import BytesIO
from PIL.Image import open

async for id_, raw in MugiMugi(MUGIMUGI_API_KEY).book.get_covers(range(10,15)):
    open(BytesIO(raw)).save(f"{id_}.jpg")
```
Can be fed to pillow for modifications.
## Save books covers
```python
from mugimugi_service import MugiMugi
await MugiMugi(MUGIMUGI_API_KEY).book.save_cover(101, "test")
```
```python
PosixPath('/dev/mugimugi/service/test.jpg')
```
```python
covers = ((10, "the tenth"),(15, "15"))
from mugimugi_service import MugiMugi
async for id_, path in MugiMugi(MUGIMUGI_API_KEY).book.save_covers(covers):
    print(f"{id_}: {path}")
```
```shell
10: /dev/mugimugi/service/the tenth.jpg
15: /dev/mugimugi/service/15.jpg
```


# Progress

|object|get|search|vote|cover|search(image)|
|-|-|-|-|-|-|
|author    |✓|✓|-|-|-|
|book      |✓|✓|✓|✓|✗|
|character |✓|✓|-|-|-|
|circle    |✓|✓|-|-|-|
|collection|✓|✓|-|-|-|
|content   |✓|✓|-|-|-|
|convention|✓|✓|-|-|-|
|genre     |✓|✓|-|-|-|
|imprint   |✓|✓|-|-|-|
|parody    |✓|✓|-|-|-|
|publisher |✓|✓|-|-|-|
|user      |✓|-|-|-|-|
