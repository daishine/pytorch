from torch._C import FileCheck as FileCheck
from ._comparison import (
    assert_allclose,
    assert_close as assert_close,
    assert_not_close as assert_not_close,
)
from ._creation import make_tensor as make_tensor
