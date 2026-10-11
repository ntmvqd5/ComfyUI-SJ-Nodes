# -*- coding: utf-8 -*-
import importlib.util
import os

def _load_pkg(name, rel):
    p = os.path.join(os.path.dirname(__file__), rel, "nodes.py")
    spec = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

_m1 = _load_pkg("sj_yasuo_nodes", "shunjing_yasuo")
_m2 = _load_pkg("sj_lm_yasuo_nodes", "shunjing-LM-yasuo")
_m3 = _load_pkg("sj_baocun_nodes", "sj_baocun")

NODE_CLASS_MAPPINGS = {}
NODE_CLASS_MAPPINGS.update(_m1.NODE_CLASS_MAPPINGS)
NODE_CLASS_MAPPINGS.update(_m2.NODE_CLASS_MAPPINGS)
NODE_CLASS_MAPPINGS.update(_m3.NODE_CLASS_MAPPINGS)

NODE_DISPLAY_NAME_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS.update(_m1.NODE_DISPLAY_NAME_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(_m2.NODE_DISPLAY_NAME_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(_m3.NODE_DISPLAY_NAME_MAPPINGS)

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
