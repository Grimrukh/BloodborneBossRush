"""Modify Bloodborne `GameParamBND` to:

    - set all boss levels to end-game scaling
    - adjust starting classes
    - set up new Bath Messengers (weapons, items) and Insight Messengers (armor) shop lineups
"""
import os
from enum import IntEnum
from pathlib import Path

from soulstruct.bloodborne.params import GameParamBND
from soulstruct.config import BB_PATH


DEBUG_BOSS_LEVEL = False  # all enemies have level 7001
DEBUG_PLAYER_LVL = False


class StartingClasses(IntEnum):
    """Player param IDs. Add 1000 to get the identical param displayed in the character creation screen."""
    Milquetoast = 2000
    LoneSurvivor = 2001
    TroubledChildhood = 2002
    ViolentPast = 2003
    Professional = 2004
    MilitaryVeteran = 2005
    NobleScion = 2006
    CruelFate = 2007
    WasteOfSkin = 2008


class BossCharacterParam(IntEnum):
    """Just for my reference, for param editing. These are listed in "story mode" Boss Rush order. Also includes boss
    minion characters."""
    ClericBeast = 500241
    FatherGascoignePhaseOne = 271000
    FatherGascoignePhaseTwo = 272000
    BloodStarvedBeast = 209000
    WitchOfHemwick = 210020  # both witches
    WitchOfHemwickMadOne = 205010
    VicarAmelia = 502000
    DarkbeastPaarl = 508000
    ShadowOfYharnam1 = 212700
    ShadowOfYharnam2 = 212710
    ShadowOfYharnam3 = 212720
    ShadowSmallSnake = 212750
    ShadowLargeSnake = 503300
    Rom = 510000
    RomSpiderMinion = 140010
    Amygdala = 512000
    MartyrLogarius = 232000
    MartyrLogariusSword = 232100
    TheOneRebornBody = 507000
    TheOneRebornHead = 507100
    TheOneRebornCaster = 507200
    TheOneRebornMaiden = 105810
    CelestialEmissary = 250080
    CelestialEmissaryGiant = 257010
    CelestialEmissaryGiantTentacles1 = 257100
    CelestialEmissaryGiantTentacles2 = 257101
    CelestialEmissaryMinion = 250081
    CelestialEmissaryMinionTentacles = 250150
    Ebrietas = 251000
    Micolash = 6380  # uses separate buff for Players. Not touching here.
    MicolashPuppet = 204600
    MicolashAttendant1 = 225000
    MicolashAttendant2 = 225020
    MergosWetNurse = 551000  # includes copies
    LudwigPhaseOne = 451000
    LudwigPhaseTwo = 451001
    LivingFailures1 = 403000
    LivingFailures2 = 403010
    LivingFailures3 = 403020
    LivingFailures4 = 403030
    LivingFailuresPool = 403050
    LadyMaria = 452000
    Laurence = 450000
    OrphanOfKosPhaseOne = 454000
    OrphanOfKosPhaseTwo = 454100
    Gehrman = 805000
    MoonPresence = 540000


def print_change(entry, field, value):
    print(f" {field}: {entry[field]} -> {value}")
    entry[field] = value


def set_boss_levels(game_param_bnd: GameParamBND):
    """Set special effects to scale difficulty of bosses. Also removes any soul rewards."""
    ng_plus_level = 7413  # Moon Presence NG+ level

    for boss in BossCharacterParam:
        boss_entry = game_param_bnd.Characters[boss]
        boss_entry["getSoul"] = 0
        if boss == BossCharacterParam.Micolash:
            pass  # leaving Micolash as he is (he's almost end-game level anyway)
        else:
            if DEBUG_BOSS_LEVEL:
                print_change(boss_entry, "spEffectID6", 7001)
            else:
                if boss_entry["spEffectID6"] < 7017 or 7023 <= boss_entry["spEffectID6"] <= 7029:
                    print_change(boss_entry, "spEffectID6", 7017)
                # Otherwise, leave boss at standard level (including all DLC bosses).
            print_change(boss_entry, "GameClearSpEffectID", ng_plus_level)

    # Cleric Beast has too much HP by default.
    cleric_beast_entry = game_param_bnd.Characters[BossCharacterParam.ClericBeast]
    cleric_beast_entry["hp"] = int(0.85 * 2700)


