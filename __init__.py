# -*- coding: utf-8 -*-
from .sj_yasuo import NODE_CLASS_MAPPINGS as _m1, NODE_DISPLAY_NAME_MAPPINGS as _n1
from .sj_lm_yasuo import NODE_CLASS_MAPPINGS as _m2, NODE_DISPLAY_NAME_MAPPINGS as _n2
from .sj_caijian import NODE_CLASS_MAPPINGS as _m3, NODE_DISPLAY_NAME_MAPPINGS as _n3
from .sj_fugai import NODE_CLASS_MAPPINGS as _m4, NODE_DISPLAY_NAME_MAPPINGS as _n4
from .sj_baocun import NODE_CLASS_MAPPINGS as _m5, NODE_DISPLAY_NAME_MAPPINGS as _n5
from .sj_wenben import NODE_CLASS_MAPPINGS as _m6, NODE_DISPLAY_NAME_MAPPINGS as _n6

NODE_CLASS_MAPPINGS = {**_m1, **_m2, **_m3, **_m4, **_m5, **_m6}
NODE_DISPLAY_NAME_MAPPINGS = {**_n1, **_n2, **_n3, **_n4, **_n5, **_n6}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]