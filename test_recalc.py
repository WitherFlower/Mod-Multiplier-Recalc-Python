from json import JSONDecoder
from typing import Any
from pytest import approx

from main import calculate_multipliers

def test_ez():
    decoder = JSONDecoder()
    input = """
    [
        {
            "acronym": "EZ"
        }
    ]
    """
    mods: list[dict[str, Any]] = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == (0.5, 0.8))
    input = """
    [
        {
            "acronym": "EZ",
            "settings": { "retries": 3 }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((0.5, 0.7)))
    input = """
    [
        {
            "acronym": "EZ",
            "settings": { "retries": 10 }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == (0.5, 0.4))

def test_cl():
    input = """
    [
        {
            "acronym": "CL"
        }
    ]
    """
    decoder = JSONDecoder()
    mods: list[dict[str, Any]] = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == (0.96, 0.985))
    input = """
    [
        {
            "acronym": "CL",
            "settings": { "classic_note_lock": true }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == (0.96, 0.985))
    input = """
    [
        {
            "acronym": "CL",
            "settings": { "classic_note_lock": false }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == (0.96, 0.96))

def test_hdcomplex():
    decoder = JSONDecoder()
    input = """
    [
        {
            "acronym": "HD",
            "settings": { "only_fade_approach_circles": true }
        },
        {
            "acronym": "WG"
        }
    ]
    """
    mods: list[dict[str, Any]] = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == (1, 1))
    input = """
    [
        {
            "acronym": "HD",
            "settings": { "only_fade_approach_circles": true }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == (1, 1.02))

def test_hd_visual_indications():
    decoder = JSONDecoder()
    input = """
    [
        {
            "acronym": "HD"
        },
        {
            "acronym": "WG"
        }
    ]
    """
    mods: list[dict[str, Any]] = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == (1.06, 1.02))
    input = """
    [
        {
            "acronym": "HD"
        },
        {
            "acronym": "GR"
        },
        {
            "acronym": "DF"
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == (1.06, 1.02))

def test_hd():
    input = """
    [
        {
            "acronym": "HD"
        }
    ]
    """
    decoder = JSONDecoder()
    mods: list[dict[str, Any]] = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == (1.06, 1.04))

def test_hr():
    input = """
    [
        {
            "acronym": "HR"
        }
    ]
    """
    decoder = JSONDecoder()
    mods: list[dict[str, Any]] = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == (1.06, 1.09))

def test_tc():
    input = """
    [
        {
            "acronym": "TC"
        }
    ]
    """
    decoder = JSONDecoder()
    mods: list[dict[str, Any]] = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == (1.0, 1.02))

