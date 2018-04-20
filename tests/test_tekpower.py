#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `tekpower` package."""

import pytest


from tekpower import tekpower


def test_tp3005p():
    tp3005p = tekpower.TP3005P(None)
    
