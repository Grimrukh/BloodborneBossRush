"""Modify Bloodborne `MSGDirectory` to rename warp destination names and add new prompts."""
import os
from pathlib import Path

from soulstruct.bloodborne.text import MSGDirectory
from soulstruct.config import BB_PATH


VERSION = "Version 2021-05-19 16:02"


NEW_EVENT_TEXT = {
    70002201: "Witch of Hemwick",  # Witch's Abode
    70002301: "Blood-starved Beast",  # Church of the Good Chalice
    70002302: "Darkbeast Paarl",  # Graveyard of the Darkbeast
    70002401: "Vicar Amelia",  # Grand Cathedral
    70002412: "Cleric Beast",  # Great Bridge
    70002413: "Father Gascoigne",  # Tomb of Oedon
    70002421: "Ebrietas, Daughter of the Cosmos",  # Altar of Despair
    70002422: "Celestial Emissary",  # Lumenflower Gardens
    70002502: "Martyr Logarius",  # Logarius' Seat
    70002601: "Mergo's Wet Nurse",  # Wet Nurse's Lunarium
    70002602: "Micolash, Host of the Nightmare",  # Mergo's Loft: Middle
    70002701: "Shadows of Yharnam",  # Forbidden Grave
    70002801: "The One Reborn",  # Advent Plaza
    70003202: "Rom, the Vacuous Spider",  # Moonside Lake
    70003301: "Amygdala",  # Amygdala's Chamber
    70003402: "Ludwig, the Holy Blade",  # Underground Corpse Pile
    70003403: "Laurence, the First Vicar",  # Nightmare Grand Cathedral
    70003501: "Living Failures",  # Lumenwood Garden
    70003502: "Lady Maria of the Astral Clocktower",  # Astral Clocktower
    70003602: "Orphan of Kos",  # Coast

    80000: VERSION,
    80001: "Challenge Gehrman, the First Hunter",
    80002: "Challenge Moon Presence",

    70011000: "Face next foe",  # replaces "Light Lamp" (ActionButtonParam 6100)
}


NEW_GEM_TEXT = {
    4419: ("Edged Blood Gem", "+18% slash damage", "Adds +18% to slash damage."),
    4420: ("Blunt Blood Gem", "+18% blunt damage", "Adds +18% to blunt damage."),
    4421: ("Sharp Blood Gem", "+18% thrust damage", "Adds +18% to thrust damage."),
    4422: ("Explosive Blood Gem", "+18% gun damage", "Adds +18% to gun damage."),
    4423: ("Arcane Blood Gem", "+15% arcane damage", "Adds +15% to arcane damage and imbues weapon with arcane."),
    4424: ("Fire Blood Gem", "+15% fire damage", "Adds +15% to fire damage and imbues weapon with fire."),
    4425: ("Bolt Blood Gem", "+15% bolt damage", "Adds +15% to bolt damage and imbues weapon with bolt."),
    4426: ("Hard Blood Gem", "+15% physical damage", "Adds +15% to physical damage."),
    4427: ("Shiny Blood Gem", "+13% all damage", "Adds +13% to all damage types."),
}

REDIRECT_RUNES_TO_GOODS = {
    11000002: 4503,  # Clockwise Metamorphosis
    11000003: 4504,  # Anti-Clockwise Metamorphosis
    11000004: 4505,  # Clawmark
    11000005: 4506,  # Blood Rapture
    11000006: 4507,  # Oedon
    11000007: 4508,  # Heir
    11000012: 4513,  # Arcane
    11000013: 4514,  # Fading
    11000014: 4516,  # Dissipating
    11000015: 4517,  # Lake
    11000016: 4518,  # Great
    11000017: 4520,  # Clear
    11000018: 4521,  # Stunning
    11000019: 4522,  # Deep
    11000020: 4523,  # Great
    11000021: 4524,  # Beast
    11000025: 4529,  # Communion
    11000026: 4531,  # Formless
    11000029: 4540,  # Guidance

    12000004: 4600,  # Radiance
    12000005: 4610,  # Corruption
    12000006: 4620,  # Hunter
    12000008: 4640,  # Beast's Embrace
    12000009: 4650,  # Milkweed
}


def main():
    """Apply all modifications to vanilla file and save."""
    for language in ("engus", "enggb"):
        msg_directory = MSGDirectory(BB_PATH + f"/msg/{language}")

        msg_directory.ArmorNames[250000] = "Grand Hunter's Crown"
        msg_directory.ArmorDescriptions[250000] = (
            "Crown of a hunter who has conquered death in all its forms, and those who deal in it.\n\n"
            "Bestows no special abilities, but casts down all eyes laid upon it.\n\n"
            "Rightfully so."
        )

        msg_directory.EventText.update(NEW_EVENT_TEXT)

        for class_name in range(402401, 402410):
            msg_directory.MenuText_SP[class_name] = "Gladiator"
            msg_directory.MenuHelpSnippets_SP[class_name] = "Champion from a distant land.\nThirsts for bloodshed."

        msg_directory.GoodNames[100] = "Skull of Memories"
        msg_directory.GoodSummaries[100] = "Use to face legendary foes from an old tale"
        msg_directory.GoodDescriptions[100] = (
            "Old skull of an unknown hunter.\n\n"
            "Its hollow gaze conjures memories of monsters from the hunter's journey through Yharnam, and beyond.\n\n"
            "Use from within the memory to return to the Dream."
        )

        msg_directory.GoodNames[101] = "Skull of Chaos"
        msg_directory.GoodSummaries[101] = "Use to face legendary foes from scattered recollection"
        msg_directory.GoodDescriptions[101] = (
            "Disfigured skull of an unknown hunter.\n\n"
            "Its hollow gaze conjures violent memories, but the nightmare has twisted their chronology.\n\n"
            "Use from within the memory to return to the Dream."
        )

        msg_directory.GoodNames[102] = "Dreaming Blank"
        msg_directory.GoodSummaries[102] = "Return to the Dream without delay"
        msg_directory.GoodDescriptions[102] = (
            "Emits an inaudible burst that abruptly ends waking entanglements.\n\n"
            "Use from within the memory to return to the Dream."
        )

        for gem_id, good_id in REDIRECT_RUNES_TO_GOODS.items():
            msg_directory.GoodNames[good_id] = msg_directory.BloodGemNames[gem_id]
            msg_directory.GoodSummaries[good_id] = msg_directory.BloodGemSummaries[gem_id]
            msg_directory.GoodDescriptions[good_id] = msg_directory.BloodGemDescriptions[gem_id] + (
                "\n\nOnly one Caryll Rune and one Covenant Rune can be purchased at a time."
            )

        for good_id, (name, summary, desc) in NEW_GEM_TEXT.items():
            msg_directory.GoodNames[good_id] = name
            msg_directory.GoodSummaries[good_id] = summary
            msg_directory.GoodDescriptions[good_id] = desc + "\n\nOnly one gemstone can be purchased at a time."

        msg_directory.write(f"../package/msg/{language}")

    for bak_file in Path("../package/msg").rglob("*.bak"):
        os.remove(bak_file)


if __name__ == '__main__':
    main()
