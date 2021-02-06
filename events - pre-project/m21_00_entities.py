from soulstruct.game_types import *


class Flags(Flag):
    InsightShopOpen = 12100320

    MeleeWeaponGiftReceived = 12101020
    GunGiftReceived = 12101021

    GehrmanDead = 12101800
    GehrmanRefusalCutsceneDone = 12101802
    MoonPresenceDead = 12101850
    MoonPresenceFirstTimeDone = 12101852

    GehrmanBattleFogEntered = 12104800
    GehrmanBattleStartedForSummon = 12104801
    GehrmanBattleStarted = 12104802
    GehrmanBattleWon = 12104809
    MoonPresenceFogEntered = 12104850
    MoonPresenceBattleStarted = 12104852

    YharnamHeadstoneAvailable = 12105030
    FrontierHeadstoneAvailable = 12105031
    UnseenHeadstoneAvailable = 12105032
    NightmareHeadstoneAvailable = 12105033
    OldHuntersHeadstoneAvailable = 12105034
    StumpMessengersActive = 12105063

    GehrmanOfferAccepted = 72100130
    GehrmanOfferRefused = 72100131

    # Lantern active (warpable) flags



class Characters(Character):
    BathShopMessengers1 = 2100211
    BathShopMessengers2 = 2100212
    BathShopMessengers3 = 2100213
    InsightShopMessengers1 = 2100214
    MeleeWeaponGiftMessengers = 2100215
    GunGiftMessengers = 2100216
    StumpMessengers = 2100218
    InsightShopMessengers2 = 2100219
    StoragePrompt = 2100200
    UpgradePrompt = 2100201
    MemoryAltarPrompt = 2100203
    MeleeWeaponGift = 2100220  # looks like an overlay of the three starting weapons
    GunGift = 2100221  # looks like an overlay of the two starting guns
    BellGiftMessengers = 2100230
    OldHuntersMessengers = 2100231  # also give you the Eye of a Blood-Drunk Hunter
    NearStumpMessengers = 2100232
    PlainDoll = 2100700
    GehrmanAlly = 2100600
    GehrmanBoss = 2100800
    MoonPresence = 2100810
    YharnamMessengers = 2100950
    FrontierMessengers = 2100951
    UnseenMessengers = 2100952
    NightmareMessengers = 2100953
    MakeshiftAltar = 2100954  # first altar in row, for Short Ritual Root Chalice
    ChaliceAltar1 = 2100955
    ChaliceAltar2 = 2100956
    ChaliceAltar3 = 2100957
    ChaliceAltar4 = 2100958
    ChaliceAltar5 = 2100959
    ChaliceAltar6 = 2100960  # called "Final Ritual Altar" in-game


class Objects(Object):
    IronGateToField = 2101000
    WorkshopFrontDoorClosed = 2101010
    WorkshopFrontDoorOpen = 2101011
    WorkshopBackDoorClosed = 2101020
    WorkshopBackDoorOpen = 2101021
    WorkshopMiddleDoorClosed = 2101030
    WorkshopMiddleDoorOpen = 2101031
    WorkshopChest = 2101050
    LonelyHeadstone = 2101100  # near Yharnam headstone
    NormalMoon = 2101300
    BloodMoon = 2101301
    NormalMoonSky = 2101310
    BloodMoonSky = 2101311
    BossFog = 2101800


class FX(FXEvent):
    BossFog = 2103800


class Cutscenes(IntEnum):
    FirstArrival = 21000000
    YharnamSunriseEndingFemale = 21000010
    YharnamSunriseEndingMale = 21001010
    HonoringWishesEnding = 21000020
    ChildhoodsBeginningEndingFemale = 21000030
    GehrmanBossBattleStarts = 21000040
    MoonPresenceBattleStarts = 21000050
    ChildhoodsBeginningEndingMale = 21001030


class Music(MusicSound):
    GehrmanPhase1Music = 2103802
    GehrmanPhase2Music = 2103803
    MoonPresencePhase1Music = 2103812
    MoonPresencePhase2Music = 2103813
    NormalMusic = 2103900
    BloodMoonMusic = 2103901


class Regions(Region):  # not bothering to specify type
    BossFogRotateTarget = 2102800
    MoonPresenceBattlePlayerStart = 2102809


class BossNames(EventText):
    Gehrman = 804000


class Goods(GoodParam):
    AugurOfEbrietas = 2000
    ACallBeyond = 2010
    BeastRoar = 2020
    LeadElixir = 2030
    ChoirBell = 2050
    OldHunterBone = 2060
    TinyTonitrus = 2070
    ExecutionersGloves = 2080
    ShamanBoneBlade = 2090
    MessengersGift = 2110
    BloodstoneShard = 3000
    TwinBloodstoneShards = 3010
    BloodstoneChunk = 3020
    BloodRock = 3030
    OedonTombKey = 4000
    GoldPendant = 4001
    CainhurstSummons = 4003
    OrphanageKey = 4006
    # Orphanage2FKey = 4007  # cut
    # UniversityKey = 4008  # cut
    IronDoorKey = 4009
    UpperCathedralKey = 4010
    HunterChiefEmblem = 4011
    LectureTheatreKey = 4012
    LunariumKey = 4013

    WorkshopHazeExtractor = 4102
    BloodGemWorkshopTool = 4103
    RuneWorkshopTool = 4104
    ShortRitualRootChalice = 4105

    SawHunterBadge = 4110
    CrowHunterBadge = 4111
    PowderKegHunterBadge = 4112
    OldHunterBadge = 4113
    SwordHunterBadge = 4114
    RadiantSwordHunterBadge = 4115
    WheelHunterBadge = 4116
    CainhurstBadge = 4117
    SparkHunterBadge = 4118
    CosmicEyeWatcherBadge = 4119

    SmallHairOrnament = 4300

    YharnamMessengerHat = 4900
    WornMessengerTopHat = 4901
    MessengerHeadBandage = 4902
    WhiteMessengerRibbon = 4903
    RedMessengerRibbon = 4904
    MessengerTopHat = 4905
    BlackMessengerHat = 4906
    BloodyMessengerHeadBandage = 4907
    MessengerUrnDance = 4908


class ItemLots(ItemLotParam):
    DollGift = 14000
