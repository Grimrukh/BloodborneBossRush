"""HUNTER'S DREAM

linked:
164

strings:
0: PC情報_拠点到達時
22: ボス_撃破
34: PC情報_ボス撃破_拠点ボス
64: ボス_戦闘開始
80: ボス_撃破時間
96: PC情報_ボス撃破_拠点ボス2
128: ボス_戦闘開始2
146: ボス_撃破時間2
164: N:\\SPRJ\\data\\Param\\event\\common.emevd
"""
from soulstruct.bloodborne.events import *
from .anims import c9020
from .common_entities import *
from .m21_00_entities import *
from .boss_rush_entities import *


def Constructor():
    """ 0: Event 0 """
    BossRushFirstArrival()

    SkipLinesIfClient(2)
    SkipLinesIfFlagOff(1, 6600)
    EnableFlag(12101999)

    SkipLinesIfFlagOn(1, 12101999)
    DisableObject(2101100)

    SetNetworkUpdateRate(Characters.PlainDoll, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(PLAYER, 110, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 111, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 112, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 113, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 114, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 115, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 116, affect_npc_part_hp=False)

    # ALTAR WARPS
    # Disable all main headstone warp request flags.
    DisableFlag(72100100)
    DisableFlag(72100101)
    DisableFlag(72100102)
    DisableFlag(72102110)
    DisableFlag(72102200)
    DisableFlag(72102201)
    DisableFlag(72102300)
    DisableFlag(72102301)
    DisableFlag(72102302)
    DisableFlag(72102400)
    DisableFlag(72102401)
    DisableFlag(72102410)
    DisableFlag(72102411)
    DisableFlag(72102412)
    DisableFlag(72102413)
    DisableFlag(72102420)
    DisableFlag(72102421)
    DisableFlag(72102422)
    DisableFlag(72102500)
    DisableFlag(72102501)
    DisableFlag(72102502)
    DisableFlag(72102600)
    DisableFlag(72102601)
    DisableFlag(72102602)
    DisableFlag(72102603)
    DisableFlag(72102700)
    DisableFlag(72102701)
    DisableFlag(72102800)
    DisableFlag(72102801)
    DisableFlag(72102802)
    DisableFlag(72102803)
    DisableFlag(72103200)
    DisableFlag(72103201)
    DisableFlag(72103202)
    DisableFlag(72103203)
    DisableFlag(72103300)
    DisableFlag(72103301)
    DisableFlag(72103400)
    DisableFlag(72103401)
    DisableFlag(72103402)
    DisableFlag(72103403)
    DisableFlag(72103500)
    DisableFlag(72103501)
    DisableFlag(72103502)
    DisableFlag(72103600)
    DisableFlag(72103601)
    DisableFlag(72103602)
    MonitorWeaponBuffRemovalRequest()
    # Monitor main headstone activation.
    WarpAtHeadstone(1, 72102201, Characters.FrontierMessengers, BossRushWarpPoints.WitchesOfHemwick)
    WarpAtHeadstone(6, 72102301, Characters.YharnamMessengers, BossRushWarpPoints.BloodStarvedBeast)
    WarpAtHeadstone(7, 72102302, Characters.YharnamMessengers, BossRushWarpPoints.DarkbeastPaarl)
    WarpAtHeadstone(11, 72102401, Characters.YharnamMessengers, BossRushWarpPoints.VicarAmelia)
    WarpAtHeadstone(17, 72102412, Characters.YharnamMessengers, BossRushWarpPoints.ClericBeast)
    WarpAtHeadstone(18, 72102413, Characters.YharnamMessengers, BossRushWarpPoints.FatherGascoigne)
    WarpAtHeadstone(21, 72102421, Characters.YharnamMessengers, BossRushWarpPoints.Ebrietas)
    WarpAtHeadstone(22, 72102422, Characters.YharnamMessengers, BossRushWarpPoints.CelestialEmissary)
    WarpAtHeadstone(27, 72102502, Characters.UnseenMessengers, BossRushWarpPoints.MartyrLogarius)
    WarpAtHeadstone(31, 72102601, Characters.NightmareMessengers, BossRushWarpPoints.MergosWetNurse)
    WarpAtHeadstone(32, 72102602, Characters.NightmareMessengers, BossRushWarpPoints.Micolash)
    WarpAtHeadstone(36, 72102701, Characters.FrontierMessengers, BossRushWarpPoints.ShadowsOfYharnam)
    WarpAtHeadstone(41, 72102801, Characters.UnseenMessengers, BossRushWarpPoints.TheOneReborn)
    WarpAtHeadstone(47, 72103202, Characters.FrontierMessengers, BossRushWarpPoints.Rom)
    WarpAtHeadstone(51, 72103301, Characters.NightmareMessengers, BossRushWarpPoints.Amygdala)
    WarpAtHeadstone(57, 72103402, Characters.OldHuntersMessengers, BossRushWarpPoints.Ludwig)
    WarpAtHeadstone(58, 72103403, Characters.OldHuntersMessengers, BossRushWarpPoints.Laurence)
    WarpAtHeadstone(61, 72103501, Characters.OldHuntersMessengers, BossRushWarpPoints.LivingFailures)
    WarpAtHeadstone(62, 72103502, Characters.OldHuntersMessengers, BossRushWarpPoints.LadyMaria)
    WarpAtHeadstone(67, 72103602, Characters.OldHuntersMessengers, BossRushWarpPoints.OrphanOfKos)

    # Chalice altars are disabled.
    DisableFlag(72100420)
    DisableFlag(72100421)
    DisableFlag(72100422)
    DisableFlag(72100423)
    DisableFlag(72100424)
    DisableFlag(72100425)
    DisableFlag(72100426)
    DisableCharacter(Characters.MakeshiftAltar)
    DisableCharacter(Characters.ChaliceAltar1)
    DisableCharacter(Characters.ChaliceAltar2)
    DisableCharacter(Characters.ChaliceAltar3)
    DisableCharacter(Characters.ChaliceAltar4)
    DisableCharacter(Characters.ChaliceAltar5)
    DisableCharacter(Characters.ChaliceAltar6)
    DisableFlag(72100300)
    DisableFlag(72100301)
    DisableFlag(72100302)
    DisableFlag(72100303)
    DisableFlag(72100304)
    DisableFlag(72100305)
    DisableFlag(72100306)
    DisableFlag(72100307)
    DisableFlag(72100308)
    DisableFlag(72100309)

    # AREA SETUP
    InitializeWorkshopAppearance()
    InitializeDreamMusic()

    # GEHRMAN, THE FIRST HUNTER
    GehrmanDies()
    PlayGehrmanDeathSound()
    StartGehrmanBossBattle()
    ControlGehrmanMusic()
    ToggleGehrmanCamera()
    StopGehrmanBossMusic()
    ActivateGehrmanPhaseTwo()
    GehrmanBuffWearsOff()

    # MOON PRESENCE
    MoonPresenceDies()
    PlayMoonPresenceDeathSound()
    StartMoonPresenceBossBattle()
    ControlMoonPresenceMusic()
    ToggleMoonPresenceCamera()
    StopMoonPresenceBossMusic()
    ControlMoonPresenceTail(0, 5, 5, 1, 100, 480, 490, 8000)
    ControlMoonPresenceTail(1, 6, 6, 2, 150, 481, 491, 8010)
    ControlMoonPresenceTail(2, 7, 7, 3, 150, 482, 492, 8030)
    ControlMoonPresenceTail(3, 8, 8, 4, 200, 483, 493, 8020)
    ControlMoonPresenceTail(4, 9, 9, 5, 200, 484, 494, 8040)
    MoonPresenceSinHarvest()

    # GATES / DOORS
    DisplayMessageAtObject(
        0, 7002, Objects.IronGateToField, CommonFlags.WorkshopOnFire, CommonEventTexts.Locked)
    DisplayMessageAtObject(
        1, 7030, Objects.WorkshopFrontDoorClosed, CommonFlags.CentralYharnamVisited, CommonEventTexts.Locked)
    DisplayMessageAtObject(
        2, 7030, Objects.WorkshopBackDoorClosed, CommonFlags.CentralYharnamVisited, CommonEventTexts.Locked)
    DisplayMessageAtObject(
        3, 7030, Objects.WorkshopMiddleDoorClosed, CommonFlags.CentralYharnamVisited, CommonEventTexts.Locked)

    # HEADSTONES
    AnimateHeadstoneMessengers(0, Characters.YharnamMessengers, Flags.YharnamHeadstoneAvailable)
    AnimateHeadstoneMessengers(1, Characters.FrontierMessengers, Flags.FrontierHeadstoneAvailable)
    AnimateHeadstoneMessengers(2, Characters.UnseenMessengers, Flags.UnseenHeadstoneAvailable)
    AnimateHeadstoneMessengers(3, Characters.NightmareMessengers, Flags.NightmareHeadstoneAvailable)
    AnimateOldHuntersHeadstoneMessengers(3, Characters.OldHuntersMessengers, Flags.OldHuntersHeadstoneAvailable)
    EnableFlag(Flags.YharnamHeadstoneAvailable)  # All headstones are available.
    EnableFlag(Flags.FrontierHeadstoneAvailable)
    EnableFlag(Flags.UnseenHeadstoneAvailable)
    EnableFlag(Flags.NightmareHeadstoneAvailable)
    EnableFlag(Flags.OldHuntersHeadstoneAvailable)

    # BATH MESSENGERS
    InitializeBathMessengers()
    # No `BathMessengerAppearance` events (all of them are enabled by default).

    InitializeStoryProgressionFlags()  # TODO: I don't think I need this.

    InitializeInsightShop()

    # Gift messengers are all disabled/hidden.
    OfferMeleeWeaponGift()
    OfferGunGift()
    OfferNotebookGift()
    OfferBeckoningBellGift()
    OfferOldHunterBellGift()
    OfferDLCAccessGift()

    # CHALICE DUNGEONS ALTARS (controls appearance, will never do anything here)
    InitializeMakeshiftAltar()
    InitializeChaliceAltar1()
    InitializeChaliceAltar2()
    InitializeChaliceAltar3()
    InitializeChaliceAltar4()
    InitializeChaliceAltar5()
    InitializeChaliceAltar6()

    # PLAIN DOLL
    InitializePlainDoll()
    Event12105200()
    Event12100115()
    Event12100116()
    Event12100117()
    Event12100120()
    Event12100121()
    Event12100123()
    Event12100112()
    Event12100113()
    Event12100114()

    # GEHRMAN (ALLY) is disabled.
    DisableCharacter(Characters.GehrmanAlly)
    DisableObject(Objects.WorkshopFrontDoorClosed)
    EnableObject(Objects.WorkshopFrontDoorOpen)
    DisableObject(Objects.WorkshopBackDoorClosed)
    EnableObject(Objects.WorkshopBackDoorOpen)
    DisableObject(Objects.WorkshopMiddleDoorClosed)
    EnableObject(Objects.WorkshopMiddleDoorOpen)
    UnknownSoapstoneMessages()  # disabled

    # STUMP MESSENGERS are disabled.
    DisableCharacter(Characters.StumpMessengers)
    DisableCharacter(Characters.NearStumpMessengers)

    # MULTIPLAYER (probably)
    Event12101100()
    Event12105300()
    AddSpecialEffect(PLAYER, Effects.InvaderBellsDisabled, affect_npc_part_hp=False)
    # SkipLinesIfFlagOn(1, Flags.GehrmanRefusalCutsceneDone)
    AddSpecialEffect(PLAYER, Effects.SummonBellsDisabled, affect_npc_part_hp=False)
    Event12100330()


def Preconstructor():
    """ 50: Event 50 """
    SkipLinesIfFlagOff(2, Flags.MeleeWeaponGiftReceived)
    DisableBackread(Characters.MeleeWeaponGiftMessengers)
    DisableBackread(Characters.MeleeWeaponGift)

    SkipLinesIfFlagOff(2, Flags.GunGiftReceived)
    DisableBackread(Characters.GunGiftMessengers)
    DisableBackread(Characters.GunGift)

    SkipLinesIfFlagOn(2, CommonFlags.WorkshopOnFire)
    DisableBackread(Characters.GehrmanBoss)
    DisableBackread(Characters.MoonPresence)

    SkipLinesIfFlagOn(1, Flags.GehrmanRefusalCutsceneDone)
    EnableFlag(2100)

    GotoIfFlagOff(Label.L0, 1003)
    DisableFlag(1003)
    DisableFlag(72100110)
    DisableFlag(72100111)
    DisableFlag(72100112)
    DisableFlag(72100113)
    DisableFlag(72100114)
    GotoIfFlagOff(Label.L1, CommonFlags.WorkshopOnFire)
    EnableFlag(1002)
    Goto(Label.L0)

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(1000)

    # --- 0 --- #
    DefineLabel(0)
    RunEvent(12100100, slot=0, args=(1000, 1019))
    RunEvent(12100101, slot=0, args=(1000, 1019))
    RunEvent(12100140, slot=0, args=(1020, 1039))
    RunEvent(12100141, slot=0, args=(1020, 1039))
    RunEvent(12100142, slot=0, args=(1020, 1039))
    RunEvent(12100143, slot=0, args=(1020, 1039))
    RunEvent(12100144, slot=0, args=(1020, 1039))
    RunEvent(12100145, slot=0, args=(1020, 1039))
    Event12100146()

    # NOTE: All character IDs I haven't replaced here do not exist in the MSB!
    DisableAnimations(Characters.StoragePrompt)
    DisableAnimations(Characters.UpgradePrompt)
    DisableAnimations(2100202)
    DisableAnimations(Characters.MemoryAltarPrompt)
    DisableAnimations(Characters.BathShopMessengers1)
    DisableAnimations(Characters.BathShopMessengers2)
    # `BathShopMessengers3` (2100213) is not included in this big disabling list for some reason.
    DisableAnimations(Characters.InsightShopMessengers2)  # has ID 2100219
    DisableAnimations(Characters.InsightShopMessengers1)
    DisableAnimations(Characters.MeleeWeaponGiftMessengers)
    DisableAnimations(Characters.GunGiftMessengers)
    DisableAnimations(2100217)
    DisableAnimations(Characters.StumpMessengers)
    DisableAnimations(Characters.MeleeWeaponGift)
    DisableAnimations(Characters.GunGift)
    DisableAnimations(2100222)
    DisableAnimations(Characters.BellGiftMessengers)
    DisableAnimations(Characters.OldHuntersMessengers)
    DisableAnimations(Characters.YharnamMessengers)
    DisableAnimations(Characters.FrontierMessengers)
    DisableAnimations(Characters.UnseenMessengers)
    DisableAnimations(Characters.NightmareMessengers)
    DisableAnimations(Characters.MakeshiftAltar)
    DisableAnimations(Characters.ChaliceAltar1)
    DisableAnimations(Characters.ChaliceAltar2)
    DisableAnimations(Characters.ChaliceAltar3)
    DisableAnimations(Characters.ChaliceAltar4)
    DisableAnimations(Characters.ChaliceAltar5)
    DisableAnimations(Characters.ChaliceAltar6)
    DisableGravity(Characters.StoragePrompt)
    DisableGravity(Characters.UpgradePrompt)
    DisableGravity(2100202)
    DisableGravity(Characters.MemoryAltarPrompt)
    DisableGravity(Characters.BathShopMessengers1)
    DisableGravity(Characters.BathShopMessengers2)
    DisableGravity(Characters.InsightShopMessengers2)
    DisableGravity(Characters.InsightShopMessengers1)
    DisableGravity(Characters.MeleeWeaponGiftMessengers)
    DisableGravity(Characters.GunGiftMessengers)
    DisableGravity(2100217)
    DisableGravity(Characters.StumpMessengers)
    DisableGravity(Characters.MeleeWeaponGift)
    DisableGravity(Characters.GunGift)
    DisableGravity(2100222)
    DisableGravity(Characters.BellGiftMessengers)
    DisableGravity(Characters.OldHuntersMessengers)
    DisableGravity(Characters.YharnamMessengers)
    DisableGravity(Characters.FrontierMessengers)
    DisableGravity(Characters.UnseenMessengers)
    DisableGravity(Characters.NightmareMessengers)
    DisableGravity(Characters.MakeshiftAltar)
    DisableGravity(Characters.ChaliceAltar1)
    DisableGravity(Characters.ChaliceAltar2)
    DisableGravity(Characters.ChaliceAltar3)
    DisableGravity(Characters.ChaliceAltar4)
    DisableGravity(Characters.ChaliceAltar5)
    DisableGravity(Characters.ChaliceAltar6)
    DisableCharacterCollision(Characters.StoragePrompt)
    DisableCharacterCollision(Characters.UpgradePrompt)
    DisableCharacterCollision(2100202)
    DisableCharacterCollision(Characters.MemoryAltarPrompt)
    DisableCharacterCollision(Characters.BathShopMessengers1)
    DisableCharacterCollision(Characters.BathShopMessengers2)
    DisableCharacterCollision(Characters.InsightShopMessengers2)
    DisableCharacterCollision(Characters.InsightShopMessengers1)
    DisableCharacterCollision(Characters.MeleeWeaponGiftMessengers)
    DisableCharacterCollision(Characters.GunGiftMessengers)
    DisableCharacterCollision(2100217)
    DisableCharacterCollision(Characters.StumpMessengers)
    DisableCharacterCollision(Characters.MeleeWeaponGift)
    DisableCharacterCollision(Characters.GunGift)
    DisableCharacterCollision(2100222)
    DisableCharacterCollision(Characters.BellGiftMessengers)
    DisableCharacterCollision(Characters.OldHuntersMessengers)
    DisableCharacterCollision(Characters.YharnamMessengers)
    DisableCharacterCollision(Characters.FrontierMessengers)
    DisableCharacterCollision(Characters.UnseenMessengers)
    DisableCharacterCollision(Characters.NightmareMessengers)
    DisableCharacterCollision(Characters.MakeshiftAltar)
    DisableCharacterCollision(Characters.ChaliceAltar1)
    DisableCharacterCollision(Characters.ChaliceAltar2)
    DisableCharacterCollision(Characters.ChaliceAltar3)
    DisableCharacterCollision(Characters.ChaliceAltar4)
    DisableCharacterCollision(Characters.ChaliceAltar5)
    DisableCharacterCollision(Characters.ChaliceAltar6)
    SkipLinesIfFlagOff(2, 12411000)
    DisableBackread(Characters.GehrmanBoss)
    DisableBackread(Characters.MoonPresence)


def Event12100100(_, arg_0_3: int, arg_4_7: int):
    """ 12100100: Event 12100100 """
    IfFlagOff(1, 1003)
    IfFlagOn(1, CommonFlags.WorkshopOnFire)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1002)


