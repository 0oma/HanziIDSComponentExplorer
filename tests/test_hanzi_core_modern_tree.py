#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Modern connected tree rendering tests for HanziCore.decompose."""

import sys
from pathlib import Path

PLUGIN_RESOURCES = (
    Path(__file__).parent.parent
    / "HanziComponentExplorerRS+.glyphsPlugin"
    / "Contents"
    / "Resources"
)
sys.path.insert(0, str(PLUGIN_RESOURCES))

from hanzi_core import HanziCore  # noqa: E402


def _make_core(records: dict) -> HanziCore:
    core = HanziCore.__new__(HanziCore)
    core.data_path = Path("__test_in_memory__")
    core._parsed_ids_cache = {}
    core.db = {}
    for char, data in records.items():
        core.db[char] = {
            "unicode": data.get("unicode", ""),
            "char": char,
            "ids_1": data.get("ids_1", ""),
            "ids_2": data.get("ids_2", ""),
            "strokes": data.get("strokes"),
        }
    core._build_indexes()
    return core


def test_modern_tree_connectors_are_compact_and_connected():
    core = _make_core(
        {
            "立": {"unicode": "7ACB", "ids_1": "立"},
            "田": {"unicode": "7530", "ids_1": "田"},
            "土": {"unicode": "571F", "ids_1": "土"},
            "里": {"unicode": "91CC", "ids_1": "⿱田土"},
            "童": {"unicode": "7AE5", "ids_1": "⿱立里"},
        }
    )

    lines = [tree + content for tree, content in core.decompose("童", max_depth=10)]

    assert lines == [
        "童",
        "└─ ⿱",
        "   ├─ 立",
        "   └─ 里",
        "      └─ ⿱",
        "         ├─ 田",
        "         └─ 土",
    ]


def test_modern_tree_keeps_vertical_continuation_for_non_last_sibling():
    core = _make_core(
        {
            "木": {"unicode": "6728", "ids_1": "木"},
            "火": {"unicode": "706B", "ids_1": "火"},
            "林": {"unicode": "6797", "ids_1": "⿰木木"},
            "焚": {"unicode": "711A", "ids_1": "⿱林火"},
        }
    )

    lines = [tree + content for tree, content in core.decompose("焚", max_depth=10)]

    assert "   ├─ 林" in lines
    assert "   │  └─ ⿰" in lines
    assert "   │     ├─ 木" in lines
    assert "   │     └─ 木" in lines
    assert lines[-1] == "   └─ 火"