def set_starting_classes(game_param_bnd: GameParamBND):

    for starting_class in StartingClasses:
        for class_id in (starting_class, starting_class + 1000):
            player_entry = game_param_bnd.Players[class_id]
            print(f"Class {starting_class.name} ({class_id}):")
            print_change(player_entry, "soul", 1019240)  # exactly enough to get from level 4 to 80

            if DEBUG_PLAYER_LVL:
                print_change(player_entry, "soulLv", 99)
                print_change(player_entry, "baseVit", 99)
                print_change(player_entry, "baseWil", 50)
                print_change(player_entry, "baseStr", 99)
                print_change(player_entry, "baseDex", 99)
                print_change(player_entry, "baseMag", 99)
                print_change(player_entry, "baseFai", 99)
            else:
                print_change(player_entry, "soulLv", 4)
                print_change(player_entry, "baseVit", 10)
                print_change(player_entry, "baseWil", 9)
                print_change(player_entry, "baseStr", 10)
                print_change(player_entry, "baseDex", 9)
                print_change(player_entry, "baseMag", 7)
                print_change(player_entry, "baseFai", 9)

            print_change(player_entry, "baseHeroPoint", 25)  # insight
            print_change(player_entry, "item_01", -1)  # remove Hunter's Mark  # TODO: add Rune Workshop Tool (4104)
            print_change(player_entry, "itemNum_01", 1)