def Event12100101(_, arg_0_3: int, arg_4_7: int):
    """ 12100101: Event 12100101 """
    IfCharacterDead(0, Characters.PlainDoll)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1003)
    SaveRequest()


def InitializePlainDoll():
    """ 12100110: Event 12100110 """
    DisableFlag(72100105)
    DisableFlag(72100106)
    DisableFlag(72100107)
    DisableFlag(12100510)

    # Doll is never disabled from lack of insight or first-time visit.

    EnableFlag(12100105)
    EnableFlag(9404)
    IfFlagOn(1, 13501800)
    IfFlagOff(1, 72100116)
    IfConditionTrue(-2, input_condition=1)
    IfFlagOn(2, 13601800)
    IfFlagOff(2, 72100117)
    IfFlagOn(-3, 1026)
    IfFlagOn(-3, 1027)
    IfConditionTrue(2, input_condition=-3)
    IfConditionTrue(-2, input_condition=2)
    EndIfConditionTrue(-2)
    EndIfFlagOn(1000)
    GotoIfFlagOn(Label.L0, 1001)
    EndIfFlagOn(1002)
    GotoIfFlagOn(Label.L4, 1003)

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfFlagOn(2, 100)
    DisableFlagRange((12100500, 12100509))
    EnableRandomFlagInRange((12100500, 12100509))
    SkipLinesIfFlagOff(1, Flags.OldHuntersHeadstoneAvailable)
    DisableFlagRange((12100501, 12100502))
    GotoIfFlagOn(Label.L1, 12100500)
    GotoIfFlagOn(Label.L2, 12100501)
    GotoIfFlagOn(Label.L3, 12100502)
    End()

    # --- 1 --- #
    DefineLabel(1)
    Move(Characters.PlainDoll, destination=2102301, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(Characters.PlainDoll, 9009, loop=True)
    Goto(Label.L8)

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(12100510)
    Move(Characters.PlainDoll, destination=2102302, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(Characters.PlainDoll, 9000, loop=True)
    Goto(Label.L8)

    # --- 3 --- #
    DefineLabel(3)
    EnableFlag(12100510)
    SkipLinesIfFlagOn(2, 6600)
    DisableFlag(12100502)
    End()
    Move(Characters.PlainDoll, destination=2102303, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(Characters.PlainDoll, 9000, loop=True)
    Goto(Label.L8)

    # --- 4 --- #
    DefineLabel(4)
    GotoIfFlagOn(Label.L5, 12100500)
    GotoIfFlagOn(Label.L6, 12100501)
    GotoIfFlagOn(Label.L7, 12100502)
    Move(Characters.PlainDoll, destination=2102300, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(Characters.PlainDoll)
    End()

    # --- 5 --- #
    DefineLabel(5)
    Move(Characters.PlainDoll, destination=2102301, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(Characters.PlainDoll)
    End()

    # --- 6 --- #
    DefineLabel(6)
    Move(Characters.PlainDoll, destination=2102302, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(Characters.PlainDoll)
    End()

    # --- 7 --- #
    DefineLabel(7)
    Move(Characters.PlainDoll, destination=2102303, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(Characters.PlainDoll)
    End()

    # --- 8 --- #
    DefineLabel(8)
    DollDoesSomething()
    End()

    # --- 9 --- #
    DefineLabel(9)
    Move(Characters.PlainDoll, destination=2102304, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(Characters.PlainDoll, 9011, loop=True)
    EnableFlag(12105100)


def DollDoesSomething():
    """ 12100111: Event 12100111 """
    GotoIfFlagOn(Label.L0, 12100500)
    GotoIfFlagOn(Label.L1, 12100501)
    GotoIfFlagOn(Label.L1, 12100502)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(72100105)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EndIfFlagOff(BossRushFlags.BossRushCompleted)  # Doll does something.
    SkipLinesIfFlagOn(3, 102)
    DisableFlagRange((12100520, 12100524))
    EnableRandomFlagInRange((12100520, 12100524))
    EndIfFlagOff(12100520)
    EnableFlag(72100105)
    End()


def Event12100112():
    """ 12100112: Event 12100112 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, 72100100)
    GotoIfFlagOn(Label.L0, 1003)
    GotoIfFlagOn(Label.L1, 12105100)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, Characters.PlainDoll, radius=1.0)
    GotoIfConditionTrue(Label.L2, input_condition=1)
    RotateToFaceEntity(PLAYER, Characters.PlainDoll, animation=101290, wait_for_completion=False)
    IfCharacterHuman(2, PLAYER)
    IfEntityWithinDistance(2, PLAYER, Characters.PlainDoll, radius=1.0)
    IfConditionTrue(-1, input_condition=2)
    IfFramesElapsed(-1, 89)
    IfConditionTrue(0, input_condition=-1)

    # --- 2 --- #
    DefineLabel(2)
    RotateToFaceEntity(PLAYER, Characters.PlainDoll, animation=101270, wait_for_completion=False)
    WaitFrames(0)
    EnableFlag(72100101)
    WaitFrames(54)
    IfFlagOff(0, 72100100)
    ForceAnimation(PLAYER, 101272)
    WaitFrames(19)
    DisableFlag(72100101)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(3, PLAYER)
    IfEntityWithinDistance(3, PLAYER, Characters.PlainDoll, radius=1.5)
    GotoIfConditionTrue(Label.L3, input_condition=3)
    RotateToFaceEntity(PLAYER, Characters.PlainDoll, animation=101290, wait_for_completion=False)
    IfCharacterHuman(4, PLAYER)
    IfEntityWithinDistance(4, PLAYER, Characters.PlainDoll, radius=1.5)
    IfConditionTrue(-2, input_condition=4)
    IfFramesElapsed(-2, 89)
    IfConditionTrue(0, input_condition=-2)

    # --- 3 --- #
    DefineLabel(3)
    RotateToFaceEntity(PLAYER, Characters.PlainDoll, animation=101280, wait_for_completion=False)
    WaitFrames(0)
    EnableFlag(72100101)
    WaitFrames(54)
    IfFlagOff(0, 72100100)
    ForceAnimation(PLAYER, 101282)
    WaitFrames(25)
    DisableFlag(72100101)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterHuman(5, PLAYER)
    IfEntityWithinDistance(5, PLAYER, Characters.PlainDoll, radius=2.0)
    GotoIfConditionTrue(Label.L4, input_condition=5)
    RotateToFaceEntity(PLAYER, Characters.PlainDoll, animation=101290, wait_for_completion=False)
    IfCharacterHuman(6, PLAYER)
    IfEntityWithinDistance(6, PLAYER, Characters.PlainDoll, radius=2.0)
    IfConditionTrue(0, input_condition=6)

    # --- 4 --- #
    DefineLabel(4)
    RotateToFaceEntity(PLAYER, Characters.PlainDoll, animation=101270, wait_for_completion=False)
    WaitFrames(0)
    EnableFlag(72100101)
    WaitFrames(54)
    IfFlagOff(0, 72100100)
    ForceAnimation(PLAYER, 101272)
    WaitFrames(19)
    DisableFlag(72100101)
    Restart()


def Event12100113():
    """ 12100113: Event 12100113 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    WaitFrames(1)
    IfHealthEqual(-1, Characters.PlainDoll, 0.0)
    IfFlagOn(-1, 12105100)
    GotoIfConditionFalse(Label.L0, input_condition=-1)
    EnableFlag(72100102)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOn(0, 72100100)
    RotateToFaceEntity(Characters.PlainDoll, PLAYER, animation=7021, wait_for_completion=False)
    WaitFrames(0)
    EnableFlag(72100102)
    WaitFrames(89)
    ForceAnimation(Characters.PlainDoll, 9010, loop=True)
    IfFlagOff(0, 72100100)
    ForceAnimation(Characters.PlainDoll, 7020)
    DisableFlag(72100102)
    WaitFrames(92)
    Restart()


def Event12100114():
    """ 12100114: Event 12100114 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, 7500)
    CreateTemporaryVFX(178, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=1)
    DisableFlag(7500)
    Restart()


def Event12100115():
    """ 12100115: Event 12100115 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    WaitFrames(2)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, Characters.PlainDoll, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    IfHealthEqual(-1, Characters.PlainDoll, 0.0)
    IfFlagOn(-1, 12105100)
    IfFlagOn(-1, 72100105)
    EndIfConditionTrue(-1)
    IfCharacterHasSpecialEffect(2, Characters.PlainDoll, 151)
    GotoIfConditionFalse(Label.L0, input_condition=2)
    RotateToFaceEntity(Characters.PlainDoll, PLAYER, animation=7010, wait_for_completion=False)
    WaitFrames(89)
    IfCharacterHasSpecialEffect(3, Characters.PlainDoll, 152)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    RotateToFaceEntity(Characters.PlainDoll, PLAYER, animation=7012, wait_for_completion=False)
    WaitFrames(0)

    # --- 0 --- #
    DefineLabel(0)
    Wait(0.0)


def Event12100116():
    """ 12100116: Event 12100116 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, 72100108)
    DisableFlag(72100108)
    IfCharacterHasSpecialEffect(1, Characters.PlainDoll, 151)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    RotateToFaceEntity(Characters.PlainDoll, PLAYER, animation=7011, wait_for_completion=False)
    WaitFrames(89)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHasSpecialEffect(2, Characters.PlainDoll, 152)
    GotoIfConditionFalse(Label.L1, input_condition=2)
    RotateToFaceEntity(Characters.PlainDoll, PLAYER, animation=7013, wait_for_completion=False)
    WaitFrames(0)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterHasSpecialEffect(3, Characters.PlainDoll, 153)
    GotoIfConditionFalse(Label.L2, input_condition=3)
    RotateToFaceEntity(Characters.PlainDoll, PLAYER, animation=7019, wait_for_completion=False)
    WaitFrames(89)

    # --- 2 --- #
    DefineLabel(2)
    Wait(0.0)


def Event12100117():
    """ 12100117: Event 12100117 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, Characters.PlainDoll, 160)
    IfFlagOn(1, 12100118)
    IfCharacterHuman(1, PLAYER)
    IfCharacterHasSpecialEffect(2, PLAYER, 161)
    IfCharacterHasSpecialEffect(3, PLAYER, 162)
    IfCharacterHasSpecialEffect(4, PLAYER, 163)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=3)
    RotateToFaceEntity(Characters.PlainDoll, PLAYER, animation=7001, wait_for_completion=False)
    WaitFrames(1)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    RotateToFaceEntity(Characters.PlainDoll, PLAYER, animation=7000, wait_for_completion=False)
    WaitFrames(1)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    RotateToFaceEntity(Characters.PlainDoll, PLAYER, animation=7026, wait_for_completion=False)
    WaitFrames(39)
    RotateToFaceEntity(Characters.PlainDoll, PLAYER, animation=7025, wait_for_completion=False)
    Restart()


def Event12100120():
    """ 12100120: Event 12100120 """
    EndIfThisEventOn()


def Event12100121():
    """ 12100121: Event 12100121 """
    IfPlayerHasGood(0, Goods.SmallHairOrnament, including_box=True)
    EnableFlag(12100122)
    IfPlayerDoesNotHaveGood(0, Goods.SmallHairOrnament, including_box=True)
    DisableFlag(12100122)
    Restart()


def Event12100123():
    """ 12100123: Event 12100123 """
    DisableNetworkSync()
    EndIfThisEventOn()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(72100114)
    IfCharacterHasSpecialEffect(1, Characters.PlainDoll, 160)
    IfFlagOn(1, 72100114)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(Characters.PlainDoll, 7030)
    IfFlagOn(0, 72100112)
    AwardItemLot(ItemLots.DollGift, host_only=False)
    RemoveGoodFromPlayer(Goods.SmallHairOrnament, quantity=1)


def Event12100140(_, arg_0_3: int, arg_4_7: int):
    """ 12100140: Event 12100140 """
    IfFlagOn(1, 1020)
    IfFlagOn(1, CommonFlags.CentralYharnamVisited)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1021)


def Event12100141(_, arg_0_3: int, arg_4_7: int):
    """ 12100141: Event 12100141 """
    IfFlagOn(1, 1022)
    IfFlagOn(1, 9800)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1023)


def Event12100142(_, arg_0_3: int, arg_4_7: int):
    """ 12100142: Event 12100142 """
    IfFlagOn(1, 1024)
    IfFlagOn(-1, 12301800)
    IfFlagOn(-1, 9801)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1025)


def Event12100143(_, arg_0_3: int, arg_4_7: int):
    """ 12100143: Event 12100143 """
    IfFlagOff(1, 1029)
    IfFlagOff(1, 1030)
    IfFlagOn(1, CommonFlags.WorkshopOnFire)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1028)


def Event12100144(_, arg_0_3: int, arg_4_7: int):
    """ 12100144: Event 12100144 """
    IfFlagOff(1, 1030)
    IfFlagOn(1, Flags.GehrmanRefusalCutsceneDone)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1029)
    SaveRequest()


def Event12100145(_, arg_0_3: int, arg_4_7: int):
    """ 12100145: Event 12100145 """
    IfFlagOn(0, Flags.GehrmanDead)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1030)
    SaveRequest()


