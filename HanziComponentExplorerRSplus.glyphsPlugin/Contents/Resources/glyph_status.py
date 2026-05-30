#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared glyph/tile status helpers for the GUI+ fork.

Fork modifications copyright © 2026 Ooma Kobayashi.
Modified from the original upstream project where applicable.

This module intentionally has no GlyphsApp/AppKit dependency. The UI layer passes
raw adapter status dictionaries in, and this module normalizes markers/counts so
status logic stays consistent across result rows, summary text, text fallback, and
object tiles.
"""

from __future__ import division, print_function, unicode_literals

STATUS_DESIGNED = "designed"
STATUS_EXISTS = "exists"
STATUS_MISSING = "missing"
STATUS_FAVORITE = "favorite"

STATUS_ORDER = (STATUS_DESIGNED, STATUS_EXISTS, STATUS_MISSING)
STATUS_MARKERS = {
    STATUS_DESIGNED: "●",
    STATUS_EXISTS: "○",
    STATUS_MISSING: "–",
    STATUS_FAVORITE: "★",
}


def status_key_from_raw(raw_status):
    """Return the canonical status key from an adapter status dictionary."""
    raw_status = raw_status or {}
    try:
        if raw_status.get("designed"):
            return STATUS_DESIGNED
        if raw_status.get("exists"):
            return STATUS_EXISTS
    except Exception:
        pass
    return STATUS_MISSING


def status_payload(char, raw_status=None, favorite=False):
    """Return a normalized status payload for one tile/list character."""
    key = status_key_from_raw(raw_status)
    marker = STATUS_MARKERS[STATUS_FAVORITE] if favorite else STATUS_MARKERS.get(key, "–")
    return {
        "char": char,
        "status": key,
        "marker": marker,
        "favorite": bool(favorite),
        "exists": key in (STATUS_DESIGNED, STATUS_EXISTS),
        "designed": key == STATUS_DESIGNED,
    }


def empty_counts():
    return {"total": 0, STATUS_DESIGNED: 0, STATUS_EXISTS: 0, STATUS_MISSING: 0, STATUS_FAVORITE: 0}


def count_statuses(chars, raw_status_provider, favorites=None):
    """Count canonical glyph statuses for unique visible characters."""
    favorites = set(favorites or [])
    counts = empty_counts()
    seen = set()
    for ch in chars or "":
        if not ch or ch in seen:
            continue
        seen.add(ch)
        counts["total"] += 1
        if ch in favorites:
            counts[STATUS_FAVORITE] += 1
        payload = status_payload(ch, raw_status_provider(ch), ch in favorites)
        counts[payload["status"]] += 1
    return counts


def designed_percent(counts):
    total = counts.get("total", 0) or 0
    if not total:
        return 0
    return int(round((counts.get(STATUS_DESIGNED, 0) / float(total)) * 100))


def unique_related_chars(text, is_valid_char):
    """Extract unique real characters from the canonical right-pane text.

    Group labels and separator lines are intentionally ignored.
    """
    seen = set()
    chars = []
    for raw_line in (text or "").splitlines():
        line = raw_line.strip()
        if not line or set(line) == {"-"}:
            continue
        payload = line.split(" ", 1)[1] if " " in line else line
        for ch in payload:
            try:
                if is_valid_char(ch) and ch not in seen:
                    seen.add(ch)
                    chars.append(ch)
            except Exception:
                pass
    return "".join(chars)
