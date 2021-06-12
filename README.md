Mugimugi (doujinshi.org) api client

# Use
```python
    from mugimugi import MugiMugi
    async with MugiMugi(MUGIMUGI_API_KEY) as c:
        a = await c.author.get(924)
    a
```
```python
    Author(
        mugimugi_id='A924',
        id=924,
        prefix=<ElementPrefix.AUTHOR: 'A'>,
        english_name='Nakajima Yuka',
        japanese_name='なかじまゆか',
        romaji_name='ナカジマユカ',
        other_names=['かなじまゆか', 'Digital Lover'],
        _type=<Type.TYPE: <ItemType.AUTHOR: 'author'>>,
        type=<ItemType.AUTHOR: 'author'>,
        version=15,
        objects_count=490,
        parent=0,
        _links=Author.Linker(items=[
            SubContent(
                mugimugi_id='K121',
                id=121,
                prefix=<ElementPrefix.CONTENT: 'K'>,
                english_name='Stockings',
                japanese_name='ストッキング',
                romaji_name='',
                other_names=[],
                _type=<Type.TYPE: <ItemType.CONTENT: 'contents'>>,
                type=<ItemType.CONTENT: 'contents'>,
                version=1,
                objects_count=29604
            ),
            SubContent(
                mugimugi_id='K15',
                id=15,
                prefix=<ElementPrefix.CONTENT: 'K'>,
                english_name='Loli',
                japanese_name='ロリ',
                romaji_name='',
                other_names=['lolicon', 'lolikon', 'rorikon', 'ロリコン'],
                _type=<Type.TYPE: <ItemType.CONTENT: 'contents'>>,
                type=<ItemType.CONTENT: 'contents'>,
                version=3,
                objects_count=75482
            )
        ])
    )
```

# Progress

|object|get|search|
|-|-|-|
|author    |×|×|
|book      |×|×|
|character |×|×|
|circle    |×|×|
|collection| | |
|content   | | |
|convention|×|×|
|genre     | | |
|image     | | |
|imprint   | | |
|parody    |×|×|
|favorite  | | |
|publisher | | |
|type      | | |
|user      |×|-|