def Event12100146():
    """ 12100146: Event 12100146 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    SetDistanceLimitForConversationStateChanges(Characters.GehrmanBoss, distance=17.0)
    IfFlagOn(0, 1029)
    SetDistanceLimitForConversationStateChanges(Characters.GehrmanBoss, distance=80.0)


def Event12100161():
    """ 12100161: Event 12100161 """
    IfFlagOn(1, 13601800)
    IfFlagOff(1, 72100117)
    EndIfConditionTrue(1)
    GotoIfFlagOn(Label.L1, 1027)
    GotoIfFlagOn(Label.L0, 1026)
    SkipLinesIfFlagOn(2, 100)
    EnableRandomFlagInRange((12105800, 12105804))
    EndIfFlagOff(12105800)
    EnableFlag(72100133)
    EnableCharacter(Characters.GehrmanAlly)
    ForceAnimation(Characters.GehrmanAlly, 9000, loop=True)
    Move(Characters.GehrmanAlly, destination=2102311, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfFlagOn(2, 100)
    EnableRandomFlagInRange((12105800, 12105809))
    EndIfFlagOff(12105800)
    EnableFlag(72100133)
    EnableCharacter(Characters.GehrmanAlly)
    ForceAnimation(Characters.GehrmanAlly, 9000, loop=True)
    Move(Characters.GehrmanAlly, destination=2102311, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagOn(2, 100)
    EnableRandomFlagInRange((12105800, 12105809))
    EndIfFlagOff(12105800)
    EnableFlag(72100133)
    EnableCharacter(Characters.GehrmanAlly)
    ForceAnimation(Characters.GehrmanAlly, 9000, loop=True)
    Move(Characters.GehrmanAlly, destination=2102311, destination_type=CoordEntityType.Region, short_move=True)


def UnknownSoapstoneMessages():
    """ 12100164: Event 12100164 """
    DisableSoapstoneMessage(2103000)
    DisableSoapstoneMessage(2103001)


def InitializeWorkshopAppearance():
    """ 12100300: Workshop is never on fire. Blood Moon is enabled if boss rush is completed (NG+ available). """
    DeleteVFX(2103300, erase_root_only=False)  # Workshop fire FX.
    DeleteVFX(2103500, erase_root_only=False)
    DeleteVFX(2103501, erase_root_only=False)
    DeleteVFX(2103502, erase_root_only=False)
    DeleteVFX(2103503, erase_root_only=False)
    DeleteVFX(2103504, erase_root_only=False)
    DeleteVFX(2103505, erase_root_only=False)
    DeleteVFX(2103506, erase_root_only=False)
    DeleteVFX(2103507, erase_root_only=False)

    GotoIfFlagOn(Label.L0, BossRushFlags.BossRushCompleted)

    # Boss rush not completed.
    EnableObject(Objects.NormalMoonSky)
    DisableObject(Objects.BloodMoonSky)
    EnableObject(Objects.NormalMoon)
    DisableObject(Objects.BloodMoon)
    End()

    # --- 0 --- # Boss rush completed.
    DisableObject(Objects.NormalMoonSky)
    EnableObject(Objects.BloodMoonSky)
    DisableObject(Objects.NormalMoon)
    EnableObject(Objects.BloodMoon)


def InitializeDreamMusic():
    """ 12100310: Play special music if boss rush is completed, or player has 50 insight. """
    IfPlayerInsightAmountGreaterThanOrEqual(-1, 50)
    IfFlagOn(-1, BossRushFlags.BossRushCompleted)
    GotoIfConditionTrue(Label.L0, input_condition=-1)
    EnableSoundEvent(Music.NormalMusic)
    DisableSoundEvent(Music.BloodMoonMusic)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableSoundEvent(Music.NormalMusic)
    EnableSoundEvent(Music.BloodMoonMusic)
    End()


def Event12100330():
    """ 12100330: Event 12100330 """
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfFlagOn(-1, 5051)
    IfFlagOn(-1, 6660)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(5051)
    EnableFlag(6660)


def Event12100350(_, arg_0_3: int, arg_4_7: int):
    """ 12100350: UNUSED (no chests in Hunter's Dream). """
    GotoIfThisEventSlotOff(Label.L0)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def DisplayMessageAtObject(_, action_button_id: int, obj: int, manual_trigger_flag: int, message: int):
    """ 12100410: Display a message if an object is activated or a certain flag enabled. """
    DisableNetworkSync()
    IfActionButtonParam(-1, action_button_id=action_button_id, entity=obj)
    IfFlagOn(-1, manual_trigger_flag)
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagOn(manual_trigger_flag)
    DisplayDialog(
        message,
        anchor_entity=obj,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def MonitorToolAndBadgePossessionForNewGamePlus():
    """ 12100450: Enables appropriate flags if player has tools/badges in their inventory.

    Only called after an ending cutscene, hence why it's probably for NG+.
    """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfPlayerDoesNotHaveGood(1, Goods.BloodGemWorkshopTool, including_box=False)
    SkipLinesIfConditionTrue(1, 1)
    EnableFlag(6630)
    IfPlayerDoesNotHaveGood(2, Goods.RuneWorkshopTool, including_box=False)
    SkipLinesIfConditionTrue(1, 2)
    EnableFlag(6631)
    IfPlayerDoesNotHaveGood(3, Goods.ShortRitualRootChalice, including_box=False)
    SkipLinesIfConditionTrue(1, 3)
    EnableFlag(6632)
    IfPlayerDoesNotHaveGood(4, Goods.WorkshopHazeExtractor, including_box=False)
    SkipLinesIfConditionTrue(1, 4)
    EnableFlag(6633)
    IfPlayerDoesNotHaveGood(5, Goods.SawHunterBadge, including_box=False)
    SkipLinesIfConditionTrue(1, 5)
    EnableFlag(6640)
    IfPlayerDoesNotHaveGood(6, Goods.PowderKegHunterBadge, including_box=False)
    SkipLinesIfConditionTrue(1, 6)
    EnableFlag(6641)
    IfPlayerDoesNotHaveGood(7, Goods.OldHunterBadge, including_box=False)
    SkipLinesIfConditionTrue(1, 7)
    EnableFlag(6642)
    IfPlayerDoesNotHaveGood(8, Goods.CrowHunterBadge, including_box=False)
    SkipLinesIfConditionTrue(1, 8)
    EnableFlag(6643)
    IfPlayerDoesNotHaveGood(9, Goods.SparkHunterBadge, including_box=False)
    SkipLinesIfConditionTrue(1, 9)
    EnableFlag(6644)
    IfPlayerDoesNotHaveGood(10, Goods.SwordHunterBadge, including_box=False)
    SkipLinesIfConditionTrue(1, 10)
    EnableFlag(6645)
    IfPlayerDoesNotHaveGood(11, Goods.RadiantSwordHunterBadge, including_box=False)
    SkipLinesIfConditionTrue(1, 11)
    EnableFlag(6646)
    IfPlayerDoesNotHaveGood(12, Goods.WheelHunterBadge, including_box=False)
    SkipLinesIfConditionTrue(1, 12)
    EnableFlag(6647)
    IfPlayerDoesNotHaveGood(13, Goods.CosmicEyeWatcherBadge, including_box=False)
    SkipLinesIfConditionTrue(1, 13)
    EnableFlag(6648)
    IfPlayerDoesNotHaveGood(14, Goods.CainhurstBadge, including_box=False)
    SkipLinesIfConditionTrue(1, 14)
    EnableFlag(6649)
    End()


def Event12100451():
    """ 12100451: Event 12100451 """
    DisableNetworkSync()
    EndIfClient()
    IfFlagOn(1, 50000400)
    SkipLinesIfConditionFalse(1, 1)
    EnableFlag(6300)
    IfFlagOn(2, 50000600)
    SkipLinesIfConditionFalse(1, 2)
    EnableFlag(6301)
    IfFlagOn(3, 50000800)
    SkipLinesIfConditionFalse(1, 3)
    EnableFlag(6302)
    IfFlagOn(4, 50001100)
    SkipLinesIfConditionFalse(1, 4)
    EnableFlag(6303)
    IfFlagOn(5, 50001300)
    SkipLinesIfConditionFalse(1, 5)
    EnableFlag(6304)
    IfFlagOn(6, 50001610)
    SkipLinesIfConditionFalse(1, 6)
    EnableFlag(6305)
    IfFlagOn(7, 50002110)
    SkipLinesIfConditionFalse(1, 7)
    EnableFlag(6306)
    IfFlagOn(8, 50003400)
    SkipLinesIfConditionFalse(1, 8)
    EnableFlag(6307)
    IfFlagOn(9, 50003500)
    SkipLinesIfConditionFalse(1, 9)
    EnableFlag(6308)
    IfFlagOn(10, 52200380)
    SkipLinesIfConditionFalse(1, 10)
    EnableFlag(6309)
    IfFlagOn(11, 52420640)
    SkipLinesIfConditionFalse(1, 11)
    EnableFlag(6310)
    IfFlagOn(12, 52420690)
    SkipLinesIfConditionFalse(1, 12)
    EnableFlag(6311)
    IfFlagOn(13, 52410640)
    SkipLinesIfConditionFalse(1, 13)
    EnableFlag(6312)
    IfFlagOn(14, 52420120)
    SkipLinesIfConditionFalse(1, 14)
    EnableFlag(6313)
    IfFlagOn(15, 52600390)
    SkipLinesIfConditionFalse(1, 15)
    EnableFlag(6314)
    IfFlagOn(-1, 52600300)
    SkipLinesIfConditionFalse(1, -1)
    EnableFlag(6315)
    IfFlagOn(-2, 52700180)
    SkipLinesIfConditionFalse(1, -2)
    EnableFlag(6316)
    IfFlagOn(-3, 52700200)
    SkipLinesIfConditionFalse(1, -3)
    EnableFlag(6317)
    IfFlagOn(-4, 52700380)
    SkipLinesIfConditionFalse(1, -4)
    EnableFlag(6318)
    IfFlagOn(-5, 52700540)
    SkipLinesIfConditionFalse(1, -5)
    EnableFlag(6319)
    IfFlagOn(-6, 52700570)
    SkipLinesIfConditionFalse(1, -6)
    EnableFlag(6320)
    IfFlagOn(-7, 52700950)
    SkipLinesIfConditionFalse(1, -7)
    EnableFlag(6321)
    IfFlagOn(-8, 52800050)
    SkipLinesIfConditionFalse(1, -8)
    EnableFlag(6322)
    IfFlagOn(-9, 52800140)
    SkipLinesIfConditionFalse(1, -9)
    EnableFlag(6323)
    IfFlagOn(-10, 52800350)
    SkipLinesIfConditionFalse(1, -10)
    EnableFlag(6324)
    IfFlagOn(-11, 53200010)
    SkipLinesIfConditionFalse(1, -11)
    EnableFlag(6325)
    IfFlagOn(-12, 53200640)
    SkipLinesIfConditionFalse(1, -12)
    EnableFlag(6326)
    IfFlagOn(-13, 53300110)
    SkipLinesIfConditionFalse(1, -13)
    EnableFlag(6327)
    IfFlagOn(-14, 53300150)
    SkipLinesIfConditionFalse(1, -14)
    EnableFlag(6328)
    IfFlagOn(-15, 53300320)
    SkipLinesIfConditionFalse(1, -15)
    EnableFlag(6329)


def Event12100452():
    """ 12100452: Event 12100452 """
    DisableNetworkSync()
    EndIfClient()
    IfFlagOn(1, 53300420)
    SkipLinesIfConditionFalse(1, 1)
    EnableFlag(6330)
    IfFlagOn(2, 53300480)
    SkipLinesIfConditionFalse(1, 2)
    EnableFlag(6331)
    IfFlagOn(3, 9458)
    SkipLinesIfConditionFalse(1, 3)
    EnableFlag(6332)
    IfFlagOn(4, 12400861)
    SkipLinesIfConditionFalse(1, 4)
    EnableFlag(6333)
    IfFlagOn(5, 50003100)
    SkipLinesIfConditionFalse(1, 5)
    EnableFlag(6334)
    IfFlagOn(6, 50001500)
    SkipLinesIfConditionFalse(1, 6)
    EnableFlag(6335)
    IfFlagOn(7, 52605000)
    SkipLinesIfConditionFalse(1, 7)
    EnableFlag(6336)
    IfFlagOn(8, 50000200)
    SkipLinesIfConditionFalse(1, 8)
    EnableFlag(6340)
    IfFlagOn(9, 50001820)
    SkipLinesIfConditionFalse(1, 9)
    EnableFlag(6341)
    IfFlagOn(10, 50001910)
    SkipLinesIfConditionFalse(1, 10)
    EnableFlag(6342)
    IfFlagOn(11, 50002260)
    SkipLinesIfConditionFalse(1, 11)
    EnableFlag(6677)


def GehrmanDies():
    """ 12101800: Gehrman is killed in his boss battle. """
    await Flags.GehrmanBattleStarted
    IfCharacterDead(0, Characters.GehrmanBoss)
    EnableFlag(BossRushFlags.BossDead_Gehrman)
    DisplayBanner(BannerType.PreySlaughtered)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=0)
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, 0, args=(3,))  # TODO: Insight amount for victory?
    # TODO: Leaving play log stuff just in case.
    StopPlayLogMeasurement(2100000)
    StopPlayLogMeasurement(2100001)
    StopPlayLogMeasurement(2100010)
    CreatePlayLog(22)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 34, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 34, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 34, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 34, PlayLogMultiplayerType.HostOnly)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


