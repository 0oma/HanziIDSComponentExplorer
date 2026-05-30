#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Right-panel display-character stickiness tests."""

import sys
from pathlib import Path

PLUGIN_RESOURCES = (
    Path(__file__).parent.parent
    / "HanziComponentExplorerRS+.glyphsPlugin"
    / "Contents"
    / "Resources"
)
sys.path.insert(0, str(PLUGIN_RESOURCES))

from hanzi_core import resolve_display_char  # noqa: E402


def test_explicit_char_wins_over_sticky_and_current():
    assert resolve_display_char("木", "林", "森") == "木"


def test_sticky_selection_survives_filter_refresh_without_explicit_char():
    assert resolve_display_char(None, "木", "森") == "木"


def test_current_char_is_fallback_when_no_sticky_selection():
    assert resolve_display_char(None, None, "森") == "森"


def test_none_when_no_display_context_exists():
    assert resolve_display_char(None, None, None) is None