def set_shop_lineups(game_param_bnd: GameParamBND):
    """All weapons and most items are for sale in Bath Messengers shop, using insight (earned from defeating bosses).

    Bath shop range: 100000 to 109999 (with other time periods at +10000, +20000, +30000).
    Insight shop range: 200000 to 200099 (with other time periods at +10000, +20000, +30000).

    Note the greatly reduced shop range of the insight shop (100 items rather than 10000).
    # TODO: sort out insight vs. bath shop properly. Currently, consumables and armor are divided kinda randomly.

    Armor is still for sale in Insight Messengers shop, along with other things that were originally sold there.
    TODO: If I can be bothered, move non-armor stuff from Insight to Bath shop.

    Note that the player starts with enough insight to buy two weapons (10), an armor set (5), a gem (1), rune (2), and
    covenant rune (2), for a total of 20.
    """

    # Any item not present in one of these categories will be removed.
    common_items = (  # 1 insight
        100002,  # Molotov Cocktail
        100114,  # Throwing Knife
        100207,  # Rope Molotov Cocktail
        100604,  # Antidote
        101001,  # Poison Knife
        101002,  # Sedative
        101021,  # Delayed Molotov
        101022,  # Delayed Rope Molotov
    )
    uncommon_items = (  # 2 insight
        100206,  # Oil Urn
        100503,  # Bolt Paper
        100705,  # Fire Paper
        100706,  # Bone Marrow Ash
        200009,  # Lead Elixir
    )
    rare_items = (  # 3 insight
        100115,  # Pungent Blood Cocktail
        100606,  # Hand Lantern
        200005,  # Blue Elixir
        200007,  # Numbing Mist
    )
    weapons = (  # 5 insight
        100100,  # Saw Cleaver
        100103,  # Hunter's Axe
        100106,  # Threaded Cane
        100109,  # Saw Spear
        100112,  # Hunter Pistol
        100113,  # Hunter Blunderbuss
        100200,  # Stake Driver
        100203,  # Rifle Spear
        100300,  # Burial Blade
        100400,  # Blades of Mercy
        100500,  # Tonitrus
        100600,  # Kirkhammer
        100603,  # Repeating Pistol
        100700,  # Ludwig's Holy Blade
        100703,  # Ludwig's Rifle
        100704,  # Flamesprayer
        100800,  # Logarius Wheel
        100900,  # Reiterpallasch
        100903,  # Chikage
        100906,  # Evelyn
        101000,  # Rosmarinus
        101020,  # Piercing Rifle
        101100,  # Beast Claw
        101103,  # Cannon
        101104,  # Torch
        101110,  # Beasthunter Saif
        101113,  # Beast Cutter
        101116,  # Church Pick
        101119,  # Simon's Bowblade
        101122,  # Holy Moonlight Sword
        101125,  # Rakuyo
        101128,  # Whirligig Saw
        101131,  # Boom Hammer
        101134,  # Bloodletter
        101137,  # Amygdalan Arm
        101140,  # Kos Parasite
        101143,  # Gatling Gun
        101144,  # Church Cannon
        101145,  # Fist of Gracia
        101146,  # Loch Shield
    )
    armor_pieces = (  # 1 insight per piece, except 2 for chest (detected from `equipId`)
        100004, 100005, 100006, 100007,  # Yharnam set
        100303, 100304, 100305,  # Gehrman set (no head)
        100403, 100404, 100405, 100406,  # Eileen set
        100709, 100710, 100711, 100712,  # Tomb Prospector set
        # 100803,  # Executioner set (full set created manually at this ID)
        100907, 100908, 100909, 100910,  # Cainhurst set
        200030, 200031, 200032, 200033,  # Henryk set
        200040, 200041, 200042, 200043,  # Gascoigne set
        200050, 200051, 200052, 200053,  # Djura set
        200060, 200061, 200062, 200063,  # Bone Ash set
        200064, 200065, 200066, 200067,  # Madman set
        200090, 200091, 200092, 200093,  # Maria set
        # New sets added below in slots near these.
    )

    def _copy_armor_set(source_head_row_id, dest_head_row_id, head_armor_id, set_name: str):
        for i_, (piece_type, piece_offset) in enumerate(
            zip(("Head", "Body", "Arms", "Legs"), (0, 1000, 2000, 3000))
        ):
            armor_id = head_armor_id + piece_offset
            if armor_id not in game_param_bnd.Armor:
                print(f"Missing armor piece: {armor_id}. Skipping.")
                continue  # missing piece, e.g. arms for Student Set
            _entry = game_param_bnd.Shops[dest_head_row_id + i_] = game_param_bnd.Shops[source_head_row_id + i_].copy()
            game_param_bnd.Armor[armor_id]["sellValue"] = 0
            print_change(_entry, "equipId", armor_id)
            _entry.name = f"{set_name} ({piece_type})"
            for s in (10000, 20000, 30000):
                game_param_bnd.Shops[dest_head_row_id + i_ + s] = game_param_bnd.Shops[dest_head_row_id + i_].copy()

    def _copy_armor_piece(source_piece_id, dest_piece_id, armor_id, name: str):
        _entry = game_param_bnd.Shops[dest_piece_id] = game_param_bnd.Shops[source_piece_id].copy()
        print_change(_entry, "equipId", armor_id)
        _entry.name = f"{name}"
        for s in (10000, 20000, 30000):
            game_param_bnd.Shops[dest_piece_id + s] = game_param_bnd.Shops[dest_piece_id].copy()

    # These will be removed below anyway, but I'm making it explicit here.
    game_param_bnd.Shops.pop(100803)  # Gold Ardeo (full Executioner set created below)
    game_param_bnd.Shops.pop(200070)  # Short Ritual Root Chalice (slot used by new armor below)

    def _set_insight_price(entry_id, price: int):
        """Sets insight price of given shop ID, and also removes any 'qwcId' and 'eventFlag'."""
        _entry = game_param_bnd.Shops[entry_id]
        print(f"{_entry.name}:")
        print_change(_entry, "shopType", 5)  # price is insight
        print_change(_entry, "eventFlag", -1)  # always available
        print_change(_entry, "sellQuantity", -1)  # unlimited supply
        print_change(_entry, "qwcId", -1)  # no badge required
        print_change(_entry, "value", price)  # insight cost

    to_remove = []
    for row_id, row in game_param_bnd.Shops.items():
        # Many entries are duplicated multiple times in the shop lineup for stock in different time periods (times of
        # day). The row ID checked is the first entry, in the range [100000, 109999] or [200000, 209999].
        if 140000 <= row_id < 149999 or 240000 <= row_id < 249999:
            check_row_id = row_id - 40000
        elif 130000 <= row_id < 139999 or 230000 <= row_id < 239999:
            check_row_id = row_id - 30000
        elif 120000 <= row_id < 129999 or 220000 <= row_id < 229999:
            check_row_id = row_id - 20000
        elif 110000 <= row_id < 119999 or 210000 <= row_id < 219999:
            check_row_id = row_id - 10000
        elif 100000 <= row_id < 109999 or 200000 <= row_id < 209999:
            check_row_id = row_id
        else:
            # Ignore this ID (chalice merchant, internal, etc.).
            continue

        if check_row_id in common_items:
            _set_insight_price(row_id, 1)
            game_param_bnd.Goods[row["equipId"]]["sellValue"] = 0
        elif check_row_id in uncommon_items:
            _set_insight_price(row_id, 1)  # NOTE: everything reduce to 1
            game_param_bnd.Goods[row["equipId"]]["sellValue"] = 0
        elif check_row_id in rare_items:
            _set_insight_price(row_id, 1)  # NOTE: everything reduced to 1
            game_param_bnd.Goods[row["equipId"]]["sellValue"] = 0
        elif check_row_id in weapons:
            _set_insight_price(row_id, 5)
            if row["equipId"] + 1000 in game_param_bnd.Weapons:
                row["equipId"] += 1000  # Change weapon ID to +10 (if available).
            game_param_bnd.Weapons[row["equipId"]]["sellValue"] = 0
            # Copying durability setup of bare fists (1/0). Seems to work.
            game_param_bnd.Weapons[row["equipId"]]["durability"] = 1
            game_param_bnd.Weapons[row["equipId"]]["durabilityMax"] = 0
        elif check_row_id in armor_pieces:
            game_param_bnd.Armor[row["equipId"]]["sellValue"] = 0
            if str(row['equipId']).endswith("1000"):
                _set_insight_price(row_id, 2)  # Body armor
            else:
                _set_insight_price(row_id, 1)  # Head/arms/legs armor
        else:
            to_remove.append(row_id)

    for row_id in to_remove:
        game_param_bnd.Shops.pop(row_id)
        print(f"Removed ID: {row_id}")

    _copy_armor_set(200030, 100803, 150000, "Executioner Set")
    _copy_armor_set(200030, 200034, 20000, "Yahar'gul Black Set")
    _copy_armor_set(200030, 200044, 30000, "Graveguard Set")
    _copy_armor_set(200030, 200054, 80000, "Knight Set")
    _copy_armor_set(200030, 200094, 110000, "Black Church Set")
    _copy_armor_set(200030, 200070, 120000, "Choir Set")
    _copy_armor_set(200030, 200074, 190000, "Student Set")
    _copy_armor_set(200030, 200078, 220000, "Doll Set")

    # _copy_armor_piece(200030, 200082, 250000, "Crown of Illusions")
    _copy_armor_piece(200030, 200083, 270000, "Iron Yahar'gul Helm")
    _copy_armor_piece(200030, 200084, 280000, "Top Hat")
    _copy_armor_piece(200030, 200085, 281000, "Hunter Garb")
    _copy_armor_piece(200030, 200086, 290000, "White Church Hat")
    _copy_armor_piece(200030, 200087, 291000, "White Church Garb")
    _copy_armor_piece(200030, 200088, 293000, "White Church Trousers")
    _copy_armor_piece(200030, 200089, 311000, "Alluring Dress")

    # Remove miscellaneous sell values.
    game_param_bnd.Goods[900]["sellValue"] = 0  # Quicksilver Bullet
    game_param_bnd.Goods[1000]["sellValue"] = 0  # Blood Vial
    game_param_bnd.Armor[230000]["sellValue"] = 0  # Black Hood
    game_param_bnd.Armor[231000]["sellValue"] = 0  # Foreign Garb
    game_param_bnd.Armor[232000]["sellValue"] = 0  # Sullied Bandage
    game_param_bnd.Armor[233000]["sellValue"] = 0  # Foreign Trousers

    # Add missing consumables to normal shop.
    beast_blood_pellet_shop = game_param_bnd.Shops[100208] = game_param_bnd.Shops[100207].copy()
    beast_blood_pellet_shop["equipId"] = 1110
    for i in (10000, 20000, 30000, 40000):
        game_param_bnd.Shops[100208 + i] = beast_blood_pellet_shop.copy()

    # Add spell items to insight shop.
    spell_goods = {
        2000: "Augur of Ebrietas",
        2010: "A Call Beyond",
        2020: "Beast Roar",
        2050: "Choir Bell",
        2060: "Old Hunter Bone",
        2070: "Tiny Tonitrus",
        2080: "Executioner's Gloves",
        2110: "Messenger's Gift",
        2120: "Blacksky Eye",
        2130: "Accursed Brew",
        2140: "Madaras Whistle",
    }
    for i, (spell_good, good_name) in enumerate(spell_goods.items()):
        shop_entry = game_param_bnd.Shops[200030].copy()
        shop_entry["value"] = 3
        shop_entry["equipId"] = spell_good
        shop_entry["equipType"] = 3  # Good
        shop_entry["eventFlag"] = -1
        shop_entry["sellQuantity"] = -1
        shop_entry.name = good_name
        for offset in (0, 10000, 20000, 30000):
            game_param_bnd.Shops[200010 + offset + i] = shop_entry

    # Add "gem" and "rune" goods.
    for i, blood_gem in enumerate(range(19, 28)):
        gem = game_param_bnd.Shops[200030].copy()
        gem["value"] = 1
        gem["equipId"] = 4400 + blood_gem
        gem["equipType"] = 3  # Good
        gem["eventFlag"] = 12112600 + 10 * i  # only nine of them
        gem["sellQuantity"] = 1
        for offset in (0, 10000, 20000, 30000):
            game_param_bnd.Shops[101160 + offset + i] = gem

    for i, rune_id in enumerate(RUNE_IDS):
        rune = game_param_bnd.Shops[200030].copy()
        rune["value"] = 2
        rune["equipId"] = 4500 + rune_id
        rune["equipType"] = 3  # Good
        rune["eventFlag"] = 12112700 + 10 * i  # only 19 of them
        rune["sellQuantity"] = 1
        for offset in (0, 10000, 20000, 30000):
            game_param_bnd.Shops[101170 + offset + i] = rune

    for i, covenant_rune_id in enumerate(COVENANT_RUNE_IDS):
        covenant_rune = game_param_bnd.Shops[200030].copy()
        covenant_rune["value"] = 2
        covenant_rune["equipId"] = 4600 + covenant_rune_id - 200000
        covenant_rune["equipType"] = 3  # Good
        covenant_rune["eventFlag"] = 12112900 + 10 * i  # only five of them
        covenant_rune["sellQuantity"] = 1
        for offset in (0, 10000, 20000, 30000):
            game_param_bnd.Shops[101190 + offset + covenant_rune_id - 200000] = covenant_rune