def PlayGehrmanDeathSound():
    """ 12101801: Play a `CharacterMotion` sound (0) when Gehrman dies. """
    await Flags.GehrmanBattleStarted
    await BossRushFlags.BossDead_Gehrman
    PlaySoundEffect(anchor_entity=Regions.BossFogRotateTarget, sound_type=SoundType.c_CharacterMotion, sound_id=0)


def StartGehrmanBossBattle():
    """ 12104802: Enable Gehrman when trigger region entered. """
    DisableCharacter(Characters.GehrmanAlly)
    DisableCharacter(Characters.GehrmanBoss)

    IfPlayerInsideRegion(1, BossRushTriggers.GehrmanOrMoonPresence)
    IfFlagOn(1, BossRushFlags.RequestBoss_Gehrman)  # Only map that requires this.
    IfFlagOff(1, BossRushFlags.BossDead_Gehrman)
    IfConditionTrue(0, 1)

    DisableFlag(BossRushFlags.RequestBoss_Gehrman)  # Disabled here instead of in common warp event.
    EnableCharacter(Characters.GehrmanBoss)
    EnableBossHealthBar(Characters.GehrmanBoss, name=BossNames.Gehrman, slot=0)
    SetCharacterEventTarget(Characters.GehrmanBoss, 2100801)
    CreatePlayLog(64)
    StartPlayLogMeasurement(2100010, 80, overwrite=True)


