Mugimugi (doujinshi.org) api client

# How to use

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


# Progress

|object|get|search|vote|cover|search(image)|
|-|-|-|-|-|-|
|author    |✓|✓|-|-|-|
|book      |✓|✓|✓|✗|✗|
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
