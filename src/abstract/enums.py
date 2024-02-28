from enum import IntEnum


class CellSize(IntEnum):
    """This enum return the cell size of a attribute.

    Usages:
        CellSize.XXS: 1
        CellSize.XS: 2
        CellSize.SMALL: 3
        CellSize.MEDIUM: 20
        CellSize.LARGE: 100
        CellSize.XL: 255
        CellSize.XXL: 500
        CellSize.XXXL: 10485760
    """

    XXS = 1
    XS = 2
    SMALL = 3
    MEDIUM = 20
    LARGE = 100
    XL = 255
    XXL = 500
    XXXL = 10485760
