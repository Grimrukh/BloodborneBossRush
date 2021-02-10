"""Modify Bloodborne `MSGDirectory` to rename warp destination names and add new prompts."""
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
    msg_directory = MSGDirectory(BB_PATH + "/msg/engus")

    msg_directory.EventText.update(NEW_EVENT_TEXT)

    for class_name in range(402401, 402410):
        msg_directory.MenuText_SP[class_name] = "Gladiator"
        msg_directory.MenuHelpSnippets_SP[class_name] = "Champion from a distant land.\nThirsts for bloodshed."

    msg_directory.GoodNames[200] = "Bell of Memories"
    msg_directory.GoodSummaries[200] = "Ring to face legendary foes from an old tale"
    msg_directory.GoodDescriptions[200] = (
        "Great old bell left behind by an unknown hunter.\n\n"
        "Its ring conjures memories of beasts and monsters from the hunter's journey through Yharnam, and beyond.\n\n"
        "Ring from within the memory to return to the Dream."
    )

    msg_directory.GoodNames[225] = "Bell of Chaos"
    msg_directory.GoodSummaries[225] = "Ring to face legendary foes from scattered recollection"
    msg_directory.GoodDescriptions[225] = (
        "Strange bell left behind by an unknown hunter.\n\n"
        "Its ring conjures memories of a hunter's journey, but the nightmare has twisted their sequence "
        "unpredictably.\n\n"
        "Ring from within the memory to return to the Dream."
    )

    msg_directory.write("../package/msg/engus")


if __name__ == '__main__':
    main()
