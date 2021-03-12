"""
TODO:
    - Swap Bells for Hunter's Mark. (Use another rune for the Chaos version.)
    - Foxy mentioned that the passage to Queen Annalise behind Logarius was open.
        - Could be an isolated thing. Have tried to fix.
    - Spawn point was also set by Logarius fight? Ah, warp must change respawn. Need to set it on every map load...
        - Actually, maybe KEEP that spawn point unless it's a boss rush.
        - Also, if not a boss rush, refresh vials/bullets on map load.
"""


from soulstruct.game_types import *


class BossRushFlags(Flag):
    """BOSS RUSH MOD FLAGS.

    These flags apparently HAVE to replace existing flags; any invalid flags seem to be "always on", and using invalid
    event IDs just crashes the game (Lance's build at least).

    Common event 7200 (22 slots) is used to control the lanterns and request warps.
        This replaces vanilla event 7200, which controlled standard lantern warping behavior.
    Common event 9360 (22 slots) is used to execute warps to bosses.
        This replaces vanilla event 9360, which awarded Blood Dregs after killing other Hunter NPCs.
    Event 6680 listens for the Story Boss Rush bell request.
    Event 6681 listens for the Random Boss Rush bell request.
    Event 6682 is the boss rush completion monitoring event.
    Event 6683 is the story boss order choice event.
    Event 6684 is the random boss order choice event.
    Event 6685 is used to warp back to the Hunter's Dream.
    """
    RequestDreamReturn = 6686
    BossRushActive = 6687
    BossRushCompleted = 6688
    MoonPresenceRequested = 6689
    BossRushRandomized = 6690

    # Boss warp requests ignored while this flag is enabled (during random search).
    ChoosingRandomBoss = 6691

    # Boss warp request flags, which trigger warps immediately when activated.
    #   These replace slots 0-21 of vanilla event 5500, which monitored possession of Uncanny/Lost DLC weapons.
    #   (Complete coincidence that exactly 22 slots were available - the number of non-Chalice bosses.)
    RequestBoss_ClericBeast = 5500
    RequestBoss_FatherGascoigne = 5501
    RequestBoss_BloodStarvedBeast = 5502
    RequestBoss_WitchesOfHemwick = 5503
    RequestBoss_VicarAmelia = 5504
    RequestBoss_DarkbeastPaarl = 5505
    RequestBoss_ShadowsOfYharnam = 5506
    RequestBoss_Rom = 5507
    RequestBoss_Amygdala = 5508
    RequestBoss_MartyrLogarius = 5509
    RequestBoss_TheOneReborn = 5510
    RequestBoss_CelestialEmissary = 5511
    RequestBoss_Ebrietas = 5512
    RequestBoss_Micolash = 5513
    RequestBoss_MergosWetNurse = 5514
    RequestBoss_Ludwig = 5515
    RequestBoss_LivingFailures = 5516
    RequestBoss_LadyMaria = 5517
    RequestBoss_Laurence = 5518
    RequestBoss_OrphanOfKos = 5519
    RequestBoss_Gehrman = 5520
    RequestBoss_MoonPresence = 5521

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

    MicolashDyingWordsDone = 72600301  # disabled when his battle starts

    FirstTimeDone_ClericBeast = 12411702
    FirstTimeDone_FatherGascoigne = 12411802
    FirstTimeDone_BloodStarvedBeast = 12301802
    FirstTimeDone_WitchesOfHemwick = 12201802
    FirstTimeDone_VicarAmelia = 12401802
    FirstTimeDone_DarkbeastPaarl = 12301702
    FirstTimeDone_ShadowsOfYharnam = 12701802
    FirstTimeDone_Rom = 13201802
    FirstTimeDone_Amygdala = 13301802
    FirstTimeDone_MartyrLogarius = 12501802
    FirstTimeDone_TheOneReborn = 12801802
    FirstTimeDone_CelestialEmissary = 12421702
    FirstTimeDone_Ebrietas = 12421802
    FirstTimeDone_Micolash = 12601852
    FirstTimeDone_MergosWetNurse = 12601802
    FirstTimeDone_Ludwig = 13401801
    FirstTimeDone_LivingFailures = 13501851
    FirstTimeDone_LadyMaria = 13501801
    FirstTimeDone_Laurence = 13401851
    FirstTimeDone_OrphanOfKos = 13601801
    # No first-time flags for Gehrman or Moon Presence (events stripped).


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
    BossRushReward = 10000
    Bells = 10010


class BossRushGoods(GoodParam):
    QuicksilverBullet = 900
    BloodBullet = 901
    BloodVial = 1000


class BossRushEffects(SpecialEffectParam):
    StoryRushRequest = 9500
    RandomRushRequest = 9501
