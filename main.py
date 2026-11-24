"""Entry for make.fun bounty: Ridiculous at First Glance, Real by the Second.

Writes one sentence (under 200 characters) pitching a bizarre startup
idea that sounds ridiculous at first glance but makes sense as a real
business, to /output/entry.txt.
"""

import os

PITCH = (
    "We sell retired subway cars to rural landowners for $15,000 each as "
    "prefab homes, because cities pay us to haul them away and buyers get "
    "hurricane-proof square footage for less than a shed."
)


def main():
    assert 1 <= len(PITCH) <= 200, "pitch must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