def set_new_item_lots(game_param_bnd: GameParamBND):
    game_param_bnd.ItemLots[1000] = vial_refill = game_param_bnd.ItemLots[5500].copy()
    vial_refill.name = "Blood Vial Refill 20"
    vial_refill["lotItemId01"] = 1000
    vial_refill["lotItemNum01"] = 20

    game_param_bnd.ItemLots[1010] = bullet_refill = game_param_bnd.ItemLots[5500].copy()
    bullet_refill.name = "Quicksilver Bullet Refill 20"
    bullet_refill["lotItemId01"] = 900
    bullet_refill["lotItemNum01"] = 20

    game_param_bnd.ItemLots[1020] = vial_refill = game_param_bnd.ItemLots[5500].copy()
    vial_refill.name = "Blood Vial Refill 10"
    vial_refill["lotItemId01"] = 1000
    vial_refill["lotItemNum01"] = 10

    game_param_bnd.ItemLots[1030] = bullet_refill = game_param_bnd.ItemLots[5500].copy()
    bullet_refill.name = "Quicksilver Bullet Refill 10"
    bullet_refill["lotItemId01"] = 900
    bullet_refill["lotItemNum01"] = 10

    boss_rush_reward = game_param_bnd.ItemLots[10000]  # overwriting Notebook drop
    boss_rush_reward.name = "Boss Rush Reward"
    boss_rush_reward["lotItemCategory01"] = 1  # Armor
    boss_rush_reward["lotItemId01"] = 250000  # Grand Hunter's Crown

    boss_rush_request_item_1 = game_param_bnd.ItemLots[10010]  # overwriting Beckoning Bell drop
    boss_rush_request_item_1.name = "Skull of Memories"
    boss_rush_request_item_1["lotItemId01"] = 100  # Skull of Memories
    game_param_bnd.ItemLots[10011] = boss_rush_request_item_2 = boss_rush_request_item_1.copy()
    boss_rush_request_item_2.name = "Skull of Chaos"
    boss_rush_request_item_2["lotItemId01"] = 101  # Skull of Chaos
    game_param_bnd.ItemLots[10012] = dreaming_blank_lot = boss_rush_request_item_1.copy()
    dreaming_blank_lot.name = "Dreaming Blank"
    dreaming_blank_lot["lotItemId01"] = 102  # Dreaming Blank


