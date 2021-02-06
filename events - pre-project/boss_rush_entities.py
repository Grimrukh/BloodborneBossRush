"""
TODO:
    Make sure player always respawns in Hunter's Dream (no other spawn points ever set).
    Change all starting origins to "Bloodstained Gladiator" (with new desc).
    Change all headstone destination names to the boss name.
    Check there are no special "first-time arrival" events in maps that cause stuff to happen.
    Have each area's skybox be in the state you would normally find it for that boss.
"""

from soulstruct.game_types import *


class BossRushFlags(Flag):
    """BOSS RUSH MOD FLAGS (seemingly unused in vanilla game)."""
    # 7400+ slots are post-boss lantern appearance/activation events.
    # 7496 is the story boss order choice event.
    # 7497 is the random boss order choice event.
    BossRushCompleted = 7498
    BossRushRandomized = 7499
    NextBossChosen = 7500
    RequestBoss_ClericBeast = 7501
    RequestBoss_FatherGascoigne = 7502
    RequestBoss_BloodStarvedBeast = 7503
    RequestBoss_WitchesOfHemwick = 7504
    RequestBoss_VicarAmelia = 7505
    RequestBoss_DarkbeastPaarl = 7506
    RequestBoss_ShadowsOfYharnam = 7507
    RequestBoss_Rom = 7508
    RequestBoss_Amygdala = 7509
    RequestBoss_MartyrLogarius = 7510
    RequestBoss_TheOneReborn = 7511
    RequestBoss_CelestialEmissary = 7512
    RequestBoss_Ebrietas = 7513
    RequestBoss_Micolash = 7514
    RequestBoss_MergosWetNurse = 7515
    RequestBoss_Ludwig = 7516
    RequestBoss_LivingFailures = 7517
    RequestBoss_LadyMaria = 7518
    RequestBoss_Laurence = 7519
    RequestBoss_OrphanOfKos = 7520
    RequestBoss_Gehrman = 7521
    RequestBoss_MoonPresence = 7522
    BossDead_ClericBeast = 7601
    BossDead_FatherGascoigne = 7602
    BossDead_BloodStarvedBeast = 7603
    BossDead_WitchesOfHemwick = 7604
    BossDead_VicarAmelia = 7605
    BossDead_DarkbeastPaarl = 7606
    BossDead_ShadowsOfYharnam = 7607
    BossDead_Rom = 7608
    BossDead_Amygdala = 7609
    BossDead_MartyrLogarius = 7610
    BossDead_TheOneReborn = 7611
    BossDead_CelestialEmissary = 7612
    BossDead_Ebrietas = 7613
    BossDead_Micolash = 7614
    BossDead_MergosWetNurse = 7615
    BossDead_Ludwig = 7616
    BossDead_LivingFailures = 7617
    BossDead_LadyMaria = 7618
    BossDead_Laurence = 7619
    BossDead_OrphanOfKos = 7620
    BossDead_Gehrman = 7621
    BossDead_MoonPresence = 7622


class BossRushWarpPoints(SpawnPointEvent):
    HuntersDream = 2102950  # Normal start position.
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
