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


def calculate_multipliers(mods: list[dict[str, Any]]) -> tuple[float, float] :
    old_multiplier = 1.0
    new_multiplier = 1.0

    for mod in mods:
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

        # TODO: Blinds interaction
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

        # TODO: Blinds interaction
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

            new_multiplier *= new_mult
            old_multiplier *= old_mult

        # Rate mods

        if mod["acronym"] == "DT":
            if ("settings" in mod.keys() and
                "speed_change" in mod["settings"].keys()):
                rate_10: int = floor(mod["settings"]["speed_change"] * 10)

                new_mult = 1 + (rate_10/10 - 1) * 0.46
                if rate_10 != 10 and rate_10 != 15:
                    new_mult -= 0.01

                old_mult = 1 + (rate_10/10 - 1) * 0.2

                new_multiplier *= new_mult
                old_multiplier *= old_mult
            else:
                new_multiplier *= 1.23
                old_multiplier *= 1.1

        if mod["acronym"] == "HT":
            if ("settings" in mod.keys() and
                "speed_change" in mod["settings"].keys()):
                rate_10 = floor(mod["settings"]["speed_change"] * 10)
                old_mult = rate_10/10 - 0.4

                rate_20: int = floor(mod["settings"]["speed_change"] * 20)
                new_mult = rate_20/20 * 1.4 - 0.5

                new_multiplier *= new_mult
                old_multiplier *= old_mult
            else:
                new_multiplier *= 0.55
                old_multiplier *= 0.3

    return old_multiplier, new_multiplier

if __name__ == "__main__":
    main()
