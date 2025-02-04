from typing import Annotated

from fastapi import Depends

from .utils import calculate_offset


DbOffset = Annotated[int, Depends(calculate_offset)]