def set_goods_and_effects(game_param_bnd: GameParamBND):
    template_effect = game_param_bnd.SpecialEffects[9000].copy()
    template_effect["stateInfo"] = 0
    game_param_bnd.SpecialEffects[9500] = template_effect.copy()  # Request story boss rush
    game_param_bnd.SpecialEffects[9501] = template_effect.copy()  # Request random boss rush
    game_param_bnd.SpecialEffects[9502] = template_effect.copy()  # Request dream return

    skull_of_memories = game_param_bnd.Goods[100]  # Hunter's Mark
    skull_of_memories.name = "Skull of Memories"
    skull_of_memories.update(
        refId=9500,
        iconId=76,  # Madman's Knowledge
        yesNoDialogMessageId=0,
        opmeMenuType=0,
    )

    game_param_bnd.Goods[101] = skull_of_chaos = skull_of_memories.copy()
    skull_of_chaos.name = "Skull of Chaos"
    skull_of_chaos.update(
        refId=9501,
        iconId=77,  # Great One's Wisdom
    )

    game_param_bnd.Goods[102] = dreaming_blank = skull_of_memories.copy()
    dreaming_blank.name = "Dreaming Blank"
    dreaming_blank.update(
        refId=9502,  # Homeward
        iconId=9,
        opmeMenuType=0,
        goodsUseAnim=15,  # normal Silencing Blank animation
    )


