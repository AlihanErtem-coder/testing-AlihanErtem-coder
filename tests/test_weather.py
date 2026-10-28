"""Starter tests for the weather module.

These tests deliberately cover only ordinary examples. They show how pytest works,
but they are not a sufficient test suite for the specification in SPECIFICATION.md.
"""
import pytest
from weather import (
    average_temperature,
    filter_by_temperature,
    hottest_measurement,
    parse_measurement,
    parse_time,
)


def test_parse_time_regular_time():
    assert parse_time("14:21") == 861
    assert parse_time("23:0000") == 1380
    assert parse_time("00014:21") == 861 # führende Nullen funktionieren
    assert parse_time("00014:00021") == 861 # führende Nullen funktionieren
    with pytest.raises(AttributeError):
       parse_time(121)
    with pytest.raises(ValueError):
       parse_time("14.,.,.,.,.,,21")  # Kein Doppelpunkt
       parse_time("24:60")
       parse_time("0:32")




def test_parse_measurement_regular_line():
    assert parse_measurement("Köln;14:21;21.7") == ("Köln", 861, 21.7)
    assert parse_measurement("  Köln     ;  14:21 ; 21.7   ") == ("Köln", 861, 21.7)
    #assert parse_time("14:21") == parse_measurement("Köln;14:21;21.7")

    with pytest.raises(ValueError):
        parse_measurement(67)    # Integer
        parse_measurement("Köln;14:21;21.7; 10")  # Nicht 3 Werte
        parse_measurement("  ;14:21;21.7")   # Fehlender Wert
        parse_measurement("  Köl  n     ;  14:21 ; 21.7   ") # Leerzeichen innerhalb
        parse_measurement("Köln,14:21,21.7") # Nur Komma anstatt Semikolon
        parse_measurement ("Köln;30:21;21.7")   # parse Time macht Value Error
        parse_measurement ("Köln;14:21;21,7")   # float erwarter 21.7 deswegen kann man nicht 21,7 nutzen


def test_filter_by_temperature_regular_values():
    measurements = [
        ("Köln", 600, 10.0),
        ("Köln", 600, 10.0),
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Düsseldorf", 720, 15.0),
        ("Düsseldorf", 720, 20.0),
        ("Bonn", 900, 25.0),
    ]
    with pytest.raises(AssertionError):
        assert filter_by_temperature(measurements, 15.0, 20.0) == [
        ("Düsseldorf", 720, 18.5) , ("Düsseldorf", 720, 20.0),("Düsseldorf", 720, 15.0)] # Falsche Reihenfolge

    assert filter_by_temperature(measurements, 15.0, 20.0) == [
            ("Düsseldorf", 720, 18.5) , ("Düsseldorf", 720, 15.0), ("Düsseldorf", 720, 20.0)]
    
    assert filter_by_temperature(measurements, 9.0, 10.0) == [
                ("Köln", 600, 10.0),("Köln", 600, 10.0),("Köln", 600, 10.0)] # Muss 3 mal
    
    assert filter_by_temperature(measurements, 9.0, 10.0) == [
                    ("Köln", 600, 10.0),("Köln", 600, 10.0)] # Muss 3 mal

    


def test_average_temperature_regular_values():
    measurements = [
        ("Köln", 600, 10.0),
        ("Köln", 720, 20.0),
    ]

    assert average_temperature(measurements, "Köln") == 15.0


def test_hottest_measurement_with_unique_maximum():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 25.0),
        ("Bonn", 900, 20.0),
    ]

    assert hottest_measurement(measurements) == ("Düsseldorf", 720, 25.0)