def test_fl():
    decoder = JSONDecoder()
    mods: list[dict[str, Any]]
    input = """
    [
        {
            "acronym": "FL"
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((1.12, 1.2)))
    input = """
    [
        {
            "acronym": "FL"
        },
        {
            "acronym": "FR"
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((1.12, 1.1)))
    input = """
    [
        {
            "acronym": "FL",
            "settings": { "combo_based_size": false }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((1.0, 1.04)))
    input = """
    [
        {
            "acronym": "FL",
            "settings": { "size_multiplier": 2 }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((1.0, 1.02)))
    input = """
    [
        {
            "acronym": "FL",
            "settings": { "size_multiplier": 2, "combo_based_size": false }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((1.0, 1.004)))

def test_bl():
    decoder = JSONDecoder()
    input = """
    [
        {
            "acronym": "BL"
        }
    ]
    """
    mods: list[dict[str, Any]] = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((1.12, 1.24)))
    input = """
    [
        {
            "acronym": "BL"
        },
        {
            "acronym": "HD"
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((1.06 * 1.12, 1.24)))
    input = """
    [
        {
            "acronym": "BL"
        },
        {
            "acronym": "TC"
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((1.12, 1.24)))

def test_hdnchr():
    input = """
    [
        {
            "acronym": "HD"
        },
        {
            "acronym": "NC"
        },
        {
            "acronym": "HR"
        }
    ]
    """
    decoder = JSONDecoder()
    mods: list[dict[str, Any]] = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((1.06 ** 2 * 1.1, 1.04 * 1.09 * 1.23)))

def test_hddthr():
    input = """
    [
        {
            "acronym": "HD"
        },
        {
            "acronym": "DT"
        },
        {
            "acronym": "HR"
        }
    ]
    """
    decoder = JSONDecoder()
    mods: list[dict[str, Any]] = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((1.06 ** 2 * 1.1, 1.04 * 1.09 * 1.23)))

def test_hdhr():
    input = """
    [
        {
            "acronym": "HD"
        },
        {
            "acronym": "HR"
        }
    ]
    """
    decoder = JSONDecoder()
    mods: list[dict[str, Any]] = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((1.06 ** 2, 1.04 * 1.09)))

def test_dt1_01():
    input = """
    [
        {
            "acronym": "DT",
            "settings": { "speed_change": 1.01 }
        }
    ]
    """
    decoder = JSONDecoder()
    mods: list[dict[str, Any]] = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == (1, 1))

def test_ht():
    input = """
    [
        {
            "acronym": "HT"
        }
    ]
    """
    decoder = JSONDecoder()
    mods: list[dict[str, Any]] = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((0.3, 0.55)))
    input = """
    [
        {
            "acronym": "HT",
            "settings": { "speed_change": 0.5 }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((0.1, 0.2)))
    input = """
    [
        {
            "acronym": "HT",
            "settings": { "speed_change": 0.94 }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((0.5, 0.76)))
    input = """
    [
        {
            "acronym": "HT",
            "settings": { "speed_change": 0.99 }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((0.5, 0.83)))

def test_dc():
    input = """
    [
        {
            "acronym": "DC"
        }
    ]
    """
    decoder = JSONDecoder()
    mods: list[dict[str, Any]] = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((0.3, 0.55)))
    input = """
    [
        {
            "acronym": "DC",
            "settings": { "speed_change": 0.5 }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((0.1, 0.2)))
    input = """
    [
        {
            "acronym": "DC",
            "settings": { "speed_change": 0.94 }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((0.5, 0.76)))
    input = """
    [
        {
            "acronym": "DC",
            "settings": { "speed_change": 0.99 }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((0.5, 0.83)))

def test_wu_wd():
    decoder = JSONDecoder()
    mods: list[dict[str, Any]]
    input = """
    [
        {
            "acronym": "WU",
            "settings": { "initial_rate": 1.2, "final_rate": 1.7 }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((0.5, 1.128)))
    input = """
    [
        {
            "acronym": "WD",
            "settings": { "initial_rate": 1.7, "final_rate": 1.2 }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((0.5, 1.128)))
    input = """
    [
        {
            "acronym": "WD",
            "settings": { "initial_rate": 0.9, "final_rate": 0.7 }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((0.5, 0.536)))
    input = """
    [
        {
            "acronym": "WD",
            "settings": { "initial_rate": 0.5, "final_rate": 0.51 }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((0.5, 0.2)))

def test_dt():
    input = """
    [
        {
            "acronym": "DT"
        }
    ]
    """
    decoder = JSONDecoder()
    mods: list[dict[str, Any]] = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == (1.1, 1.23))
    input = """
    [
        {
            "acronym": "DT",
            "settings": { "speed_change": 2 }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == (1.2, 1.45))

def test_nc():
    input = """
    [
        {
            "acronym": "NC"
        }
    ]
    """
    decoder = JSONDecoder()
    mods: list[dict[str, Any]] = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == (1.1, 1.23))
    input = """
    [
        {
            "acronym": "NC",
            "settings": { "speed_change": 2 }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == (1.2, 1.45))

def test_da():
    decoder = JSONDecoder()
    mods: list[dict[str, Any]]
    input = """
    [
        {
            "acronym": "DA",
            "settings": { "circle_size": 3.5, "approach_rate": 9.5 }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods, cs=4, hp=5, od=9, ar=9.2) == approx((0.5, 0.6375)))
    input = """
    [
        {
            "acronym": "DA",
            "settings": { "circle_size": 0, "approach_rate": 0 }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods, cs=4, hp=5, od=9, ar=9.2) == approx((0.5, 0.1)))

def test_fun_and_stuff():
    decoder = JSONDecoder()
    mods: list[dict[str, Any]]
    input = """
    [
        {
            "acronym": "SY"
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == (0.8, 0.99))
    input = """
    [
        {
            "acronym": "AD"
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == (1.0, 0.7))
    input = """
    [
        {
            "acronym": "MG"
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == approx((0.5, 0.4)))
    input = """
    [
        {
            "acronym": "AS"
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == (0.5, 0.1))
    input = """
    [
        {
            "acronym": "TP"
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == (0.1, 0.01))
    input = """
    [
        {
            "acronym": "DF",
            "settings": { "start_scale": 4 }
        }
    ]
    """
    mods = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    assert(calculate_multipliers(mods) == (1.0, 0.96))