def set_action_buttons(game_param_bnd: GameParamBND):
    challenge_gehrman = game_param_bnd.ActionButtons[7002].copy()
    challenge_gehrman["textId"] = 80001  # Challenge Gehrman, the First Hunter
    challenge_gehrman.name = "Challenge Gehrman"
    game_param_bnd.ActionButtons[7003] = challenge_gehrman
    challenge_moon_presence = game_param_bnd.ActionButtons[7002].copy()
    challenge_moon_presence["textId"] = 80002  # Challenge Moon Presence
    challenge_moon_presence.name = "Challenge Moon Presence"
    game_param_bnd.ActionButtons[7004] = challenge_moon_presence


RUNE_IDS = {
    # 0: "Moon",  # blood echoes up
    # 1: blood echoes down
    # 2: "Eye",  # item drop up
    3: "Clockwise Metamorphosis",  # max HP up
    4: "Anti-Clockwise Metamorphosis",  # max stamina up
    5: "Clawmark",  # visceral damage up
    6: "Blood Rapture",  # visceral health regain
    7: "Oedon Writhe",  # visceral attack bullet recovery
    8: "Heir",  # visceral attack blood echoes
    # 9: slash defense up
    # 10: blunt defense up
    # 11: thrust defense up
    # 12: gun defense up
    13: "Arcane Lake",  # arcane defense up
    14: "Fading Lake",  # fire defense up
    # 15: fire defense down
    16: "Dissipating Lake",  # bolt defense up
    17: "Lake",  # physical defense up
    18: "Great Lake",  # all defense up
    # 19: all defense down
    20: "Clear Deep Sea",  # slow poison defense up
    21: "Stunning Deep Sea",  # fast poison defense up
    22: "Deep Sea",  # frenzy defense up
    23: "Great Deep Sea",  # all status resistance up
    24: "Beast",  # beast extension
    # 25: slow poison shortening
    # 26: fast poison shortening
    # 27: blood vial recovery up
    # 28: blood vial recovery down
    29: "Communion",  # max blood vials up
    # 30: max blood vials down
    31: "Formless Oedon",  # max bullets up
    # 32: max bullets down
    # 33: stamina recovery speed up
    # 34: stamina recovery speed down
    # 35: fall damage reduction
    40: "Guidance",  # rally potential up (NOTE: level 3 not found in game)

    # Beast's Embrace
    # Corruption
    # Hunter
    # Impurity (no point including)
    # Milkweed
    # Radiance
}