def ControlGehrmanMusic():
    """ 12104803: Enables Gehrman music, including second phase. """
    DisableSoundEvent(Music.GehrmanPhase1Music)
    DisableSoundEvent(Music.GehrmanPhase2Music)
    await Flags.GehrmanBattleStarted

    IfFlagOff(1, BossRushFlags.BossDead_Gehrman)
    IfCharacterInsideRegion(1, PLAYER, region=2102802)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(Music.NormalMusic)
    DisableSoundEvent(Music.BloodMoonMusic)
    EnableBossMusic(Music.GehrmanPhase1Music)

    IfHasTAEEvent(0, Characters.GehrmanBoss, tae_event_id=100)

    IfFlagOff(2, BossRushFlags.BossDead_Gehrman)
    IfCharacterInsideRegion(2, PLAYER, region=2102802)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(Music.GehrmanPhase1Music)
    WaitFrames(0)
    EnableBossMusic(Music.GehrmanPhase2Music)


def ToggleGehrmanCamera():
    """ 12104804: Change camera when Gehrman gets closer than 8 units. """
    await Flags.GehrmanBattleStarted
    IfHealthGreaterThan(1, Characters.GehrmanBoss, 0.0)
    IfEntityWithinDistance(1, PLAYER, Characters.GehrmanBoss, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=1)
    IfHealthGreaterThan(2, Characters.GehrmanBoss, 0.0)
    IfEntityBeyondDistance(2, PLAYER, Characters.GehrmanBoss, radius=10.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=0)
    return RESTART


def StopGehrmanBossMusic():
    """ 12104805: Stops boss music as soon as boss health reaches zero. """
    await Flags.GehrmanBattleStarted
    IfFlagOn(0, BossRushFlags.BossDead_Gehrman)
    DisableBossMusic(Music.GehrmanPhase1Music)
    DisableBossMusic(Music.GehrmanPhase2Music)
    DisableBossMusic(-1)


def ActivateGehrmanPhaseTwo():
    """ 12104807: Instructs Gehrman to extend his Burial Blade for phase two. """
    await Flags.GehrmanBattleStarted
    IfHealthLessThan(0, Characters.GehrmanBoss, 0.5)
    AICommand(Characters.GehrmanBoss, command_id=100, slot=0)
    IfHasTAEEvent(0, Characters.GehrmanBoss, tae_event_id=100)
    CancelSpecialEffect(Characters.GehrmanBoss, 5305)
    AICommand(Characters.GehrmanBoss, command_id=-1, slot=0)
    ReplanAI(Characters.GehrmanBoss)
    Wait(0.10000000149011612)
    AICommand(Characters.GehrmanBoss, command_id=1, slot=1)


def GehrmanBuffWearsOff():
    """ 12104808: Educated guess. Waits for TAE event 20 and cancels effect 5526. """
    await Flags.GehrmanBattleStarted
    IfHasTAEEvent(0, Characters.GehrmanBoss, tae_event_id=20)
    CancelSpecialEffect(Characters.GehrmanBoss, 5526)
    Wait(0.10000000149011612)
    Restart()


def MoonPresenceDies():
    """ 12101850: Moon Presence is killed in battle. """
    await Flags.MoonPresenceBattleStarted
    IfCharacterDead(0, Characters.MoonPresence)
    EnableFlag(BossRushFlags.BossDead_MoonPresence)
    EnableFlag(12104859)  # Stops music.
    DisplayBanner(BannerType.NightmareSlain)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=0)
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, 0, args=(5,))
    StopPlayLogMeasurement(2100011)
    CreatePlayLog(22)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 96, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 96, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 96, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 96, PlayLogMultiplayerType.HostOnly)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


def PlayMoonPresenceDeathSound():
    """ 12101851: Event 12101851 """
    await Flags.MoonPresenceBattleStarted
    await BossRushFlags.BossDead_MoonPresence
    PlaySoundEffect(anchor_entity=Regions.BossFogRotateTarget, sound_type=SoundType.c_CharacterMotion, sound_id=0)


def StartMoonPresenceBossBattle():
    """ 12104852: Event 12104852 """
    DisableCharacter(Characters.MoonPresence)

    IfPlayerInsideRegion(1, BossRushTriggers.GehrmanOrMoonPresence)
    IfFlagOn(1, BossRushFlags.RequestBoss_MoonPresence)  # Only map that requires this.
    IfFlagOff(1, BossRushFlags.BossDead_MoonPresence)
    IfConditionTrue(0, 1)

    DisableFlag(BossRushFlags.RequestBoss_MoonPresence)  # Disabled here instead of in common warp event.
    EnableCharacter(Characters.MoonPresence)
    EnableBossHealthBar(Characters.MoonPresence, name=540000, slot=0)
    CreatePlayLog(128)
    StartPlayLogMeasurement(2100011, 146, overwrite=True)


