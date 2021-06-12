from mugimugi.enum import ElementNode


class AbstractLinker:
    class Meta:
        name = ElementNode.LINK.value

    items: list