# Taken from the old cut goods (1600+).
RUNE_GOOD_ICONS = {
    3: 332,  # "Clockwise Metamorphosis",  # max HP up
    4: 333,  # "Anti-Clockwise Metamorphosis",  # max stamina up
    5: 341,  # "Clawmark",  # visceral damage up
    6: 334,  # "Blood Rapture",  # visceral health regain
    7: 335,  # "Oedon Writhe",  # visceral attack bullet recovery
    8: 342,  # "Heir",  # visceral attack blood echoes
    13: 336,  # "Arcane Lake",  # arcane defense up
    14: 336,  # "Fading Lake",  # fire defense up
    16: 336,  # "Dissipating Lake",  # bolt defense up
    17: 336,  # "Lake",  # physical defense up
    18: 336,  # "Great Lake",  # all defense up
    20: 337,  # "Clear Deep Sea",  # slow poison defense up
    21: 337,  # "Stunning Deep Sea",  # fast poison defense up
    22: 337,  # "Deep Sea",  # frenzy defense up
    23: 337,  # "Great Deep Sea",  # all status resistance up
    24: 338,  # "Beast",  # beast extension
    29: 339,  # "Communion",  # max blood vials up
    31: 340,  # "Formless Oedon",  # max bullets up
    40: 330,  # "Guidance",  # rally potential up (NOTE: level 3 not found in game)
}

RUNE_SP_EFFECTS = {
    3: 103002,
    4: 105002,
    5: 107002,
    6: 108002,
    7: 110002,
    8: 112002,
    13: 118002,
    14: 119002,
    16: 121002,
    17: 122002,
    18: 123002,
    20: 125002,
    21: 126002,
    22: 127002,
    23: 128002,
    24: 129002,
    29: 134004,  # level 5
    31: 136004,  # level 5
    40: 141002,  # Guidance level 3, normally unobtainable
}

