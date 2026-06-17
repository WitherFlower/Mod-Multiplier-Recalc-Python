from json import JSONDecoder
from math import floor
from operator import contains
from typing import Any

input = """
[
    {
        "acronym": "HD"
    },
    {
        "acronym": "DT",
        "speed_change": 1.2
    }
]
"""

def main():
    decoder = JSONDecoder()
    mods: list[dict[str, Any]] = list()
    for mod_dict in decoder.decode(input):
        mods.append(mod_dict)
    print(calculate_multipliers(mods))


def calculate_multipliers(mods: list[dict[str, Any]], cs: float = 0, ar: float = 0, od: float = 0, hp: float = 0) -> tuple[float, float] :
    old_multiplier = 1.0
    new_multiplier = 1.0

    for mod in mods:

        # Difficulty decrease

        if mod["acronym"] == "EZ":
            old_multiplier *= 0.5
            if ("settings" in mod.keys() and
                "retries" in mod["settings"].keys()):
                retries = mod["settings"]["retries"]
                DEFAULT_RETRIES = 2
                new_multiplier *= max(0.4, 0.8 - max(0, 0.1 * (retries - DEFAULT_RETRIES)))
            else:
                new_multiplier *= 0.8

        if mod["acronym"] == "CL":
            old_multiplier *= 0.96
            if ("settings" in mod.keys() and
                "classic_note_lock" in mod["settings"].keys() and
                mod["settings"]["classic_note_lock"] == False):
                new_multiplier *= 0.96
            else:
                new_multiplier *= 0.985

        # Difficulty increase

        if mod["acronym"] == "HD":
            old_mult = 1.06
            new_mult = 1.04
            if ("settings" in mod.keys() and
                "only_fade_approach_circles" in mod["settings"].keys() and
                mod["settings"]["only_fade_approach_circles"] == True):
                    old_mult = 1
                    new_mult -= 0.02
            if (len(list(filter(lambda x:
                                x["acronym"] == "WG" or
                                x["acronym"] == "GR" or
                                x["acronym"] == "DF" or
                                x["acronym"] == "RP" or
                                x["acronym"] == "DP",
                                mods))) > 0):
                    new_mult -= 0.02
            if (new_mult < 1):
                new_mult = 1
            if (len(list(filter(lambda x: x["acronym"] == "BL", mods))) > 0):
                new_mult = 1
            new_multiplier *= new_mult
            old_multiplier *= old_mult

        if mod["acronym"] == "HR":
            old_multiplier *= 1.06
            new_multiplier *= 1.09

        if mod["acronym"] == "TC":
            new_mult = 1.02
            if (len(list(filter(lambda x: x["acronym"] == "BL", mods))) > 0):
                new_mult = 1
            new_multiplier *= new_mult

        if mod["acronym"] == "BL":
            old_multiplier *= 1.12
            new_multiplier *= 1.24

        # TODO: Freeze Frame interaction :
        #       Combination<OsuModFlashlight, OsuModFreezeFrame>(hasMultiplier: (flashlight, _) =>
        #           1 + (flashlightMultiplier(flashlight) - 1) / 2);
        if mod["acronym"] == "FL":
            old_mult = 1.12
            new_mult = 1.2

            if ("settings" in mod.keys() and
                "size_multiplier" in mod["settings"].keys()):
                size = mod["settings"]["size_multiplier"]
                new_mult = max(1.02, min(1.2, 1.2 - 0.2 * (size - 1)))
                old_mult = 1

            if ("settings" in mod.keys() and
                "combo_based_size" in mod["settings"].keys() and
                mod["settings"]["combo_based_size"] == False):
                new_mult = 1 + (new_mult - 1) / 5
                old_mult = 1

            if (len(list(filter(lambda x: x["acronym"] == "FR", mods))) > 0):
                new_mult = 1 + (new_mult - 1) / 2

            new_multiplier *= new_mult
            old_multiplier *= old_mult

        # Rate mods

        def new_dt_mult(rate: float):
            rate_10: int = floor(rate * 10)
            new_mult = 1 + (rate_10/10 - 1) * 0.46
            if rate_10 != 10 and rate_10 != 15:
                new_mult -= 0.01
            return new_mult

        if mod["acronym"] == "DT":
            if ("settings" in mod.keys() and
                "speed_change" in mod["settings"].keys()):

                rate = mod["settings"]["speed_change"]
                rate_10: int = floor(rate * 10)

                new_mult = new_dt_mult(rate)
                old_mult = 1 + (rate_10/10 - 1) * 0.2

                new_multiplier *= new_mult
                old_multiplier *= old_mult
            else:
                new_multiplier *= 1.23
                old_multiplier *= 1.1

        def new_ht_mult(rate: float):
            rate_20: int = floor(rate * 20)
            new_mult = rate_20/20 * 1.4 - 0.5
            return new_mult

        if mod["acronym"] == "HT":
            if ("settings" in mod.keys() and
                "speed_change" in mod["settings"].keys()):
                rate_10 = floor(mod["settings"]["speed_change"] * 10)
                old_mult = rate_10/10 - 0.4

                rate = mod["settings"]["speed_change"]
                new_multiplier *= new_ht_mult(rate)
                old_multiplier *= old_mult
            else:
                new_multiplier *= 0.55
                old_multiplier *= 0.3

        if mod["acronym"] == "WU":
            initial_rate = 1
            final_rate = 1.5
            if ("settings" in mod.keys() and
                "initial_rate" in mod["settings"].keys()):
                initial_rate = mod["settings"]["initial_rate"]
            if ("settings" in mod.keys() and
                "final_rate" in mod["settings"].keys()):
                final_rate = mod["settings"]["final_rate"]
            max_rate = max(initial_rate, final_rate)
            min_rate = min(initial_rate, final_rate)
            min_mult = new_ht_mult(min_rate) if min_rate < 1 else new_dt_mult(min_rate)
            max_mult = new_ht_mult(max_rate) if max_rate < 1 else new_dt_mult(max_rate)
            old_multiplier = 0.5
            new_multiplier = 0.8 * min_mult + 0.2 * max_mult

        if mod["acronym"] == "WD":
            initial_rate = 1
            final_rate = 0.75
            if ("settings" in mod.keys() and
                "initial_rate" in mod["settings"].keys()):
                initial_rate = mod["settings"]["initial_rate"]
            if ("settings" in mod.keys() and
                "final_rate" in mod["settings"].keys()):
                final_rate = mod["settings"]["final_rate"]
            max_rate = max(initial_rate, final_rate)
            min_rate = min(initial_rate, final_rate)
            min_mult = new_ht_mult(min_rate) if min_rate < 1 else new_dt_mult(min_rate)
            max_mult = new_ht_mult(max_rate) if max_rate < 1 else new_dt_mult(max_rate)
            old_multiplier = 0.5
            new_multiplier = 0.8 * min_mult + 0.2 * max_mult

        # Conversion

        if mod["acronym"] == "TP":
            old_multiplier *= 0.1
            new_multiplier *= 0.01

        if mod["acronym"] == "RD":
            new_multiplier *= 0.7

        if mod["acronym"] == "DA":
            new_mult = 1
            if ("settings" in mod.keys() and
                "circle_size" in mod["settings"].keys()):
                new_mult *= max(0.1, 1 - 0.5 * abs(cs - mod["settings"]["circle_size"]))
                print(new_mult)
            if ("settings" in mod.keys() and
                "approach_rate" in mod["settings"].keys()):
                new_mult *= max(0.1, 1 - 0.5 * abs(ar - mod["settings"]["approach_rate"]))
                print(new_mult)
            if ("settings" in mod.keys() and
                "overall_difficulty" in mod["settings"].keys()):
                new_mult *= max(0.1, 1 - 0.5 * abs(od - mod["settings"]["overall_difficulty"]))
                print(new_mult)
            if ("settings" in mod.keys() and
                "drain_rate" in mod["settings"].keys()):
                new_mult *= max(0.1, 1 - 0.5 * abs(hp - mod["settings"]["drain_rate"]))
                print(new_mult)

            new_multiplier *= max(new_mult, 0.1)
            old_multiplier *= 0.5

        # Fun

        if mod["acronym"] == "DF":
            if ("settings" in mod.keys() and
                "start_scale" in mod["settings"].keys()):
                new_multiplier *= (1 - max(0, 0.02 * (mod["settings"]["start_scale"] - 2)))

        if mod["acronym"] == "AD":
            new_multiplier *= 0.7

        if mod["acronym"] == "AS":
            old_multiplier *= 0.5
            new_multiplier *= 0.1

        if mod["acronym"] == "SY":
            old_multiplier *= 0.8
            new_multiplier *= 0.99

        if mod["acronym"] == "MG":
            attraction_strength = 0.5
            if ("settings" in mod.keys() and
                "attraction_strength" in mod["settings"].keys()):
                attraction_strength = mod["settings"]["attraction_strength"]
            old_multiplier *= 0.5
            new_multiplier *= (0.7 - attraction_strength * 0.6)

    return old_multiplier, new_multiplier

if __name__ == "__main__":
    main()
