
from soulstruct.game_types import *


class BossRushFlags(Flag):
    """BOSS RUSH MOD FLAGS. Stolen from Abandoned Old Workshop flag range (1000+) that is never used in vanilla.

    Common event 7400 (22 slots) is used to control the lanterns and request warps.
    Common event 7450 (22 slots) is used to execute warps to bosses.
    Event 7493 listens for the Story Boss Rush bell request.
    Event 7494 listens for the Random Boss Rush bell request.
    Event 7495 is the completion monitoring event.
    Event 7496 is the story boss order choice event.
    Event 7497 is the random boss order choice event.
    Event 7498 is used to warp back to the Hunter's Dream, as requested by flag 7499.
    """
    RequestDreamReturn = 7499
    BossRushActive = 12111800
    BossRushCompleted = 12111801
    MoonPresenceRequested = 12111998  # boss requires disambiguity separate from warp request flag
    BossRushRandomized = 12111999

    # Boss warp requests ignored while this flag is enabled (during random search).
    ChoosingRandomBoss = 12111000
    # Boss warp request flags, which trigger warps immediately when activated.
    RequestBoss_ClericBeast = 12111001
    RequestBoss_FatherGascoigne = 12111002
    RequestBoss_BloodStarvedBeast = 12111003
    RequestBoss_WitchesOfHemwick = 12111004
    RequestBoss_VicarAmelia = 12111005
    RequestBoss_DarkbeastPaarl = 12111006
    RequestBoss_ShadowsOfYharnam = 12111007
    RequestBoss_Rom = 12111008
    RequestBoss_Amygdala = 12111009
    RequestBoss_MartyrLogarius = 12111010
    RequestBoss_TheOneReborn = 12111011
    RequestBoss_CelestialEmissary = 12111012
    RequestBoss_Ebrietas = 12111013
    RequestBoss_Micolash = 12111014
    RequestBoss_MergosWetNurse = 12111015
    RequestBoss_Ludwig = 12111016
    RequestBoss_LivingFailures = 12111017
    RequestBoss_LadyMaria = 12111018
    RequestBoss_Laurence = 12111019
    RequestBoss_OrphanOfKos = 12111020
    RequestBoss_Gehrman = 12111021
    RequestBoss_MoonPresence = 12111022

    # Boss death flags. These are the same as in the vanilla game, but are disabled every time you return to the Dream.
    BossDead_ClericBeast = 12411700
    BossDead_FatherGascoigne = 12411800
    BossDead_BloodStarvedBeast = 12301800
    BossDead_WitchesOfHemwick = 12201800
    BossDead_VicarAmelia = 12401800
    BossDead_DarkbeastPaarl = 12301700
    BossDead_ShadowsOfYharnam = 12701800
    BossDead_Rom = 13201800
    BossDead_Amygdala = 13301800
    BossDead_MartyrLogarius = 12501800
    BossDead_TheOneReborn = 12801800
    BossDead_CelestialEmissary = 12421700
    BossDead_Ebrietas = 12421800
    BossDead_Micolash = 12601850
    BossDead_MergosWetNurse = 12601800
    BossDead_Ludwig = 13401800
    BossDead_LivingFailures = 13501850
    BossDead_LadyMaria = 13501800
    BossDead_Laurence = 13401850
    BossDead_OrphanOfKos = 13601800
    BossDead_Gehrman = 12101800
    BossDead_MoonPresence = 12101850

    MicolashDyingWordsDone = 72600301


class BossRushWarpPoints(SpawnPointEvent):
    HuntersDream = 2102962  # Normal start position.
    GehrmanOrMoonPresence = 2102965  # Shared (checks warp flag).
    WitchesOfHemwick = 2202951
    BloodStarvedBeast = 2302951
    DarkbeastPaarl = 2302952
    VicarAmelia = 2402951
    ClericBeast = 2412952
    FatherGascoigne = 2412953
    Ebrietas = 2422951
    CelestialEmissary = 2422952
    MartyrLogarius = 2502952
    Micolash = 2602952
    MergosWetNurse = 2602951
    ShadowsOfYharnam = 2702951
    TheOneReborn = 2802951
    Rom = 3202952
    Amygdala = 3302951
    Ludwig = 3402952
    Laurence = 3402953
    LivingFailures = 3502951
    LadyMaria = 3502952
    OrphanOfKos = 3602952


class HeadstoneWarpUnlockedFlags(SpawnPointEvent):
    """All of these flags are simply enabled upon first arrival in the Hunter's Dream."""
    # GehrmanOrMoonPresence = 2102965  # TODO: Single Gehrman and Moon Presence fights are activated elsewhere (gate?).
    WitchesOfHemwick = 12207820 + 10
    BloodStarvedBeast = 12307820 + 10
    DarkbeastPaarl = 12307840 + 10
    VicarAmelia = 12407820 + 10
    ClericBeast = 12417840 + 10
    FatherGascoigne = 12417860 + 10
    Ebrietas = 12427820 + 10
    CelestialEmissary = 12427840 + 10
    MartyrLogarius = 12507840 + 10
    Micolash = 12607840 + 10
    MergosWetNurse = 12607820 + 10
    ShadowsOfYharnam = 12707820 + 10
    TheOneReborn = 12807820 + 10
    Rom = 13207840 + 10
    Amygdala = 13307820 + 10
    Ludwig = 13407840 + 10
    Laurence = 13407860 + 10
    LivingFailures = 13507820 + 10
    LadyMaria = 13507840 + 10
    OrphanOfKos = 13607840 + 10


class BossRushTriggers(Region):
    """Cylindrical regions that overlay each warp point.

    ID range (aab275x) is 200 less than the warp point, and confirmed to be available in all maps.
    """
    # No trigger region needed for Hunter's Dream.
    GehrmanOrMoonPresence = 2102765  # Shared (checks warp flag).
    WitchesOfHemwick = 2202751
    BloodStarvedBeast = 2302751
    DarkbeastPaarl = 2302752
    VicarAmelia = 2402751
    ClericBeast = 2412752
    FatherGascoigne = 2412753
    Ebrietas = 2422751
    CelestialEmissary = 2422752
    MartyrLogarius = 2502752
    Micolash = 2602752  # Lantern has been moved into locked chamber where Micolash is supposed to be killed (h000022).
    MergosWetNurse = 2602751
    ShadowsOfYharnam = 2702751
    TheOneReborn = 2802751
    Rom = 3202752
    Amygdala = 3302751  # Lantern has been moved into boss chamber, right where boss spawns (same MapPiece draw parent).
    Ludwig = 3402752
    Laurence = 3402753
    LivingFailures = 3502751
    LadyMaria = 3502752
    OrphanOfKos = 3602752


class BossRushText(EventText):
    FaceNextFoe = 70011002


class BossRushItemLots(ItemLotParam):
    VialBulletRefill = 1000
    Bells = 10010


class BossRushGoods(GoodParam):
    QuicksilverBullet = 900
    BloodBullet = 901
    BloodVial = 1000


class BossRushEffects(SpecialEffectParam):
    StoryRushRequest = 9500
    RandomRushRequest = 9501