# Actual `GemsAndRunes` entries.
COVENANT_RUNE_IDS = {
    200000: "Radiance",
    200010: "Corruption",
    200020: "Hunter",
    # 200030: "Impurity",
    200040: "Beast's Embrace",
    200050: "Milkweed",
}


BLOOD_GEM_NAMES = {
    19: "Blood Gem: +18% Slash Damage",
    20: "Blood Gem: +18% Blunt Damage",
    21: "Blood Gem: +18% Thrust Damage",
    22: "Blood Gem: +18% Gun Damage",
    23: "Blood Gem: +15% Arcane Damage",
    24: "Blood Gem: +15% Fire Damage",
    25: "Blood Gem: +15% Bolt Damage",
    26: "Blood Gem: +15% Physical Damage",
    27: "Blood Gem: +13% All Damage",
}


def set_gems_and_runes(game_param_bnd: GameParamBND):
    """I can't get gems or runes to appear in shops (using any `equipType`), so I need to use goods (key items) to
    spoof them, and match the texture.

    Buying one will remove any others in that category from your inventory. They cost 1 (gems) or 2 (runes) insight.

    Common EMEVD checks if you possess a "gem" or "rune" good on map load (don't worry about re-checking if you buy a
    new one) and apply a permanent SpEffect to the player with the appropriate effect. They will only apply to the right
    hand weapon, just like Bolt Paper and co, so gems will reapply their effect every second in case you switch weapons.

    The (cost4 rank10) levels of the "magnification" gems give about +15%. For reference, these GemEffects IDs:
        19410: +18% Slash
        20410: +18% Blunt
        21410: +18% Piercing
        22410: +15% Neutral (Guns)
        23410: +15% Arcane (Magic element)
        24410: +15% Fire (Fire element)
        25410: +15% Bolt (Lightning element)
        26410: +15% Physical
        27410: +13% All
    They reference the same SpecialEffect ID. There are also duplicates at +100000 and +200000 (maybe more), possibly
    just for different gem shape slots.
    """
    def create_gem_good(good_id: int, icon_id: int, name: str):
        new_good = game_param_bnd.Goods[4000].copy()  # Oedon Tomb Key
        new_good["iconId"] = icon_id
        new_good["goodsType"] = 2  # key items don't show up; trying materials
        new_good.name = name
        game_param_bnd.Goods[good_id] = new_good

    for i in range(19, 28):  # "Slash" to "All"; see IDs above
        create_gem_good(4400 + i, icon_id=324, name=BLOOD_GEM_NAMES[i])  # Petrified Blood Gem icon

    for rune_id, rune_name in RUNE_IDS.items():
        create_gem_good(4500 + rune_id, icon_id=RUNE_GOOD_ICONS[rune_id], name=rune_name)

    for covenant_rune_id, rune_name in COVENANT_RUNE_IDS.items():
        create_gem_good(4600 + covenant_rune_id - 200000, icon_id=331, name=rune_name)  # Eye


def main():
    """Apply all modifications to vanilla file and save."""
    game_param_bnd = GameParamBND(BB_PATH + "/param/gameparam/gameparam.parambnd.dcx")
    set_boss_levels(game_param_bnd)
    set_starting_classes(game_param_bnd)
    set_shop_lineups(game_param_bnd)
    set_new_item_lots(game_param_bnd)
    set_goods_and_effects(game_param_bnd)
    set_action_buttons(game_param_bnd)
    set_gems_and_runes(game_param_bnd)
    game_param_bnd.write("../package/param/gameparam/gameparam.parambnd.dcx")

    for bak_file in Path("../package/param/gameparam").glob("*.bak"):
        os.remove(bak_file)


if __name__ == '__main__':
    main()
