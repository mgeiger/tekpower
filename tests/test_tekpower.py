#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `tekpower` package."""

import pytest


from tekpower import tekpower


@pytest.fixture(scope='module')
def blank_tp3005p():
    tp = tekpower.TP3005P(None)
    yield tp


@pytest.mark.usefixtures('blank_tp3005p')
def test_tp3005p_init(blank_tp3005p):
    assert not blank_tp3005p.on, "Initialized TP3005P to On state."


@pytest.mark.usefixtures('blank_tp3005p')
def test_tp3005p_identify(blank_tp3005p):
    with pytest.raises(AttributeError):
        identify = blank_tp3005p.identify()


@pytest.mark.usefixtures('blank_tp3005p')
def test_tp3005p_status(blank_tp3005p):
    with pytest.raises(AttributeError):
        status = blank_tp3005p.status()

@pytest.mark.usefixtures('blank_tp3005p')
def test_tp3005p_output(blank_tp3005p):
    assert not blank_tp3005p.output(state=False), \
        "State should not have been set."

    with pytest.raises(AttributeError):
        blank_tp3005p.output(state=True)

@pytest.mark.usefixtures('blank_tp3005p')
def test_tp3005p_current(blank_tp3005p):
    with pytest.raises(AttributeError):
        current = blank_tp3005p.current()

@pytest.mark.usefixtures('blank_tp3005p')
def test_tp3005p_voltage(blank_tp3005p):
    with pytest.raises(AttributeError):
        voltage = blank_tp3005p.voltage()

@pytest.mark.usefixtures('blank_tp3005p')
def test_tp3005p_current_setpoint(blank_tp3005p):
    with pytest.raises(AttributeError):
        current_setpoint = blank_tp3005p.current_setpoint()

    with pytest.raises(AttributeError):
        current_setpoint = blank_tp3005p.current_setpoint(1.0)

@pytest.mark.usefixtures('blank_tp3005p')
def test_tp3005p_voltage_setpoint(blank_tp3005p):
    with pytest.raises(AttributeError):
        voltage_setpoint = blank_tp3005p.voltage_setpoint()

    with pytest.raises(AttributeError):
        voltage_setpoint = blank_tp3005p.voltage_setpoint(1.0)