def ControlMoonPresenceMusic():
    """ 12104853: Enable Moon Presence music, including second phase. """
    DisableSoundEvent(Music.MoonPresencePhase1Music)
    DisableSoundEvent(Music.MoonPresencePhase2Music)
    await Flags.MoonPresenceBattleStarted

    IfFlagOff(1, BossRushFlags.BossDead_MoonPresence)
    IfCharacterInsideRegion(1, PLAYER, region=2102801)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(Music.NormalMusic)
    DisableSoundEvent(Music.BloodMoonMusic)
    EnableBossMusic(Music.MoonPresencePhase1Music)

    IfHasTAEEvent(0, Characters.MoonPresence, tae_event_id=500)

    IfFlagOff(2, BossRushFlags.BossDead_MoonPresence)
    IfCharacterInsideRegion(2, PLAYER, region=2102801)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(Music.MoonPresencePhase1Music)
    WaitFrames(0)
    EnableBossMusic(Music.MoonPresencePhase2Music)


def ToggleMoonPresenceCamera():
    """ 12104854: Event 12104854 """
    DisableNetworkSync()
    EndIfFlagOn(Flags.MoonPresenceDead)
    IfHealthGreaterThan(1, Characters.MoonPresence, 0.0)
    IfEntityWithinDistance(1, PLAYER, Characters.MoonPresence, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=1)
    IfHealthGreaterThan(2, Characters.MoonPresence, 0.0)
    IfEntityBeyondDistance(2, PLAYER, Characters.MoonPresence, radius=12.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=HUNTERS_DREAM, camera_slot=0)
    Restart()


def StopMoonPresenceBossMusic():
    """ 12104855: Event 12104855 """
    await Flags.MoonPresenceBattleStarted
    await FlagEnabled(12104859)
    DisableBossMusic(Music.MoonPresencePhase1Music)
    DisableBossMusic(Music.MoonPresencePhase2Music)
    DisableBossMusic(-1)


def ControlMoonPresenceTail(
    _, part_id: short, monitor_part_id: int, part_index: short, part_health: int, limb_broken_speffect: int,
    limb_unbroken_speffect: int, wounded_animation: int,
):
    """ 12104860: Event 12104860 """
    EndIfFlagOn(Flags.MoonPresenceDead)

    CreateNPCPart(
        Characters.MoonPresence,
        npc_part_id=part_id,
        part_index=part_index,
        part_health=part_health,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(
        Characters.MoonPresence, npc_part_id=monitor_part_id, material_sfx_id=59, material_vfx_id=59
    )

    IfCharacterPartHealthLessThanOrEqual(2, Characters.MoonPresence, npc_part_id=monitor_part_id, value=0)
    IfHealthLessThanOrEqual(3, Characters.MoonPresence, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)

    EndIfFinishedConditionTrue(3)

    CreateNPCPart(
        Characters.MoonPresence,
        npc_part_id=part_id,
        part_index=part_index,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(
        Characters.MoonPresence, npc_part_id=monitor_part_id, material_sfx_id=60, material_vfx_id=60
    )
    ResetAnimation(Characters.MoonPresence, disable_interpolation=False)
    ForceAnimation(Characters.MoonPresence, wounded_animation)
    AddSpecialEffect(Characters.MoonPresence, limb_broken_speffect, affect_npc_part_hp=False)
    CancelSpecialEffect(Characters.MoonPresence, limb_unbroken_speffect)
    ReplanAI(Characters.MoonPresence)

    Wait(30.0)

    AICommand(Characters.MoonPresence, command_id=10, slot=1)
    ReplanAI(Characters.MoonPresence)
    IfHasTAEEvent(0, Characters.MoonPresence, tae_event_id=300)
    SetNPCPartHealth(Characters.MoonPresence, npc_part_id=monitor_part_id, desired_health=-1, overwrite_max=True)
    AddSpecialEffect(Characters.MoonPresence, limb_unbroken_speffect, affect_npc_part_hp=False)
    CancelSpecialEffect(Characters.MoonPresence, limb_broken_speffect)
    AICommand(Characters.MoonPresence, command_id=-1, slot=1)
    ReplanAI(Characters.MoonPresence)
    WaitFrames(10)
    return RESTART


def MoonPresenceSinHarvest():
    """ 12104870: Activate player immortality temporarily after "sin harvest" 1 HP attack by Moon Presence. """
    DisableNetworkSync()
    IfHasTAEEvent(0, Characters.MoonPresence, tae_event_id=10)
    EnableImmortality(PLAYER)
    IfCharacterHasSpecialEffect(-1, PLAYER, 5570)
    IfFramesElapsed(-1, 70)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(5)
    DisableImmortality(PLAYER)
    IfAttackedWithDamageType(-1, attacked_entity=PLAYER, attacker=Characters.MoonPresence)
    IfTimeElapsed(-1, 10.0)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(PLAYER, 5572)
    Restart()


@RestartOnRest
def AnimateHeadstoneMessengers(_, headstone_messengers: Character, headstone_active_flag: Flag):
    """ 12105000: Wake up messengers of a given headstone. """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, headstone_active_flag)
    ForceAnimation(headstone_messengers, 7000)
    WaitFrames(109)
    ForceAnimation(headstone_messengers, c9020.WaitingGrouped, loop=True)
    IfFlagOff(0, headstone_active_flag)
    ForceAnimation(headstone_messengers, 7002)
    WaitFrames(74)
    return RESTART


@RestartOnRest
def AnimateOldHuntersHeadstoneMessengers(_, headstone_messengers: Character, headstone_active_flag: Flag):
    """ 12105004: Variant of 12105000 that also moves and gives a special effect to the messengers.

    Note that the only instance of this is run with slot 3 for some reason.
    """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, headstone_active_flag)
    Move(headstone_messengers, destination=2102305, destination_type=CoordEntityType.Region, short_move=True)
    AddSpecialEffect(headstone_messengers, 5401, affect_npc_part_hp=False)
    ForceAnimation(headstone_messengers, 7000)
    WaitFrames(109)
    ForceAnimation(headstone_messengers, c9020.WaitingGrouped, loop=True)
    IfFlagOff(0, headstone_active_flag)
    ForceAnimation(headstone_messengers, 7002)
    WaitFrames(74)
    Restart()


