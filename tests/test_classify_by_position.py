#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Position-aware grouping tests ported from the upstream v1.2 feature concept."""

import sys
from pathlib import Path

PLUGIN_RESOURCES = (
    Path(__file__).parent.parent
    / "HanziComponentExplorerRSplus.glyphsPlugin"
    / "Contents"
    / "Resources"
)
sys.path.insert(0, str(PLUGIN_RESOURCES))

from hanzi_core import (  # noqa: E402
    HanziCore,
    MULTI_POSITION_MARKER,
    NESTED_POSITION_MARKER,
    UNCLASSIFIED_LABEL,
    _split_top_operands,
)


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


def test_split_top_operands_preserves_nested_subtrees():
    tokens = ["⿰", "氵", "⿱", "日", "月"]
    assert _split_top_operands(tokens) == [["氵"], ["⿱", "日", "月"]]


def test_classify_direct_positions_are_individual_for_symmetric_operands():
    core = _make_core(
        {
            "木": {"ids_1": "木"},
            "林": {"ids_1": "⿰木木"},
            "沐": {"ids_1": "⿰氵木"},
            "休": {"ids_1": "⿰亻木"},
        }
    )

    assert core.classify_by_position("木", "沐") == "⿰2"
    assert core.classify_by_position("木", "休") == "⿰2"
    assert core.classify_by_position("木", "林") == f"⿰{MULTI_POSITION_MARKER}"


def test_classify_nested_position_uses_dot_suffix():
    core = _make_core(
        {
            "木": {"ids_1": "木"},
            "林": {"ids_1": "⿰木木"},
            "淋": {"ids_1": "⿰氵林"},
            "焚": {"ids_1": "⿱林火"},
        }
    )

    assert core.classify_by_position("木", "淋") == f"⿰2{NESTED_POSITION_MARKER}"
    assert core.classify_by_position("木", "焚") == f"⿱1{NESTED_POSITION_MARKER}"


def test_group_by_position_sorts_direct_before_nested_and_unclassified_last():
    core = _make_core(
        {
            "木": {"ids_1": "木"},
            "林": {"ids_1": "⿰木木"},
            "沐": {"ids_1": "⿰氵木"},
            "村": {"ids_1": "⿰木寸"},
            "淋": {"ids_1": "⿰氵林"},
            "本": {"ids_1": "本"},
        }
    )

    grouped = core.group_by_position("木", ["淋", "沐", "本", "村", "林"])

    assert list(grouped) == ["⿰1", "⿰2", f"⿰{MULTI_POSITION_MARKER}", f"⿰2{NESTED_POSITION_MARKER}", UNCLASSIFIED_LABEL]
    assert grouped["⿰1"] == ["村"]
    assert grouped["⿰2"] == ["沐"]
    assert grouped[f"⿰{MULTI_POSITION_MARKER}"] == ["林"]
    assert grouped[f"⿰2{NESTED_POSITION_MARKER}"] == ["淋"]
    assert grouped[UNCLASSIFIED_LABEL] == ["本"]


def test_compose_immediate_component_lines_and_coarse_idc_grouping():
    core = _make_core(
        {
            "木": {"ids_1": "木"},
            "林": {"ids_1": "⿰木木"},
            "沐": {"ids_1": "⿰氵木"},
            "森": {"ids_1": "⿱木林"},
        }
    )

    assert core.compose_immediate_component_lines("木", ["沐", "森"]) == [
        "⿰2 沐",
        "⿱1 森",
    ]
    assert core.compose_immediate_component_lines("木", ["沐", "林"], coarse_by_idc=True) == [
        "⿰ 沐林",
    ]
