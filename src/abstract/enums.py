from enum import IntEnum


class CellSize(IntEnum):
    """
    Enumeration representing cell sizes.

    Attributes:
        XXS (int): Extra Extra Small cell size. Value: 1
        XS (int): Extra Small cell size. Value: 2
        SMALL (int): Small cell size. Value: 3
        MEDIUM (int): Medium cell size. Value: 20
        LARGE (int): Large cell size. Value: 100
        XL (int): Extra Large cell size. Value: 255
        XXL (int): Extra Extra Large cell size. Value: 500
        XXXL (int): Extra Extra Extra Large cell size. Value: 10485760
    """

    XXS = 1
    XS = 2
    SMALL = 3
    MEDIUM = 20
    LARGE = 100
    XL = 255
    XXL = 500
    XXXL = 10485760