@RestartOnRest
def InitializeMakeshiftAltar():
    """ 12105010: Event 12105010 """
    DisableObject(2101200)
    DisableObject(2101201)
    DisableObject(2101202)
    DisableObject(2101203)
    DisableObject(2101204)
    DisableObject(2101205)
    DisableObject(2101206)
    DisableObject(2101207)
    DisableObject(2101208)
    IfFlagOn(10, 94005500)
    IfFlagRangeAnyOn(10, (94005100, 94005101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagOn(11, 94005500)
    IfFlagRangeAnyOn(11, (94005103, 94005104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagOn(12, 94005500)
    IfFlagOn(12, 94005102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagOn(Label.L3, 94005503)
    GotoIfFlagOn(Label.L4, 94005504)
    GotoIfFlagOn(Label.L5, 94005505)
    GotoIfFlagOn(Label.L6, 94005502)
    GotoIfFlagOn(Label.L7, 94005507)
    GotoIfFlagOn(Label.L8, 94005501)
    IfFlagOn(1, 94005500)
    IfFlagRangeAnyOn(1, (94005100, 94005101))
    IfFlagOn(2, 94005500)
    IfFlagRangeAnyOn(2, (94005103, 94005104))
    IfFlagOn(3, 94005500)
    IfFlagOn(3, 94005102)
    IfFlagOn(4, 94005503)
    IfFlagOn(5, 94005504)
    IfFlagOn(6, 94005505)
    IfFlagOn(7, 94005502)
    IfFlagOn(8, 94005507)
    IfFlagOn(9, 94005501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(31)
    CreateTemporaryVFX(
        350, anchor_entity=Characters.MakeshiftAltar, anchor_type=CoordEntityType.Character, model_point=200)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101200)
    IfFlagOff(0, 94005500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101201)
    IfFlagOff(0, 94005500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101202)
    IfFlagOff(0, 94005500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101203)
    IfFlagOff(0, 94005503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101204)
    IfFlagOff(0, 94005504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101205)
    IfFlagOff(0, 94005505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101206)
    IfFlagOff(0, 94005502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101207)
    IfFlagOff(0, 94005507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101208)
    IfFlagOff(0, 94005501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(
        351, anchor_entity=Characters.MakeshiftAltar, anchor_type=CoordEntityType.Character, model_point=200)
    Restart()


@RestartOnRest
def InitializeChaliceAltar1():
    """ 12105011: Event 12105011 """
    DisableObject(2101210)
    DisableObject(2101211)
    DisableObject(2101212)
    DisableObject(2101213)
    DisableObject(2101214)
    DisableObject(2101215)
    DisableObject(2101216)
    DisableObject(2101217)
    DisableObject(2101218)
    IfFlagOn(10, 94105500)
    IfFlagRangeAnyOn(10, (94105100, 94105101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagOn(11, 94105500)
    IfFlagRangeAnyOn(11, (94105103, 94105104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagOn(12, 94105500)
    IfFlagOn(12, 94105102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagOn(Label.L3, 94105503)
    GotoIfFlagOn(Label.L4, 94105504)
    GotoIfFlagOn(Label.L5, 94105505)
    GotoIfFlagOn(Label.L6, 94105502)
    GotoIfFlagOn(Label.L7, 94105507)
    GotoIfFlagOn(Label.L8, 94105501)
    IfFlagOn(1, 94105500)
    IfFlagRangeAnyOn(1, (94105100, 94105101))
    IfFlagOn(2, 94105500)
    IfFlagRangeAnyOn(2, (94105103, 94105104))
    IfFlagOn(3, 94105500)
    IfFlagOn(3, 94105102)
    IfFlagOn(4, 94105503)
    IfFlagOn(5, 94105504)
    IfFlagOn(6, 94105505)
    IfFlagOn(7, 94105502)
    IfFlagOn(8, 94105507)
    IfFlagOn(9, 94105501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(31)
    CreateTemporaryVFX(
        350, anchor_entity=Characters.ChaliceAltar1, anchor_type=CoordEntityType.Character, model_point=200)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101210)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagOff(0, 94105500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101211)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagOff(0, 94105500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101212)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagOff(0, 94105500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101213)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagOff(0, 94105503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101214)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagOff(0, 94105504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101215)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagOff(0, 94105505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101216)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagOff(0, 94105502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101217)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagOff(0, 94105507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101218)
    WaitFrames(45)
    EnableFlag(70000221)
    IfFlagOff(0, 94105501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(
        351, anchor_entity=Characters.ChaliceAltar1, anchor_type=CoordEntityType.Character, model_point=200)
    Restart()


@RestartOnRest
def InitializeChaliceAltar2():
    """ 12105012: Event 12105012 """
    DisableObject(2101220)
    DisableObject(2101221)
    DisableObject(2101222)
    DisableObject(2101223)
    DisableObject(2101224)
    DisableObject(2101225)
    DisableObject(2101226)
    DisableObject(2101227)
    DisableObject(2101228)
    IfFlagOn(10, 94205500)
    IfFlagRangeAnyOn(10, (94205100, 94205101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagOn(11, 94205500)
    IfFlagRangeAnyOn(11, (94205103, 94205104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagOn(12, 94205500)
    IfFlagOn(12, 94205102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagOn(Label.L3, 94205503)
    GotoIfFlagOn(Label.L4, 94205504)
    GotoIfFlagOn(Label.L5, 94205505)
    GotoIfFlagOn(Label.L6, 94205502)
    GotoIfFlagOn(Label.L7, 94205507)
    GotoIfFlagOn(Label.L8, 94205501)
    IfFlagOn(1, 94205500)
    IfFlagRangeAnyOn(1, (94205100, 94205101))
    IfFlagOn(2, 94205500)
    IfFlagRangeAnyOn(2, (94205103, 94205104))
    IfFlagOn(3, 94205500)
    IfFlagOn(3, 94205102)
    IfFlagOn(4, 94205503)
    IfFlagOn(5, 94205504)
    IfFlagOn(6, 94205505)
    IfFlagOn(7, 94205502)
    IfFlagOn(8, 94205507)
    IfFlagOn(9, 94205501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(31)
    CreateTemporaryVFX(
        350, anchor_entity=Characters.ChaliceAltar2, anchor_type=CoordEntityType.Character, model_point=200)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101220)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagOff(0, 94205500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101221)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagOff(0, 94205500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101222)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagOff(0, 94205500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101223)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagOff(0, 94205503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101224)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagOff(0, 94205504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101225)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagOff(0, 94205505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101226)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagOff(0, 94205502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101227)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagOff(0, 94205507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101228)
    WaitFrames(45)
    EnableFlag(70000222)
    IfFlagOff(0, 94205501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(
        351, anchor_entity=Characters.ChaliceAltar2, anchor_type=CoordEntityType.Character, model_point=200)
    Restart()


@RestartOnRest
def InitializeChaliceAltar3():
    """ 12105013: Event 12105013 """
    DisableObject(2101230)
    DisableObject(2101231)
    DisableObject(2101232)
    DisableObject(2101233)
    DisableObject(2101234)
    DisableObject(2101235)
    DisableObject(2101236)
    DisableObject(2101237)
    DisableObject(2101238)
    IfFlagOn(10, 94305500)
    IfFlagRangeAnyOn(10, (94305100, 94305101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagOn(11, 94305500)
    IfFlagRangeAnyOn(11, (94305103, 94305104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagOn(12, 94305500)
    IfFlagOn(12, 94305102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagOn(Label.L3, 94305503)
    GotoIfFlagOn(Label.L4, 94305504)
    GotoIfFlagOn(Label.L5, 94305505)
    GotoIfFlagOn(Label.L6, 94305502)
    GotoIfFlagOn(Label.L7, 94305507)
    GotoIfFlagOn(Label.L8, 94305501)
    IfFlagOn(1, 94305500)
    IfFlagRangeAnyOn(1, (94305100, 94305101))
    IfFlagOn(2, 94305500)
    IfFlagRangeAnyOn(2, (94305103, 94305104))
    IfFlagOn(3, 94305500)
    IfFlagOn(3, 94305102)
    IfFlagOn(4, 94305503)
    IfFlagOn(5, 94305504)
    IfFlagOn(6, 94305505)
    IfFlagOn(7, 94305502)
    IfFlagOn(8, 94305507)
    IfFlagOn(9, 94305501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(31)
    CreateTemporaryVFX(
        350, anchor_entity=Characters.ChaliceAltar3, anchor_type=CoordEntityType.Character, model_point=200)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101230)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagOff(0, 94305500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101231)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagOff(0, 94305500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101232)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagOff(0, 94305500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101233)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagOff(0, 94305503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101234)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagOff(0, 94305504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101235)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagOff(0, 94305505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101236)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagOff(0, 94305502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101237)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagOff(0, 94305507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101238)
    WaitFrames(45)
    EnableFlag(70000223)
    IfFlagOff(0, 94305501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(
        351, anchor_entity=Characters.ChaliceAltar3, anchor_type=CoordEntityType.Character, model_point=200)
    Restart()


@RestartOnRest
def InitializeChaliceAltar4():
    """ 12105014: Event 12105014 """
    DisableObject(2101240)
    DisableObject(2101241)
    DisableObject(2101242)
    DisableObject(2101243)
    DisableObject(2101244)
    DisableObject(2101245)
    DisableObject(2101246)
    DisableObject(2101247)
    DisableObject(2101248)
    IfFlagOn(10, 94405500)
    IfFlagRangeAnyOn(10, (94405100, 94405101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagOn(11, 94405500)
    IfFlagRangeAnyOn(11, (94405103, 94405104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagOn(12, 94405500)
    IfFlagOn(12, 94405102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagOn(Label.L3, 94405503)
    GotoIfFlagOn(Label.L4, 94405504)
    GotoIfFlagOn(Label.L5, 94405505)
    GotoIfFlagOn(Label.L6, 94405502)
    GotoIfFlagOn(Label.L7, 94405507)
    GotoIfFlagOn(Label.L8, 94405501)
    IfFlagOn(1, 94405500)
    IfFlagRangeAnyOn(1, (94405100, 94405101))
    IfFlagOn(2, 94405500)
    IfFlagRangeAnyOn(2, (94405103, 94405104))
    IfFlagOn(3, 94405500)
    IfFlagOn(3, 94405102)
    IfFlagOn(4, 94405503)
    IfFlagOn(5, 94405504)
    IfFlagOn(6, 94405505)
    IfFlagOn(7, 94405502)
    IfFlagOn(8, 94405507)
    IfFlagOn(9, 94405501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(31)
    CreateTemporaryVFX(
        350, anchor_entity=Characters.ChaliceAltar4, anchor_type=CoordEntityType.Character, model_point=200)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101240)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagOff(0, 94405500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101241)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagOff(0, 94405500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101242)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagOff(0, 94405500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101243)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagOff(0, 94405503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101244)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagOff(0, 94405504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101245)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagOff(0, 94405505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101246)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagOff(0, 94405502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101247)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagOff(0, 94405507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101248)
    WaitFrames(45)
    EnableFlag(70000224)
    IfFlagOff(0, 94405501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(
        351, anchor_entity=Characters.ChaliceAltar4, anchor_type=CoordEntityType.Character, model_point=200)
    Restart()


@RestartOnRest
def InitializeChaliceAltar5():
    """ 12105015: Event 12105015 """
    DisableObject(2101250)
    DisableObject(2101251)
    DisableObject(2101252)
    DisableObject(2101253)
    DisableObject(2101254)
    DisableObject(2101255)
    DisableObject(2101256)
    DisableObject(2101257)
    DisableObject(2101258)
    IfFlagOn(10, 94505500)
    IfFlagRangeAnyOn(10, (94505100, 94505101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagOn(11, 94505500)
    IfFlagRangeAnyOn(11, (94505103, 94505104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagOn(12, 94505500)
    IfFlagOn(12, 94505102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagOn(Label.L3, 94505503)
    GotoIfFlagOn(Label.L4, 94505504)
    GotoIfFlagOn(Label.L5, 94505505)
    GotoIfFlagOn(Label.L6, 94505502)
    GotoIfFlagOn(Label.L7, 94505507)
    GotoIfFlagOn(Label.L8, 94505501)
    IfFlagOn(1, 94505500)
    IfFlagRangeAnyOn(1, (94505100, 94505101))
    IfFlagOn(2, 94505500)
    IfFlagRangeAnyOn(2, (94505103, 94505104))
    IfFlagOn(3, 94505500)
    IfFlagOn(3, 94505102)
    IfFlagOn(4, 94505503)
    IfFlagOn(5, 94505504)
    IfFlagOn(6, 94505505)
    IfFlagOn(7, 94505502)
    IfFlagOn(8, 94505507)
    IfFlagOn(9, 94505501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(31)
    CreateTemporaryVFX(
        350, anchor_entity=Characters.ChaliceAltar5, anchor_type=CoordEntityType.Character, model_point=200)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101250)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagOff(0, 94505500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101251)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagOff(0, 94505500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101252)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagOff(0, 94505500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101253)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagOff(0, 94505503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101254)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagOff(0, 94505504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101255)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagOff(0, 94505505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101256)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagOff(0, 94505502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101257)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagOff(0, 94505507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101258)
    WaitFrames(45)
    EnableFlag(70000225)
    IfFlagOff(0, 94505501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(
        351, anchor_entity=Characters.ChaliceAltar5, anchor_type=CoordEntityType.Character, model_point=200)
    Restart()


@RestartOnRest
def InitializeChaliceAltar6():
    """ 12105016: Event 12105016 """
    DisableObject(2101260)
    DisableObject(2101261)
    DisableObject(2101262)
    DisableObject(2101263)
    DisableObject(2101264)
    DisableObject(2101265)
    DisableObject(2101266)
    DisableObject(2101267)
    DisableObject(2101268)
    IfFlagOn(10, 94605500)
    IfFlagRangeAnyOn(10, (94605100, 94605101))
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfFlagOn(11, 94605500)
    IfFlagRangeAnyOn(11, (94605103, 94605104))
    GotoIfConditionTrue(Label.L1, input_condition=11)
    IfFlagOn(12, 94605500)
    IfFlagOn(12, 94605102)
    GotoIfConditionTrue(Label.L2, input_condition=12)
    GotoIfFlagOn(Label.L3, 94605503)
    GotoIfFlagOn(Label.L4, 94605504)
    GotoIfFlagOn(Label.L5, 94605505)
    GotoIfFlagOn(Label.L6, 94605502)
    GotoIfFlagOn(Label.L7, 94605507)
    GotoIfFlagOn(Label.L8, 94605501)
    IfFlagOn(1, 94605500)
    IfFlagRangeAnyOn(1, (94605100, 94605101))
    IfFlagOn(2, 94605500)
    IfFlagRangeAnyOn(2, (94605103, 94605104))
    IfFlagOn(3, 94605500)
    IfFlagOn(3, 94605102)
    IfFlagOn(4, 94605503)
    IfFlagOn(5, 94605504)
    IfFlagOn(6, 94605505)
    IfFlagOn(7, 94605502)
    IfFlagOn(8, 94605507)
    IfFlagOn(9, 94605501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(31)
    CreateTemporaryVFX(
        350, anchor_entity=Characters.ChaliceAltar6, anchor_type=CoordEntityType.Character, model_point=200)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L4, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=6)
    GotoIfFinishedConditionTrue(Label.L6, input_condition=7)
    GotoIfFinishedConditionTrue(Label.L7, input_condition=8)
    GotoIfFinishedConditionTrue(Label.L8, input_condition=9)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2101260)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagOff(0, 94605500)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2101261)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagOff(0, 94605500)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2101262)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagOff(0, 94605500)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2101263)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagOff(0, 94605503)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2101264)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagOff(0, 94605504)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2101265)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagOff(0, 94605505)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2101266)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagOff(0, 94605502)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableObject(2101267)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagOff(0, 94605507)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    EnableObject(2101268)
    WaitFrames(45)
    EnableFlag(70000226)
    IfFlagOff(0, 94605501)

    # --- 9 --- #
    DefineLabel(9)
    CreateTemporaryVFX(
        351, anchor_entity=Characters.ChaliceAltar6, anchor_type=CoordEntityType.Character, model_point=200)
    Restart()


@RestartOnRest
def InitializeBathMessengers():
    """ 12105040: Event 12105040 """
    ForceAnimation(Characters.BathShopMessengers1, c9020.WaitingGrouped, loop=True)
    ForceAnimation(Characters.BathShopMessengers2, 7002, loop=True)
    ForceAnimation(Characters.BathShopMessengers3, 7041, loop=True)
    IfFlagOn(0, 12105041)
    ForceAnimation(Characters.BathShopMessengers1, 7005)
    ForceAnimation(Characters.BathShopMessengers2, 7006)
    ForceAnimation(Characters.BathShopMessengers3, 7045)
    WaitFrames(29)
    ForceAnimation(Characters.BathShopMessengers1, c9020.Disappear, loop=True)
    ForceAnimation(Characters.BathShopMessengers2, c9020.Appear, loop=True)
    ForceAnimation(Characters.BathShopMessengers3, 7043, loop=True)
    IfFlagOff(0, 12105041)
    ForceAnimation(Characters.BathShopMessengers1, 7007)
    ForceAnimation(Characters.BathShopMessengers2, 7008)
    ForceAnimation(Characters.BathShopMessengers3, 7047)
    WaitFrames(28)
    Restart()


def InitializeStoryProgressionFlags():
    """ 12101010: Enables flags in 5900-5904 range depending on story progression. """
    DisableNetworkSync()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    SkipLinesIfFlagOff(1, 9800)
    EnableFlag(5900)
    SkipLinesIfFlagOff(1, 9801)
    EnableFlag(5901)
    SkipLinesIfFlagOff(1, CommonFlags.BloodMoonPhase)
    EnableFlag(5902)
    SkipLinesIfFlagOff(1, CommonFlags.OneRebornDead)
    EnableFlag(5903)
    SkipLinesIfFlagOff(1, CommonFlags.WetNurseDead)
    EnableFlag(5904)
    SkipLinesIfFlagOff(1, 6603)
    EnableFlagRange((5900, 5904))


@RestartOnRest
def InitializeInsightShop():
    """ 12105043: Second Insight shop messenger wakes up when player has 1 insight. """
    # TODO: Sell armor sets at this shop.
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)

    # Always available.
    EnableFlag(12105045)
    ForceAnimation(Characters.InsightShopMessengers2, 7032, loop=True)
    IfFlagOn(0, 12105044)
    ForceAnimation(Characters.InsightShopMessengers2, 7034)
    WaitFrames(29)
    ForceAnimation(Characters.InsightShopMessengers2, 7035, loop=True)
    IfFlagOff(0, 12105044)
    ForceAnimation(Characters.InsightShopMessengers2, 7036)
    WaitFrames(28)
    return RESTART


def OfferMeleeWeaponGift():
    """ 12101020: Disabled. """
    DisableBackread(Characters.MeleeWeaponGiftMessengers)
    DisableBackread(Characters.MeleeWeaponGift)


def OfferGunGift():
    """ 12101021: Disabled. """
    DisableBackread(Characters.GunGiftMessengers)
    DisableBackread(Characters.GunGift)


def OfferNotebookGift():
    """ 12101022: Disabled. """
    ForceAnimation(Characters.BellGiftMessengers, c9020.OfferingHidden, loop=True)


def OfferBeckoningBellGift():
    """ 12101024: Disabled. """
    ForceAnimation(Characters.OldHuntersMessengers, c9020.OfferingHidden, loop=True)


def OfferOldHunterBellGift():
    """ 12101026: Disabled. """
    ForceAnimation(Characters.BellGiftMessengers, c9020.OfferingHidden, loop=True)


def OfferDLCAccessGift():
    """ 12101028: Disabled. """
    ForceAnimation(Characters.OldHuntersMessengers, c9020.OfferingHidden, loop=True)


def Event12101100():
    """ 12101100: Event 12101100 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(1, 6899)
    IfFlagOn(1, 9801)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12101101)


def Event12105200():
    """ 12105200: Enables this flag 1 frame after Plain Doll has effect 153. """
    DisableFlag(12105200)
    IfCharacterHasSpecialEffect(0, Characters.PlainDoll, 153)
    WaitFrames(1)


def MonitorWeaponBuffRemovalRequest():
    """ 12105210: Event 12105210 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, CommonFlags.RequestWeaponBuffRemoval)
    DisableFlag(CommonFlags.RequestWeaponBuffRemoval)
    CancelSpecialEffect(PLAYER, Effects.FirePaper)
    CancelSpecialEffect(PLAYER, Effects.EmptyPhantasmShell)
    CancelSpecialEffect(PLAYER, Effects.BoltPaper)
    Restart()


def Event12105300():
    """ 12105300: Event 12105300 """
    DisableNetworkSync()
    EndIfClient()
    SkipLinesIfFlagOff(1, 5020)
    EnableFlag(6228)
    SkipLinesIfFlagOff(1, 5021)
    EnableFlag(6235)
    IfFlagOn(-1, 5023)
    IfFlagOn(-1, 70009200)
    SkipLinesIfConditionFalse(1, -1)
    EnableFlag(6242)
    SkipLinesIfFlagOff(1, 5027)
    EnableFlag(6249)
    IfFlagOn(-2, 5029)
    IfFlagOn(-2, 70009220)
    SkipLinesIfConditionFalse(1, -2)
    EnableFlag(6256)
    SkipLinesIfFlagOff(1, 5022)
    EnableFlag(6236)
    IfFlagOn(-3, 5025)
    IfFlagOn(-3, 70009210)
    SkipLinesIfConditionFalse(1, -3)
    EnableFlag(6243)
    SkipLinesIfFlagOff(1, 5028)
    EnableFlag(6251)
    IfFlagOn(-4, 5031)
    IfFlagOn(-4, 70009230)
    SkipLinesIfConditionFalse(1, -4)
    EnableFlag(6258)
    IfFlagOn(-5, 5033)
    IfFlagOn(-5, 70009240)
    SkipLinesIfConditionFalse(1, -5)
    EnableFlag(6259)


def WarpAtHeadstone(_, choice_flag: int, headstone: int, warp_point: int):
    """ 12107000: Activate a headstone warp out into Yharnam, the Nightmare, etc. """
    EndIfClient()
    IfFlagOn(0, choice_flag)
    RotateToFaceEntity(PLAYER, headstone, animation=PlayerAnimations.WarpAtHeadstone, wait_for_completion=False)
    Wait(4.0)
    WarpPlayerToRespawnPoint(warp_point)


def BossRushFirstArrival():
    """ 9401: Gives player equipment and blood echoes, and sets up flags. """
    DisableNetworkSync()
    EndIfClient()
    EndIfThisEventOn()

    # Set respawn point to Hunter's Dream. (This is the one and only respawn point in the mod.)
    SetRespawnPoint(2102961)

    # Enable warp flags for boss lanterns only.
    EnableFlag(HeadstoneWarpUnlockedFlags.WitchesOfHemwick)
    EnableFlag(HeadstoneWarpUnlockedFlags.BloodStarvedBeast)
    EnableFlag(HeadstoneWarpUnlockedFlags.DarkbeastPaarl)
    EnableFlag(HeadstoneWarpUnlockedFlags.VicarAmelia)
    EnableFlag(HeadstoneWarpUnlockedFlags.ClericBeast)
    EnableFlag(HeadstoneWarpUnlockedFlags.FatherGascoigne)
    EnableFlag(HeadstoneWarpUnlockedFlags.Ebrietas)
    EnableFlag(HeadstoneWarpUnlockedFlags.CelestialEmissary)
    EnableFlag(HeadstoneWarpUnlockedFlags.MartyrLogarius)
    EnableFlag(HeadstoneWarpUnlockedFlags.Micolash)
    EnableFlag(HeadstoneWarpUnlockedFlags.MergosWetNurse)
    EnableFlag(HeadstoneWarpUnlockedFlags.ShadowsOfYharnam)
    EnableFlag(HeadstoneWarpUnlockedFlags.TheOneReborn)
    EnableFlag(HeadstoneWarpUnlockedFlags.Rom)
    EnableFlag(HeadstoneWarpUnlockedFlags.Amygdala)
    EnableFlag(HeadstoneWarpUnlockedFlags.Ludwig)
    EnableFlag(HeadstoneWarpUnlockedFlags.Laurence)
    EnableFlag(HeadstoneWarpUnlockedFlags.LivingFailures)
    EnableFlag(HeadstoneWarpUnlockedFlags.LadyMaria)
    EnableFlag(HeadstoneWarpUnlockedFlags.OrphanOfKos)

    # TODO: All starting classes are Waste of Skin (all same stats, except they start with 687334 echoes).
    #  Can rename the class to something else, actually.

    # TODO: Give player all weapons and equipment (just look up available item lots, probably).
