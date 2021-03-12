"""Modify Bloodborne `MSGDirectory` to rename warp destination names and add new prompts."""
import os
from pathlib import Path

from soulstruct.bloodborne.text import MSGDirectory
from soulstruct.config import BB_PATH


NEW_EVENT_TEXT = {
    70002201: "Witch of Hemwick",  # Witch's Abode
    70002301: "Blood-Starved Beast",  # Church of the Good Chalice
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
    70002803: "The One Reborn",  # Yahar'gul Chapel
    70003202: "Rom, the Vacuous Spider",  # Moonside Lake
    70003301: "Amygdala",  # Amygdala's Chamber
    70003402: "Ludwig, the Holy Blade",  # Underground Corpse Pile
    70003403: "Laurence, the First Vicar",  # Nightmare Grand Cathedral
    70003501: "Living Failures",  # Lumenwood Garden
    70003502: "Lady Maria of the Astral Clocktower",  # Astral Clocktower
    70003602: "Orphan of Kos",  # Coast

    70011002: "Face next foe",
}


def main():
    """Apply all modifications to vanilla file and save."""
    for language in ("engus", "enggb"):
        msg_directory = MSGDirectory(BB_PATH + f"/msg/{language}")

        msg_directory.ArmorNames[250000] = "Grand Hunter's Crown"
        msg_directory.ArmorDescriptions[250000] = (
            "Crown of a hunter who has conquered death in all its forms, and those who dole it out.\n\n"
            "Bestows no special abilities, but makes into timid subjects all who lay eyes upon it.\n\n"
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

        msg_directory.write(f"../package/msg/{language}")

    for bak_file in Path("../package/msg").rglob("*.bak"):
        os.remove(bak_file)


if __name__ == '__main__':
    main()
