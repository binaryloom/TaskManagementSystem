from enum import IntEnum, StrEnum



class CellSize(IntEnum):
    """This enum return the cell size of a attribute.

    Usages:
        CellSize.XXS: 1
        CellSize.XS: 2
        CellSize.SMALL: 3
        CellSize.MEDIUM: 20
        CellSize.XM: 50
        CellSize.LARGE: 100
        CellSize.XL: 255
        CellSize.XXL: 500
        CellSize.XXXL: 1000
        CellSize.EXTRAXL: 10000
        CellSize.EXTRAXXL: 100000
        CellSize.EXTRAXXXL = 10485760
    """

    XXS = 1
    XS = 2
    SMALL = 3
    MEDIUM = 20
    XM = 50
    LARGE = 100
    XL = 255
    XXL = 500
    XXXL = 1000
    EXTRAXL = 10000
    EXTRAXXL = 100000
    EXTRAXXXL = 10485760