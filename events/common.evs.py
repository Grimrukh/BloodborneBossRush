"""
linked:


strings:

"""
from soulstruct.bloodborne.events import *
from .common_entities import *
from .boss_rush_entities import *


def Constructor():
    """ 0: Event 0 """

    if (BossRushTriggers.GehrmanOrMoonPresence or OutsideMap(HUNTERS_DREAM)) and not BossRushFlags.BossRushActive:
        # Get exactly 20 Vials and Bullets on map load if this is a single boss fight.
        RemoveGoodFromPlayer(BossRushGoods.BloodVial, 99)
        RemoveGoodFromPlayer(BossRushGoods.QuicksilverBullet, 99)
        RemoveGoodFromPlayer(BossRushGoods.BloodBullet, 99)
        AwardItemLot(BossRushItemLots.VialRefill20)
        AwardItemLot(BossRushItemLots.BulletRefill20)
        # Leave spawn point as whatever was warped to, for single boss fight.
    else:
        # Set respawn point to normal Hunter's Dream spawn.
        SetRespawnPoint(BossRushWarpPoints.HuntersDream)  # Hunter's Dream

    ManageGems()
    ManageNormalRunes()
    ManageCovenantRunes()
    MonitorGemPurchase()
    MonitorNormalRunePurchase()
    MonitorCovenantRunePurchase()

    DisableFlag(7501)
    RunEvent(9190)
    RunEvent(9191)
    RunEvent(9192)
    RunEvent(9193)
    RunEvent(9198)
    RunEvent(6788)
    RunEvent(6789)
    RunEvent(6809)
    RunEvent(6815)
    RunEvent(6816)
    RunEvent(9181)
    RunEvent(9182)
    RunEvent(9183)
    RunEvent(9186)

    # Events 6680 to 6697 monitored possession of various weapons (any upgrade level). I've hijacked them.

    # 5500-5521 hijacked (5500, slots 0 to 21).

    RunEvent(9500, slot=0, args=(3400, 100000))
    RunEvent(9500, slot=1, args=(3401, 100010))
    RunEvent(9500, slot=2, args=(3402, 100020))
    RunEvent(9500, slot=3, args=(3403, 100030))
    RunEvent(9500, slot=4, args=(3404, 100040))
    RunEvent(9500, slot=5, args=(3405, 100050))
    RunEvent(9500, slot=6, args=(3406, 100060))
    RunEvent(9500, slot=7, args=(3407, 100070))
    RunEvent(9500, slot=8, args=(3408, 100080))
    RunEvent(9500, slot=9, args=(3409, 100090))
    RunEvent(9500, slot=10, args=(3410, 100100))
    RunEvent(9500, slot=11, args=(3411, 100110))
    RunEvent(9500, slot=12, args=(3412, 100120))
    RunEvent(9500, slot=13, args=(3390, 100500))
    RunEvent(9500, slot=14, args=(3391, 100510))
    RunEvent(9500, slot=15, args=(3392, 100520))
    RunEvent(9500, slot=16, args=(3450, 101000))
    RunEvent(9500, slot=17, args=(3451, 101010))
    RunEvent(9500, slot=18, args=(3452, 101020))
    RunEvent(9500, slot=19, args=(3453, 101030))
    RunEvent(9500, slot=20, args=(3454, 101040))
    RunEvent(9500, slot=21, args=(3455, 101050))
    RunEvent(9500, slot=22, args=(3456, 101060))
    RunEvent(9500, slot=23, args=(3457, 101070))
    RunEvent(9500, slot=24, args=(3458, 101080))
    RunEvent(9500, slot=25, args=(3459, 101090))
    RunEvent(9500, slot=26, args=(3460, 101100))
    RunEvent(9500, slot=27, args=(3461, 101110))
    RunEvent(9500, slot=28, args=(3462, 101120))
    RunEvent(9500, slot=29, args=(3463, 101130))
    RunEvent(9500, slot=30, args=(3464, 101140))
    RunEvent(9500, slot=31, args=(3465, 101150))
    RunEvent(9500, slot=32, args=(3466, 101160))
    RunEvent(9500, slot=33, args=(3467, 101170))
    RunEvent(9500, slot=34, args=(3468, 101180))
    RunEvent(9500, slot=35, args=(3469, 101190))
    RunEvent(9500, slot=36, args=(3470, 101200))
    RunEvent(9500, slot=37, args=(3471, 101210))
    RunEvent(9500, slot=38, args=(3472, 101220))
    RunEvent(9500, slot=39, args=(3473, 101230))
    RunEvent(9500, slot=40, args=(3474, 101240))
    RunEvent(9500, slot=41, args=(3475, 101250))
    RunEvent(9500, slot=42, args=(3476, 101260))
    RunEvent(9500, slot=43, args=(3477, 101270))
    RunEvent(9500, slot=44, args=(3478, 101280))
    RunEvent(9500, slot=45, args=(3479, 101290))
    RunEvent(9500, slot=46, args=(3480, 101300))
    RunEvent(9500, slot=47, args=(3481, 101310))
    RunEvent(9500, slot=48, args=(3482, 101320))
    RunEvent(9500, slot=49, args=(3483, 101330))
    RunEvent(9500, slot=50, args=(3484, 101340))
    RunEvent(9440, slot=0, args=(9440, 10500))
    RunEvent(9440, slot=1, args=(9441, 11500))
    RunEvent(9440, slot=2, args=(9442, 12500))

    # 9421 hijacked.
    # 9422 hijacked.
    # 9400 hijacked.
    # 9404 hijacked.

    RunEvent(9040, slot=2, args=(9042, 17000))
    RunEvent(9040, slot=5, args=(9045, 22000))
    RunEvent(9040, slot=6, args=(9046, 23000))
    RunEvent(9040, slot=7, args=(9047, 24000))
    RunEvent(9040, slot=8, args=(9048, 24010))
    RunEvent(9040, slot=9, args=(9049, 24020))
    RunEvent(9040, slot=10, args=(9050, 24030))
    RunEvent(9040, slot=11, args=(9051, 24040))
    RunEvent(9040, slot=12, args=(9052, 24050))
    RunEvent(9040, slot=14, args=(9054, 26000))
    RunEvent(9040, slot=15, args=(9055, 26010))
    RunEvent(9040, slot=16, args=(9056, 26020))
    RunEvent(9040, slot=17, args=(9057, 26030))
    RunEvent(9040, slot=18, args=(9058, 27000))
    RunEvent(9040, slot=19, args=(9059, 27010))
    RunEvent(9040, slot=20, args=(9060, 27020))
    RunEvent(9040, slot=21, args=(9061, 27030))
    RunEvent(9040, slot=22, args=(9062, 27040))
    RunEvent(9040, slot=23, args=(9063, 27050))
    RunEvent(9040, slot=24, args=(9064, 27060))
    RunEvent(9040, slot=26, args=(9066, 29000))
    RunEvent(9040, slot=27, args=(9067, 30000))
    RunEvent(9040, slot=29, args=(9069, 32000))
    RunEvent(9040, slot=31, args=(9071, 33000))
    RunEvent(9040, slot=32, args=(9072, 34000))
    RunEvent(9040, slot=33, args=(9073, 34010))
    RunEvent(9040, slot=34, args=(9074, 35000))
    RunEvent(9040, slot=35, args=(9075, 35010))
    RunEvent(9040, slot=36, args=(9076, 39000))
    RunEvent(9040, slot=37, args=(9077, 39010))
    RunEvent(9100, slot=0, args=(72410359, 24060))
    RunEvent(9100, slot=1, args=(72410310, 23000))
    RunEvent(9100, slot=2, args=(72400398, 32020))
    RunEvent(9100, slot=3, args=(72400489, 28000))
    RunEvent(9100, slot=4, args=(9043, 17010))
    RunEvent(9910)
    RunEvent(9909)
    RunEvent(9905, slot=0, args=(4685,))
    RunEvent(9905, slot=1, args=(4686,))
    RunEvent(9905, slot=2, args=(4687,))
    RunEvent(9905, slot=3, args=(4688,))
    SkipLinesIfHost(1)
    AddSpecialEffect(PLAYER, 9110, affect_npc_part_hp=False)
    RunEvent(9030, slot=0, args=(6100, 180010))
    RunEvent(9030, slot=1, args=(6110, 180000))
    RunEvent(9030, slot=2, args=(6120, 180020))
    RunEvent(9035, slot=0, args=(6142, 180040))
    IfPlayerHasGood(1, 6302, including_box=False)
    SkipLinesIfConditionFalse(1, 1)
    EnableFlag(70009200)
    IfPlayerHasGood(2, 6312, including_box=False)
    SkipLinesIfConditionFalse(1, 2)
    EnableFlag(70009210)
    IfPlayerHasGood(3, 6502, including_box=False)
    SkipLinesIfConditionFalse(1, 3)
    EnableFlag(70009220)
    IfPlayerHasGood(4, 6522, including_box=False)
    SkipLinesIfConditionFalse(1, 4)
    EnableFlag(70009230)
    IfPlayerHasGood(5, 6532, including_box=False)
    SkipLinesIfConditionFalse(1, 5)
    EnableFlag(70009240)

    # NEW BOSS RUSH EVENTS

    # These events warp you to the given warp point whenever the given request flag is enabled.
    WarpToBoss(0, BossRushFlags.RequestBoss_ClericBeast, BossRushWarpPoints.ClericBeast)
    WarpToBoss(1, BossRushFlags.RequestBoss_FatherGascoigne, BossRushWarpPoints.FatherGascoigne)
    WarpToBoss(2, BossRushFlags.RequestBoss_BloodStarvedBeast, BossRushWarpPoints.BloodStarvedBeast)
    WarpToBoss(3, BossRushFlags.RequestBoss_WitchesOfHemwick, BossRushWarpPoints.WitchesOfHemwick)
    WarpToBoss(4, BossRushFlags.RequestBoss_VicarAmelia, BossRushWarpPoints.VicarAmelia)
    WarpToBoss(5, BossRushFlags.RequestBoss_DarkbeastPaarl, BossRushWarpPoints.DarkbeastPaarl)
    WarpToBoss(6, BossRushFlags.RequestBoss_ShadowsOfYharnam, BossRushWarpPoints.ShadowsOfYharnam)
    WarpToBoss(7, BossRushFlags.RequestBoss_Rom, BossRushWarpPoints.Rom)
    WarpToBoss(8, BossRushFlags.RequestBoss_Amygdala, BossRushWarpPoints.Amygdala)
    WarpToBoss(9, BossRushFlags.RequestBoss_MartyrLogarius, BossRushWarpPoints.MartyrLogarius)
    WarpToBoss(10, BossRushFlags.RequestBoss_TheOneReborn, BossRushWarpPoints.TheOneReborn)
    WarpToBoss(11, BossRushFlags.RequestBoss_CelestialEmissary, BossRushWarpPoints.CelestialEmissary)
    WarpToBoss(12, BossRushFlags.RequestBoss_Ebrietas, BossRushWarpPoints.Ebrietas)
    WarpToBoss(13, BossRushFlags.RequestBoss_Micolash, BossRushWarpPoints.Micolash)
    WarpToBoss(14, BossRushFlags.RequestBoss_MergosWetNurse, BossRushWarpPoints.MergosWetNurse)
    WarpToBoss(15, BossRushFlags.RequestBoss_Ludwig, BossRushWarpPoints.Ludwig)
    WarpToBoss(16, BossRushFlags.RequestBoss_LivingFailures, BossRushWarpPoints.LivingFailures)
    WarpToBoss(17, BossRushFlags.RequestBoss_LadyMaria, BossRushWarpPoints.LadyMaria)
    WarpToBoss(18, BossRushFlags.RequestBoss_Laurence, BossRushWarpPoints.Laurence)
    WarpToBoss(19, BossRushFlags.RequestBoss_OrphanOfKos, BossRushWarpPoints.OrphanOfKos)
    WarpToBoss(20, BossRushFlags.RequestBoss_Gehrman, BossRushWarpPoints.GehrmanOrMoonPresence)
    WarpToBoss(21, BossRushFlags.RequestBoss_MoonPresence, BossRushWarpPoints.GehrmanOrMoonPresence)

    MonitorStoryBossRushRequest()
    MonitorRandomBossRushRequest()
    FinishBossRush()
    WarpBackToDream()


def Preconstructor():
    """ 50: Event 50 """
    RunEvent(6002)
    GotoIfClient(Label.L2)
    SkipLinesIfFlagOff(2, 12101800)
    EnableFlag(9450)
    DisableFlag(3210)
    SkipLinesIfFlagOff(2, 12101850)
    EnableFlag(9451)
    DisableFlag(3211)
    SkipLinesIfFlagOff(3, 12201800)
    EnableFlag(9452)
    EnableFlag(5911)
    DisableFlag(3220)
    SkipLinesIfFlagOff(2, 12301800)
    EnableFlag(9453)
    DisableFlag(3230)
    SkipLinesIfFlagOff(2, 12301700)
    EnableFlag(9454)
    DisableFlag(3231)
    SkipLinesIfFlagOff(2, 12401800)
    EnableFlag(9455)
    DisableFlag(3240)
    SkipLinesIfFlagOff(2, 12411700)
    EnableFlag(9456)
    DisableFlag(3241)
    SkipLinesIfFlagOff(3, 12411800)
    EnableFlag(9457)
    EnableFlag(5910)
    DisableFlag(3242)
    SkipLinesIfFlagOff(2, 12421700)
    EnableFlag(9458)
    DisableFlag(3243)
    SkipLinesIfFlagOff(2, 12421800)
    EnableFlag(9459)
    DisableFlag(3244)
    SkipLinesIfFlagOff(2, 12501800)
    EnableFlag(9460)
    DisableFlag(3250)
    SkipLinesIfFlagOff(4, 12601850)
    EnableFlag(9461)
    DisableFlag(3260)
    SkipLinesIfFlagOff(1, 12607850)
    EnableFlag(12601854)
    SkipLinesIfFlagOff(2, 12601800)
    EnableFlag(9462)
    DisableFlag(3261)
    SkipLinesIfFlagOff(2, 12701800)
    EnableFlag(9463)
    DisableFlag(3270)
    SkipLinesIfFlagOff(2, 12801800)
    EnableFlag(9464)
    DisableFlag(3280)
    SkipLinesIfFlagOff(2, 13201800)
    EnableFlag(9465)
    DisableFlag(3320)
    SkipLinesIfFlagOff(2, 13301800)
    EnableFlag(9466)
    DisableFlag(3330)
    SkipLinesIfFlagOff(1, 12410810)
    EnableFlag(5912)
    SkipLinesIfFlagOff(1, 12300704)
    EnableFlag(5914)
    SkipLinesIfFlagOff(1, 12600029)
    EnableFlag(5913)
    SkipLinesIfFlagOff(1, 12700710)
    EnableFlag(9467)
    SkipLinesIfFlagOff(1, 12410322)
    EnableFlag(12410330)

    # --- 2 --- #
    DefineLabel(2)
    DisableFlag(CommonFlags.CutsceneActive)
    # Old 9360 calls (Blood Dreg rewards) removed.
    RunEvent(9480, slot=0, args=(1710, 1711, 1712, 1713, 73600521))
    RunEvent(9480, slot=1, args=(1730, 1730, 1730, 1730, 6001))
    RunEvent(9480, slot=2, args=(1790, 1790, 1790, 1790, 6001))
    RunEvent(9480, slot=3, args=(13501900, 13501900, 13501900, 13501900, 6001))
    RunEvent(9480, slot=4, args=(12700909, 12700909, 12700909, 12700909, 6001))
    RunEvent(9480, slot=5, args=(13400970, 13400970, 13400970, 13400970, 6001))
    RunEvent(9480, slot=6, args=(13400971, 13400971, 13400971, 13400971, 6001))
    RunEvent(9480, slot=7, args=(13501901, 13501901, 13501901, 13501901, 6001))
    RunEvent(9480, slot=8, args=(13501902, 13501902, 13501902, 13501902, 6001))
    RunEvent(9480, slot=9, args=(13501903, 13501903, 13501903, 13501903, 6001))
    RunEvent(9480, slot=10, args=(13501904, 13501904, 13501904, 13501904, 6001))
    GotoIfFlagOn(Label.L0, 999)
    SkipLinesIfFlagRangeAnyOn(1, (1000, 1019))
    EnableFlag(1000)
    SkipLinesIfFlagRangeAnyOn(1, (1020, 1039))
    EnableFlag(1020)
    SkipLinesIfFlagRangeAnyOn(1, (1040, 1059))
    EnableFlag(1040)
    SkipLinesIfFlagRangeAnyOn(1, (1060, 1079))
    EnableFlag(1060)
    SkipLinesIfFlagRangeAnyOn(1, (1080, 1099))
    EnableFlag(1080)
    SkipLinesIfFlagRangeAnyOn(1, (1100, 1119))
    EnableFlag(1100)
    SkipLinesIfFlagRangeAnyOn(1, (1120, 1139))
    EnableFlag(1120)
    SkipLinesIfFlagRangeAnyOn(1, (1140, 1159))
    EnableFlag(1140)
    SkipLinesIfFlagRangeAnyOn(1, (1160, 1179))
    EnableFlag(1160)
    SkipLinesIfFlagRangeAnyOn(1, (1180, 1199))
    EnableFlag(1180)
    SkipLinesIfFlagRangeAnyOn(1, (1200, 1219))
    EnableFlag(1200)
    SkipLinesIfFlagRangeAnyOn(1, (1220, 1239))
    EnableFlag(1220)
    SkipLinesIfFlagRangeAnyOn(1, (1240, 1259))
    EnableFlag(1240)
    SkipLinesIfFlagRangeAnyOn(1, (1260, 1279))
    EnableFlag(1260)
    SkipLinesIfFlagRangeAnyOn(1, (1280, 1289))
    EnableFlag(1280)
    SkipLinesIfFlagRangeAnyOn(1, (1290, 1299))
    EnableFlag(1290)
    SkipLinesIfFlagRangeAnyOn(1, (1300, 1319))
    EnableFlag(1300)
    SkipLinesIfFlagRangeAnyOn(1, (1320, 1339))
    EnableFlag(1320)
    SkipLinesIfFlagRangeAnyOn(1, (1340, 1359))
    EnableFlag(1340)
    SkipLinesIfFlagRangeAnyOn(1, (1360, 1379))
    EnableFlag(1360)
    SkipLinesIfFlagRangeAnyOn(1, (1380, 1399))
    EnableFlag(1380)
    SkipLinesIfFlagRangeAnyOn(1, (1400, 1419))
    EnableFlag(1400)
    SkipLinesIfFlagRangeAnyOn(1, (1420, 1439))
    EnableFlag(1420)
    SkipLinesIfFlagRangeAnyOn(1, (1440, 1459))
    EnableFlag(1440)
    EnableFlag(999)

    # --- 0 --- #
    DefineLabel(0)
    RunEvent(9700, slot=0, args=(1020, 1039))
    RunEvent(9701, slot=0, args=(1020, 1039))
    RunEvent(9702, slot=0, args=(1020, 1039))
    RunEvent(9703, slot=0, args=(1020, 1039))
    RunEvent(9710, slot=0, args=(1000, 1019))
    RunEvent(9720)
    RunEvent(9721)
    RunEvent(9722)
    RunEvent(9723)
    RunEvent(9755)
    RunEvent(9756)
    RunEvent(9770)
    RunEvent(9780)
    RunEvent(9781)
    RunEvent(9782)
    RunEvent(3500, slot=0, args=(4900, 6900, 6071, 6011))
    RunEvent(3500, slot=1, args=(4901, 6901, 6072, 6012))
    RunEvent(3500, slot=2, args=(4902, 6902, 6073, 6013))
    RunEvent(3503)
    GotoIfFlagOff(Label.L1, 6604)
    RemoveGoodFromPlayer(4000, quantity=1)
    RemoveGoodFromPlayer(4001, quantity=1)
    RemoveGoodFromPlayer(4003, quantity=1)
    RemoveGoodFromPlayer(4006, quantity=1)
    RemoveGoodFromPlayer(4009, quantity=1)
    RemoveGoodFromPlayer(4010, quantity=1)
    RemoveGoodFromPlayer(4011, quantity=1)
    RemoveGoodFromPlayer(4012, quantity=1)
    RemoveGoodFromPlayer(4013, quantity=1)
    RemoveGoodFromPlayer(4300, quantity=1)
    RemoveGoodFromPlayer(4305, quantity=1)
    RemoveGoodFromPlayer(4308, quantity=1)
    RemoveGoodFromPlayer(4310, quantity=1)
    RemoveGoodFromPlayer(4320, quantity=1)
    RemoveGoodFromPlayer(4321, quantity=1)
    RemoveGoodFromPlayer(4322, quantity=1)
    RemoveGoodFromPlayer(4323, quantity=1)
    RemoveGoodFromPlayer(4900, quantity=1)
    RemoveGoodFromPlayer(4901, quantity=1)
    RemoveGoodFromPlayer(4902, quantity=1)
    RemoveGoodFromPlayer(4903, quantity=1)
    RemoveGoodFromPlayer(4904, quantity=1)
    RemoveGoodFromPlayer(4905, quantity=1)
    RemoveGoodFromPlayer(4906, quantity=1)
    RemoveGoodFromPlayer(4907, quantity=1)
    RemoveGoodFromPlayer(4908, quantity=1)
    RemoveGoodFromPlayer(4014, quantity=1)
    RemoveGoodFromPlayer(4015, quantity=1)
    RemoveGoodFromPlayer(4021, quantity=1)
    RemoveGoodFromPlayer(4017, quantity=1)
    RemoveGoodFromPlayer(4018, quantity=1)
    RemoveGoodFromPlayer(4019, quantity=1)
    RemoveGoodFromPlayer(4020, quantity=1)
    RemoveGoodFromPlayer(4311, quantity=1)
    RemoveGoodFromPlayer(4340, quantity=1)
    RemoveGoodFromPlayer(4341, quantity=1)
    RemoveGoodFromPlayer(4342, quantity=1)
    RemoveGoodFromPlayer(700, quantity=99)
    DisableFlag(6604)

    # --- 1 --- #
    DefineLabel(1)


def Event3500(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 3500: Event 3500 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOff(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    RemoveGoodFromPlayer(arg_0_3, quantity=99)
    DisableFlag(arg_8_11)
    DisableFlag(arg_12_15)


@RestartOnRest
def Event6002():
    """ 6002: Event 6002 """
    EnableFlag(6000)
    DisableFlag(6001)


# Events 6680 to 6697 (weapon monitors) hijacked.

# Events 6788, 6789 (Vermin item management) hijacked, along with flag 6790 they used.


def Event6809():
    """ 6809: Event 6809 """
    DisableNetworkSync()
    IfEventValueComparison(0, 6800, bit_count=9, comparison_type=ComparisonType.GreaterThanOrEqual, value=1)
    EnableFlag(6810)
    IfEventValueComparison(0, 6800, bit_count=9, comparison_type=ComparisonType.GreaterThanOrEqual, value=2)
    EnableFlag(6811)
    IfEventValueComparison(0, 6800, bit_count=9, comparison_type=ComparisonType.GreaterThanOrEqual, value=5)
    EnableFlag(6812)


def Event6815():
    """ 6815: Event 6815 """
    DisableNetworkSync()
    IfFlagOn(1, 6813)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 6150, affect_npc_part_hp=False)
    IfFlagOff(-1, 6813)
    IfCharacterDoesNotHaveSpecialEffect(-1, PLAYER, 6142)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(PLAYER, 6150)
    Restart()


def Event6816():
    """ 6816: Event 6816 """
    DisableNetworkSync()
    IfFlagOn(1, 6814)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 6140, affect_npc_part_hp=False)
    IfFlagOff(-1, 6814)
    IfCharacterDoesNotHaveSpecialEffect(-1, PLAYER, 6142)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(PLAYER, 6140)
    Restart()


def ToggleLantern(_, lantern_chr: int, lantern_obj: int, required_flag: int, lantern_base_flag: int):
    """ 7000: Event 7000 """
    DisableNetworkSync()
    DisableCharacter(lantern_chr)
    DisableObject(lantern_obj)
    IfCharacterBackreadEnabled(0, lantern_chr)
    GotoIfFlagOn(Label.L0, required_flag)
    DisableCharacter(lantern_chr)
    DisableObject(lantern_obj)
    IfFlagOn(0, required_flag)
    EnableObject(lantern_obj)
    EnableCharacter(lantern_chr)
    CreateTemporaryVFX(100330, anchor_entity=lantern_obj, anchor_type=CoordEntityType.Object, model_point=100)

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(lantern_obj)
    EnableCharacter(lantern_chr)
    RegisterLantern(lantern_base_flag, lantern_obj, 0.0, reaction_angle=0.0, initial_sword_number=0, sword_level=0)


def LightLantern(_, light_lantern_request_flag: int, lantern_obj: int):
    """ 7100: Event 7100 """
    EndIfFlagOn(light_lantern_request_flag)
    IfFlagOn(0, light_lantern_request_flag)
    RotateToFaceEntity(PLAYER, lantern_obj, animation=101170, wait_for_completion=False)
    WaitFrames(32)
    InitializeWarpObject(lantern_obj)
    EndIfFlagOn(6715)
    WaitFrames(58)
    EnableFlag(70000030)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EnableFlag(6715)


def ArriveAtLantern(_, trigger_flag: int, lantern_obj: int):
    """ 7300: Event 7300 """
    EndIfClient()
    IfFlagOn(0, trigger_flag)
    WaitFrames(1)
    CreateTemporaryVFX(100321, anchor_entity=lantern_obj, anchor_type=CoordEntityType.Object, model_point=100)
    InitializeWarpObject(lantern_obj)
    DisableFlag(trigger_flag)


def Event7600(_, arg_0_3: int, arg_4_7: int):
    """ 7600: Event 7600 """
    DisableNetworkSync()
    DisableObject(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    IfConnectingMultiplayer(-1)
    IfMultiplayer(-1)
    IfConditionTrue(0, input_condition=-1)
    EnableObject(arg_0_3)
    CreateVFX(arg_4_7)
    IfConnectingMultiplayer(-2)
    IfMultiplayer(-2)
    IfConditionFalse(0, input_condition=-2)
    Restart()


def Event9030(_, arg_0_3: int, arg_4_7: int):
    """ 9030: Event 9030 """
    DisableNetworkSync()
    IfCharacterHasSpecialEffect(0, PLAYER, arg_0_3)
    AddSpecialEffect(PLAYER, arg_4_7, affect_npc_part_hp=False)
    IfCharacterDoesNotHaveSpecialEffect(0, PLAYER, arg_0_3)
    CancelSpecialEffect(PLAYER, arg_4_7)
    Restart()


def Event9035(_, arg_0_3: int, arg_4_7: int):
    """ 9035: Event 9035 """
    DisableNetworkSync()
    IfCharacterHasSpecialEffect(1, PLAYER, arg_0_3)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, arg_4_7, affect_npc_part_hp=False)
    IfCharacterHasSpecialEffect(2, PLAYER, arg_0_3)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfConditionFalse(0, input_condition=2)
    CancelSpecialEffect(PLAYER, arg_4_7)
    Restart()


def Event9040(_, arg_0_3: int, arg_4_7: int):
    """ 9040: Event 9040 """
    EndIfFlagOn(arg_0_3)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, arg_0_3)
    AwardItemLot(arg_4_7, host_only=False)


def Event9100(_, arg_0_3: int, arg_4_7: int):
    """ 9100: Event 9100 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, arg_0_3)
    DisableFlag(arg_0_3)
    AwardItemLot(arg_4_7, host_only=False)
    Restart()


def Event9110(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 9110: Event 9110 """
    EndIfFlagOn(arg_0_3)
    EndIfClient()
    IfFlagOn(0, arg_0_3)
    SkipLinesIfFlagOn(2, arg_12_15)
    AwardItemLot(arg_4_7, host_only=False)
    SkipLines(1)
    AwardItemLot(arg_8_11, host_only=False)


def Event9181():
    """ 9181: Event 9181 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfClientTypeCountComparison(0, ClientType.Coop, ComparisonType.GreaterThanOrEqual, value=1)
    DisableFlag(9185)
    IfCharacterDoesNotHaveSpecialEffect(0, PLAYER, 9000)
    Restart()


def Event9182():
    """ 9182: Event 9182 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(9184)
    IfConnectingMultiplayer(1)
    IfMultiplayer(2)
    IfConditionFalse(1, input_condition=2)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9184)
    IfConnectingMultiplayer(3)
    IfConditionFalse(-1, input_condition=3)
    IfMultiplayer(-1)
    IfConditionTrue(0, input_condition=-1)
    Restart()


def Event9183():
    """ 9183: Event 9183 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 9000)
    IfFlagOn(1, 9185)
    IfFlagOff(1, 9184)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    DisableFlag(9185)
    Wait(2.5)
    DisplayBattlefieldMessage(100300, display_location_index=0)
    Restart()


def Event9186():
    """ 9186: Event 9186 """
    DisableNetworkSync()
    EnableFlag(9187)
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    EnableFlag(9187)
    IfPlayerInsightAmountGreaterThanOrEqual(1, 1)
    IfFlagOff(1, 6009)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(9187)
    IfPlayerInsightAmountGreaterThanOrEqual(2, 1)
    IfFlagOff(2, 6009)
    IfConditionFalse(0, input_condition=2)
    Restart()


def Event9190():
    """ 9190: Event 9190 """
    DisableNetworkSync()
    IfMultiplayer(1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 9001, affect_npc_part_hp=False)
    IfMultiplayer(2)
    IfHost(2)
    IfConditionFalse(0, input_condition=2)
    CancelSpecialEffect(PLAYER, 9001)
    Restart()


def Event9191():
    """ 9191: Event 9191 """
    EndIfClient()
    IfInsideMap(-1, game_map=CHALICE_DUNGEON)
    IfInsideMap(-1, game_map=NIGHTMARE_OF_MENSIS)
    IfInsideMap(-1, game_map=NIGHTMARE_FRONTIER)
    GotoIfConditionTrue(Label.L0, input_condition=-1)
    EnableFlag(6500)
    IfFlagOn(0, 9800)
    EnableFlag(6501)
    IfFlagOn(0, 9801)
    EnableFlag(6502)
    IfFlagOn(0, 9802)
    EnableFlag(6503)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableFlagRange((6500, 6503))
    End()


def Event9192():
    """ 9192: Event 9192 """
    EndIfClient()
    EnableFlag(6400)
    IfFlagOn(0, 9800)
    EnableFlag(6401)
    IfFlagOn(0, 9801)
    EnableFlag(6402)
    IfFlagOn(0, 9802)
    EnableFlag(6403)


def Event9193():
    """ 9193: Event 9193 """
    EndIfClient()
    IfFlagOn(0, 6006)
    AddSpecialEffect(PLAYER, 6130, affect_npc_part_hp=False)
    IfFlagOff(0, 6006)
    CancelSpecialEffect(PLAYER, 6130)
    Restart()


def Event9198():
    """ 9198: Event 9198 """
    GotoIfFlagOn(Label.L0, 9199)
    IfCharacterHuman(1, PLAYER)
    IfCharacterHasSpecialEffect(1, PLAYER, 9000)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9185)
    IfTimeElapsed(0, 5.0)
    DisplayBattlefieldMessage(100001, display_location_index=0)
    EnableFlag(9199)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(2, PLAYER)
    IfCharacterDoesNotHaveSpecialEffect(2, PLAYER, 9000)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(9199)
    Restart()


def Event9200(_, arg_0_3: int):
    """ 9200: Event 9200 """
    DisableNetworkSync()
    DisableSoundEvent(arg_0_3)
    IfPlayerInsightAmountGreaterThanOrEqual(-1, 60)
    IfFlagOn(-1, 9802)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 9180)
    IfFlagOff(1, 9462)
    IfOutsideMap(1, game_map=NIGHTMARE_OF_MENSIS)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(arg_0_3)
    IfPlayerInsightAmountGreaterThanOrEqual(-2, 60)
    IfFlagOn(-2, 9802)
    IfConditionTrue(2, input_condition=-2)
    IfFlagOff(2, 9180)
    IfFlagOff(2, 9462)
    IfOutsideMap(2, game_map=NIGHTMARE_OF_MENSIS)
    IfConditionFalse(0, input_condition=2)
    Restart()


@RestartOnRest
def Event9220(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_16: uchar, arg_17_17: uchar):
    """ 9220: Event 9220 """
    GotoIfFlagOff(Label.L0, arg_8_11)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7010)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EndIfFlagOn(arg_4_7)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7010, loop=True)
    IfOnline(1)
    IfFlagOff(1, arg_8_11)
    IfCharacterAlive(1, arg_0_3)
    IfFlagOff(1, arg_12_15)
    IfInsideMap(1, game_map=(arg_16_16, arg_17_17))
    IfCharacterHuman(2, PLAYER)
    IfPlayerSoulLevelGreaterThanOrEqual(2, 30)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.GreaterThanOrEqual, value=1)
    IfCharacterHasSpecialEffect(3, PLAYER, 9025)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IfRandomTimeElapsed(0, min_seconds=10.0, max_seconds=10.0)
    DisplayBattlefieldMessage(109000, display_location_index=0)
    ForceAnimation(arg_0_3, 7011)
    WaitFrames(59)
    EnableAI(arg_0_3)
    EnableFlag(arg_4_7)


@RestartOnRest
def Event9240(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_16: uchar, arg_17_17: uchar):
    """ 9240: Event 9240 """
    EndIfFlagOn(arg_8_11)
    IfFlagOn(1, arg_4_7)
    IfFlagOff(1, arg_12_15)
    IfFlagOff(1, arg_8_11)
    IfInsideMap(1, game_map=(arg_16_16, arg_17_17))
    IfClientTypeCountComparison(1, ClientType.Invader, ComparisonType.Equal, value=0)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(2, PLAYER)
    IfRandomTimeElapsed(2, min_seconds=10.0, max_seconds=10.0)
    IfConditionTrue(0, input_condition=2)
    AddSpecialEffect(PLAYER, 9020, affect_npc_part_hp=False)
    AddSpecialEffect(arg_0_3, 9100, affect_npc_part_hp=False)
    ReplanAI(arg_0_3)
    EnableFlag(arg_12_15)
    DisplayBattlefieldMessage(100002, display_location_index=0)
    Restart()


@RestartOnRest
def Event9260(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_16: uchar, arg_17_17: uchar):
    """ 9260: Event 9260 """
    EndIfFlagOn(arg_8_11)
    IfFlagOn(1, arg_4_7)
    IfFlagOn(1, arg_12_15)
    IfFlagOn(-1, arg_8_11)
    IfClientTypeCountComparison(-1, ClientType.Invader, ComparisonType.GreaterThanOrEqual, value=1)
    IfOutsideMap(-1, game_map=(arg_16_16, arg_17_17))
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(0, PLAYER)
    CancelSpecialEffect(PLAYER, 9020)
    CancelSpecialEffect(arg_0_3, 9100)
    ReplanAI(arg_0_3)
    DisableFlag(arg_12_15)
    Restart()


def Event9280(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_20: uchar, arg_21_21: uchar
):
    """ 9280: Event 9280 """
    IfFlagOn(-15, arg_8_11)
    IfFlagOn(-15, arg_12_15)
    IfFlagOn(-15, arg_16_19)
    EndIfConditionTrue(-15)
    IfFlagOn(1, arg_4_7)
    IfInsideMap(1, game_map=(arg_20_20, arg_21_21))
    IfHealthEqual(2, arg_0_3, 0.0)
    IfFlagOn(3, arg_16_19)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_8_11)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=3)
    Wait(5.0)
    DisplayBattlefieldMessage(109001, display_location_index=0)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7012)
    WaitFrames(88)
    ForceAnimation(arg_0_3, 7010)


def GainInsight(_, insight_count: int):
    """ 9350: Grants the player up to 9 insight by repeatedly applying SpEffect 4680. """
    EndIfClient()
    GotoIfValueComparison(Label.L1, ComparisonType.Equal, left=insight_count, right=1)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=insight_count, right=2)
    GotoIfValueComparison(Label.L3, ComparisonType.Equal, left=insight_count, right=3)
    GotoIfValueComparison(Label.L4, ComparisonType.Equal, left=insight_count, right=4)
    GotoIfValueComparison(Label.L5, ComparisonType.Equal, left=insight_count, right=5)
    GotoIfValueComparison(Label.L6, ComparisonType.Equal, left=insight_count, right=6)
    GotoIfValueComparison(Label.L7, ComparisonType.Equal, left=insight_count, right=7)
    GotoIfValueComparison(Label.L8, ComparisonType.Equal, left=insight_count, right=8)
    GotoIfValueComparison(Label.L9, ComparisonType.Equal, left=insight_count, right=9)
    End()

    # --- 9 --- #
    DefineLabel(9)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 8 --- #
    DefineLabel(8)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 7 --- #
    DefineLabel(7)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 6 --- #
    DefineLabel(6)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 5 --- #
    DefineLabel(5)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 4 --- #
    DefineLabel(4)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 1 --- #
    DefineLabel(1)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)


def Event9440(_, arg_0_3: int, arg_4_7: int):
    """ 9440: Event 9440 """
    DisableNetworkSync()
    EndIfThisEventSlotOn()
    EndIfClient()
    IfFlagOn(0, arg_0_3)
    AwardItemLot(arg_4_7, host_only=False)


def Event9480(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 9480: Event 9480 """
    EndIfThisEventSlotOn()
    EndIfFlagOn(arg_0_3)
    EndIfFlagOn(arg_4_7)
    EndIfFlagOn(arg_8_11)
    IfFlagOn(-1, arg_0_3)
    IfFlagOn(-1, arg_4_7)
    IfFlagOn(-1, arg_8_11)
    IfFlagOn(-1, arg_12_15)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(2, arg_16_19)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(2)
    IfCharacterHuman(-3, PLAYER)
    IfCharacterType(-3, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(3, input_condition=-3)
    IfCharacterHasSpecialEffect(3, PLAYER, 6100)
    EndIfConditionFalse(3)
    AwardItemLot(5520, host_only=True)


def Event9500(_, arg_0_3: int, arg_4_7: int):
    """ 9500: Event 9500 """
    DisableNetworkSync()
    IfCharacterHasSpecialEffect(0, PLAYER, arg_0_3)
    AwardItemLot(arg_4_7, host_only=True)
    Wait(0.10000000149011612)
    Restart()


def Event9700(_, arg_0_3: int, arg_4_7: int):
    """ 9700: Event 9700 """
    IfFlagOn(1, 1021)
    IfFlagOn(1, 72100121)
    IfOutsideMap(1, game_map=HUNTERS_DREAM)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1022)


def Event9701(_, arg_0_3: int, arg_4_7: int):
    """ 9701: Event 9701 """
    IfFlagOn(1, 1023)
    IfFlagOn(1, 72100123)
    IfOutsideMap(1, game_map=HUNTERS_DREAM)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1024)


def Event9702(_, arg_0_3: int, arg_4_7: int):
    """ 9702: Event 9702 """
    IfFlagOn(1, 1025)
    IfFlagOn(1, 72100125)
    IfOutsideMap(1, game_map=HUNTERS_DREAM)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1026)


def Event9703(_, arg_0_3: int, arg_4_7: int):
    """ 9703: Event 9703 """
    IfFlagOn(1, 1026)
    IfFlagOn(1, 9802)
    IfFlagOn(1, 72100128)
    IfOutsideMap(1, game_map=HUNTERS_DREAM)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1027)


def Event9710(_, arg_0_3: int, arg_4_7: int):
    """ 9710: Event 9710 """
    IfFlagOn(1, 1000)
    IfFlagOn(1, 72100110)
    IfOutsideMap(1, game_map=HUNTERS_DREAM)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(1001)


def Event9720():
    """ 9720: Event 9720 """
    GotoIfThisEventOn(Label.L0)
    GotoIfFlagOn(Label.L0, 12410810)
    GotoIfFlagOn(Label.L0, 9467)
    IfFlagOn(1, 1362)
    IfFlagOn(1, 72400520)
    IfInsideMap(1, game_map=HUNTERS_DREAM)
    IfFlagOn(2, 1363)
    IfFlagOn(-1, 1701)
    IfFlagOn(-1, 1702)
    IfConditionTrue(3, input_condition=-1)
    IfFlagOn(-2, 1368)
    IfFlagOn(-2, 1369)
    IfConditionTrue(3, input_condition=-2)
    IfFlagOn(-3, 12410810)
    IfFlagOn(-3, 9467)
    IfConditionTrue(-4, input_condition=1)
    IfConditionTrue(-4, input_condition=2)
    IfConditionTrue(-4, input_condition=3)
    IfConditionTrue(-4, input_condition=-3)
    IfConditionTrue(0, input_condition=-4)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=-3)
    EnableFlag(70002413)
    IfFlagOn(-5, 12410810)
    IfFlagOn(-5, 9467)
    IfConditionTrue(0, input_condition=-5)

    # --- 0 --- #
    DefineLabel(0)
    DisableFlag(70002413)


def Event9721():
    """ 9721: Event 9721 """
    GotoIfThisEventOn(Label.L0)
    IfFlagOn(1, 1371)
    IfFlagOn(2, 1705)
    IfCharacterDead(2, 2400902)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    DisableFlag(70002401)


def Event9722():
    """ 9722: Event 9722 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(1, 1373)
    IfFlagOn(1, 9802)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1360, 1379))
    EnableFlag(1370)
    EnableFlag(70002401)


def Event9723():
    """ 9723: Event 9723 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(1, 1374)
    IfFlagOn(1, 9802)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1360, 1379))
    EnableFlag(1372)
    EnableFlag(70002401)


def Event9755():
    """ 9755: Event 9755 """
    IfFlagOn(-2, 1205)
    IfFlagOn(-2, 1207)
    IfConditionTrue(1, input_condition=-2)
    IfFlagOn(1, 72400360)
    IfFlagChange(-1, 12201800)
    IfFlagChange(-1, 12301800)
    IfFlagChange(-1, 12301700)
    IfFlagChange(-1, 12401800)
    IfFlagChange(-1, 12411800)
    IfFlagChange(-1, 12411700)
    IfFlagChange(-1, 12421800)
    IfFlagChange(-1, 12421700)
    IfFlagChange(-1, 12501800)
    IfFlagChange(-1, 12601800)
    IfFlagChange(-1, 12601850)
    IfFlagChange(-1, 12701800)
    IfFlagChange(-1, 12801800)
    IfFlagChange(-1, 13201800)
    IfFlagChange(-1, 13301800)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IncrementEventValue(70000200, bit_count=3, max_value=7)
    Restart()


def Event9756():
    """ 9756: Event 9756 """
    IfFlagOn(-2, 1205)
    IfFlagOn(-2, 1207)
    IfConditionTrue(1, input_condition=-2)
    IfFlagOn(1, 72400360)
    IfInsideMap(1, game_map=CHALICE_DUNGEON)
    IfFlagChange(-1, 12901800)
    IfFlagChange(-1, 12901801)
    IfFlagChange(-1, 12901802)
    IfFlagChange(-1, 12901803)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IncrementEventValue(70000200, bit_count=3, max_value=7)
    Restart()


def Event9770():
    """ 9770: Event 9770 """
    IfFlagOn(1, 1351)
    IfOutsideMap(1, game_map=CASTLE_CAINHURST)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(72500359)


def Event9780():
    """ 9780: Event 9780 """
    IfFlagOn(1, 1422)
    IfOutsideMap(1, game_map=BYRGENWERTH)
    IfFlagOn(1, 73200326)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1420, 1437))
    EnableFlag(1423)


def Event9781():
    """ 9781: Event 9781 """
    EndIfThisEventOn()
    IfCharacterHuman(1, PLAYER)
    IfInsideMap(1, game_map=FORBIDDEN_WOODS)
    IfConditionTrue(0, input_condition=1)
    EndIfFlagOn(1438)
    EnableFlag(1439)
    EnableFlag(72410382)


def Event9782():
    """ 9782: Event 9782 """
    IfPlayerHasGood(1, 4310, including_box=False)
    IfInsideMap(-2, game_map=HUNTERS_DREAM)
    IfCharacterDead(-2, PLAYER)
    IfConditionTrue(1, input_condition=-2)
    IfFlagOn(2, 1431)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    EnableFlag(1438)
    DisableFlag(1439)


def Event9909():
    """ 9909: Event 9909 """
    EndIfFlagOn(9900)
    IfEventValueComparison(0, 9901, bit_count=4, comparison_type=ComparisonType.GreaterThanOrEqual, value=3)
    EnableFlag(9900)


def Event9905(_, arg_0_3: int):
    """ 9905: Event 9905 """
    EndIfThisEventSlotOn()
    IfCharacterHasSpecialEffect(0, PLAYER, arg_0_3)
    IncrementEventValue(9901, bit_count=4, max_value=4)


def Event9910():
    """ 9910: Event 9910 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfThisEventOn()
    SkipLinesIfFlagOn(3, 6300)
    DisableFlag(50000400)
    EnableFlag(50000405)
    SkipLines(2)
    EnableFlag(50000400)
    DisableFlag(50000405)
    SkipLinesIfFlagOn(3, 6301)
    DisableFlag(50000600)
    EnableFlag(50000605)
    SkipLines(2)
    EnableFlag(50000600)
    DisableFlag(50000605)
    SkipLinesIfFlagOn(3, 6302)
    DisableFlag(50000800)
    EnableFlag(50000801)
    SkipLines(2)
    EnableFlag(50000800)
    DisableFlag(50000801)
    SkipLinesIfFlagOn(3, 6303)
    DisableFlag(50001100)
    EnableFlag(50001105)
    SkipLines(2)
    EnableFlag(50001100)
    DisableFlag(50001105)
    SkipLinesIfFlagOn(3, 6304)
    DisableFlag(50001300)
    EnableFlag(50001301)
    SkipLines(2)
    EnableFlag(50001300)
    DisableFlag(50001301)
    SkipLinesIfFlagOn(3, 6305)
    DisableFlag(50001610)
    EnableFlag(50001611)
    SkipLines(2)
    EnableFlag(50001610)
    DisableFlag(50001611)
    SkipLinesIfFlagOn(3, 6306)
    DisableFlag(50002110)
    EnableFlag(50002115)
    SkipLines(2)
    EnableFlag(50002110)
    DisableFlag(50002115)
    SkipLinesIfFlagOn(3, 6307)
    DisableFlag(50003400)
    EnableFlag(50003405)
    SkipLines(2)
    EnableFlag(50003400)
    DisableFlag(50003405)
    SkipLinesIfFlagOn(3, 6308)
    DisableFlag(50003500)
    EnableFlag(50003505)
    SkipLines(2)
    EnableFlag(50003500)
    DisableFlag(50003505)
    SkipLinesIfFlagOn(4, 6340)
    DisableFlag(50000200)
    DisableFlag(50000205)
    EnableFlag(50000210)
    SkipLines(3)
    EnableFlag(50000200)
    EnableFlag(50000205)
    DisableFlag(50000210)
    SkipLinesIfFlagOn(3, 6341)
    DisableFlag(50001820)
    EnableFlag(50001825)
    SkipLines(2)
    EnableFlag(50001820)
    DisableFlag(50001825)
    SkipLinesIfFlagOn(5, 6342)
    DisableFlag(50001910)
    EnableFlag(50001915)
    DisableFlag(50001900)
    EnableFlag(50001905)
    SkipLines(4)
    EnableFlag(50001910)
    DisableFlag(50001915)
    DisableFlag(50001900)
    EnableFlag(50001905)
    SkipLinesIfFlagOn(3, 6334)
    DisableFlag(50003100)
    EnableFlag(50003105)
    SkipLines(2)
    EnableFlag(50003100)
    DisableFlag(50003105)
    SkipLinesIfFlagOn(3, 6335)
    DisableFlag(50001500)
    EnableFlag(50001505)
    SkipLines(2)
    EnableFlag(50001500)
    DisableFlag(50001505)
    SkipLinesIfFlagOn(3, 6641)
    DisableFlag(50001700)
    EnableFlag(50001701)
    SkipLines(2)
    EnableFlag(50001700)
    DisableFlag(50001701)
    SkipLinesIfFlagOn(3, 6643)
    DisableFlag(50001900)
    EnableFlag(50001905)
    SkipLines(2)
    EnableFlag(50001900)
    DisableFlag(50001905)
    SkipLinesIfFlagOn(3, 6647)
    DisableFlag(50001810)
    EnableFlag(50001805)
    SkipLines(2)
    EnableFlag(50001810)
    DisableFlag(50001805)
    SkipLinesIfFlagOn(3, 6649)
    DisableFlag(50000205)
    EnableFlag(50000210)
    SkipLines(2)
    EnableFlag(50000205)
    DisableFlag(50000210)
    SkipLinesIfFlagOn(3, 6677)
    DisableFlag(50002260)
    EnableFlag(50002261)
    SkipLines(2)
    EnableFlag(50002260)
    DisableFlag(50002261)


# NEW BOSS RUSH STUFF


def ControlBossRushLantern(_, lantern_chr: int, lantern_obj: int, boss_dead_flag: int):
    """ 7200: Enable given lantern when given boss death flag is enabled, and monitor interaction with it.

    Alternatively, just warps player back to the dream automatically if there's no next boss to go to, because this is
    either a single fight or because you just finished the boss rush.

    The lantern has a simple "Face next foe" prompt when approached. When you interact with it, the Boss Rush event
    looks up the next boss (either random or in story order) and warps you to the appropriate arena.

    The `boss_dead_flag` should only be enabled on map load if there are multiple bosses in this map and the player is
    currently fighting another one. In that case, this event will end immediately after the lantern is disabled (so
    Gehrman and Moon Presence lanterns behave correctly).

    This event ID used to warp the player back to Hunter's Dream when a lantern was used properly.
    """
    if lantern_chr != 0:
        DisableCharacter(lantern_chr)  # always disabled, since prompt is so simple
    DisableObject(lantern_obj)

    # If boss is already dead, just end here and leave lantern disabled.
    EndIfFlagOn(boss_dead_flag)

    await FlagEnabled(boss_dead_flag)

    GainInsight(0, 2)  # replaces all boss-specific insight gains

    if not BossRushFlags.BossRushActive:
        # This is a single boss fight. Warp back to Dream after waiting long enough for the boss death sound to play.
        Wait(5.0)
        EnableFlag(BossRushFlags.RequestDreamReturn)
        return

    WaitFrames(5)  # give boss rush completion flag a chance to be enabled
    if BossRushFlags.BossRushCompleted:
        Wait(7.0)
        DisplayBanner(BannerType.NightmareSlain)
        AwardItemLot(BossRushItemLots.BossRushReward)  # first time only (item lot flag 6620)
        GainInsight(0, 5)  # Can only apply up to 9 insight in one event call, so doing 10 * 5.
        GainInsight(1, 5)  # Fortunately, slots 1-9 of 9350 do not appear to clash with other event IDs.
        GainInsight(2, 5)
        GainInsight(3, 5)
        GainInsight(4, 5)
        GainInsight(5, 5)
        GainInsight(6, 5)
        GainInsight(7, 5)
        GainInsight(8, 5)
        GainInsight(9, 5)
        Wait(9.0)
        EnableFlag(BossRushFlags.RequestDreamReturn)
        return

    # Wait for player to continue boss rush at lantern.

    EnableObject(lantern_obj)
    CreateTemporaryVFX(100330, anchor_entity=lantern_obj, anchor_type=CoordEntityType.Object, model_point=100)

    IfActionButtonParam(0, 6100, entity=lantern_obj)  # "Face next foe"

    # Remove blood bullets, but keep existing vials/bullets.
    # RemoveGoodFromPlayer(BossRushGoods.BloodVial, 99)
    # RemoveGoodFromPlayer(BossRushGoods.QuicksilverBullet, 99)
    RemoveGoodFromPlayer(BossRushGoods.BloodBullet, 99)
    AwardItemLot(BossRushItemLots.VialRefill10)  # give 10 extra, rather than setting to 20 exactly
    AwardItemLot(BossRushItemLots.BulletRefill10)  # give 10 extra, rather than setting to 20 exactly

    Wait(2.0)
    if BossRushFlags.BossRushRandomized:
        EnableRandomBossWarpFlag()
    else:
        EnableNextStoryBossWarpFlag()


def WarpToBoss(_, required_boss_warp_flag: int, warp_point: int):
    """ 9360: Warp player to requested next boss in Boss Rush.

    This event ID + slots used to be for awarding Blood Dregs.
    """
    Wait(2.0)  # give other events a chance to run first
    Await(FlagEnabled(required_boss_warp_flag) and not BossRushFlags.ChoosingRandomBoss)
    DisableFlag(required_boss_warp_flag)
    WarpPlayerToRespawnPoint(warp_point)
    return RESTART


def MonitorStoryBossRushRequest():
    """ 6680: Start a new Story Boss Rush when request item is used in the Dream. Return to the Dream otherwise. """
    Await(HasSpecialEffect(PLAYER, BossRushEffects.StoryRushRequest))

    if not InsideMap(HUNTERS_DREAM):
        # End boss rush/challenge.
        Wait(1.0)
        EnableFlag(BossRushFlags.RequestDreamReturn)
        return

    # Start story boss rush.
    Wait(2.0)
    DisableFlag(BossRushFlags.BossRushCompleted)
    EnableFlag(BossRushFlags.BossRushActive)
    DisableFlag(BossRushFlags.BossRushRandomized)  # just for clarity here
    RemoveGoodFromPlayer(BossRushGoods.BloodVial, 99)
    RemoveGoodFromPlayer(BossRushGoods.QuicksilverBullet, 99)
    RemoveGoodFromPlayer(BossRushGoods.BloodBullet, 99)
    AwardItemLot(BossRushItemLots.VialRefill20)
    AwardItemLot(BossRushItemLots.BulletRefill20)

    Wait(1.0)
    EnableNextStoryBossWarpFlag()


def MonitorRandomBossRushRequest():
    """ 6681: Starts a new Random Boss Rush when bell is rung, or ends current boss rush.

    This event ID used to monitor Loch Shield possession.
    """
    Await(HasSpecialEffect(PLAYER, BossRushEffects.RandomRushRequest))

    if not InsideMap(HUNTERS_DREAM):
        # End boss rush.
        Wait(1.0)
        EnableFlag(BossRushFlags.RequestDreamReturn)
        return

    # Start random boss rush.
    Wait(2.0)
    DisableFlag(BossRushFlags.BossRushCompleted)
    EnableFlag(BossRushFlags.BossRushActive)
    EnableFlag(BossRushFlags.BossRushRandomized)
    RemoveGoodFromPlayer(BossRushGoods.BloodVial, 99)
    RemoveGoodFromPlayer(BossRushGoods.QuicksilverBullet, 99)
    RemoveGoodFromPlayer(BossRushGoods.BloodBullet, 99)
    AwardItemLot(BossRushItemLots.VialRefill20)
    AwardItemLot(BossRushItemLots.BulletRefill20)

    Wait(1.0)
    EnableRandomBossWarpFlag()


def FinishBossRush():
    """ 6682: Enables completion flag when every boss is dead.

    This event ID used to monitor Beasthunter Saif possession.
    """
    IfFlagOn(1, BossRushFlags.BossDead_ClericBeast)
    IfFlagOn(1, BossRushFlags.BossDead_FatherGascoigne)
    IfFlagOn(1, BossRushFlags.BossDead_BloodStarvedBeast)
    IfFlagOn(1, BossRushFlags.BossDead_WitchesOfHemwick)
    IfFlagOn(1, BossRushFlags.BossDead_VicarAmelia)
    IfFlagOn(1, BossRushFlags.BossDead_DarkbeastPaarl)
    IfFlagOn(1, BossRushFlags.BossDead_ShadowsOfYharnam)
    IfFlagOn(1, BossRushFlags.BossDead_Rom)
    IfFlagOn(1, BossRushFlags.BossDead_Amygdala)
    IfFlagOn(1, BossRushFlags.BossDead_MartyrLogarius)
    IfFlagOn(1, BossRushFlags.BossDead_TheOneReborn)
    IfFlagOn(1, BossRushFlags.BossDead_CelestialEmissary)
    IfFlagOn(1, BossRushFlags.BossDead_Ebrietas)
    IfFlagOn(1, BossRushFlags.BossDead_Micolash)
    IfFlagOn(1, BossRushFlags.BossDead_MergosWetNurse)
    IfFlagOn(1, BossRushFlags.BossDead_Ludwig)
    IfFlagOn(1, BossRushFlags.BossDead_LivingFailures)
    IfFlagOn(1, BossRushFlags.BossDead_LadyMaria)
    IfFlagOn(1, BossRushFlags.BossDead_Laurence)
    IfFlagOn(1, BossRushFlags.BossDead_OrphanOfKos)
    IfFlagOn(1, BossRushFlags.BossDead_Gehrman)
    IfFlagOn(1, BossRushFlags.BossDead_MoonPresence)
    IfConditionTrue(0, 1)
    EnableFlag(BossRushFlags.BossRushCompleted)


def EnableNextStoryBossWarpFlag():
    """ 6683: Enable the next story boss warp flag, based on the last-numbered boss death flag.

    This event ID used to monitor Beast Claw possession.
    """

    SkipLinesIfFlagOff(3, BossRushFlags.BossDead_Gehrman)
    EnableFlag(BossRushFlags.RequestBoss_MoonPresence)
    EnableFlag(BossRushFlags.MoonPresenceRequested)  # tells Hunter's Dream which boss to prepare
    Goto(Label.L0)

    SkipLinesIfFlagOff(3, BossRushFlags.BossDead_OrphanOfKos)
    EnableFlag(BossRushFlags.RequestBoss_Gehrman)
    DisableFlag(BossRushFlags.MoonPresenceRequested)  # just in case
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.BossDead_Laurence)
    EnableFlag(BossRushFlags.RequestBoss_OrphanOfKos)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.BossDead_LadyMaria)
    EnableFlag(BossRushFlags.RequestBoss_Laurence)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.BossDead_LivingFailures)
    EnableFlag(BossRushFlags.RequestBoss_LadyMaria)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.BossDead_Ludwig)
    EnableFlag(BossRushFlags.RequestBoss_LivingFailures)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.BossDead_MergosWetNurse)
    EnableFlag(BossRushFlags.RequestBoss_Ludwig)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.BossDead_Micolash)
    EnableFlag(BossRushFlags.RequestBoss_MergosWetNurse)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.BossDead_Ebrietas)
    EnableFlag(BossRushFlags.RequestBoss_Micolash)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.BossDead_CelestialEmissary)
    EnableFlag(BossRushFlags.RequestBoss_Ebrietas)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.BossDead_TheOneReborn)
    EnableFlag(BossRushFlags.RequestBoss_CelestialEmissary)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.BossDead_MartyrLogarius)
    EnableFlag(BossRushFlags.RequestBoss_TheOneReborn)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.BossDead_Amygdala)
    EnableFlag(BossRushFlags.RequestBoss_MartyrLogarius)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.BossDead_Rom)
    EnableFlag(BossRushFlags.RequestBoss_Amygdala)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.BossDead_ShadowsOfYharnam)
    EnableFlag(BossRushFlags.RequestBoss_Rom)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.BossDead_DarkbeastPaarl)
    EnableFlag(BossRushFlags.RequestBoss_ShadowsOfYharnam)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.BossDead_VicarAmelia)
    EnableFlag(BossRushFlags.RequestBoss_DarkbeastPaarl)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.BossDead_WitchesOfHemwick)
    EnableFlag(BossRushFlags.RequestBoss_VicarAmelia)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.BossDead_BloodStarvedBeast)
    EnableFlag(BossRushFlags.RequestBoss_WitchesOfHemwick)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.BossDead_FatherGascoigne)
    EnableFlag(BossRushFlags.RequestBoss_BloodStarvedBeast)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.BossDead_ClericBeast)
    EnableFlag(BossRushFlags.RequestBoss_FatherGascoigne)
    Goto(Label.L0)

    # Cleric Beast isn't dead (i.e. this was activated from the Hunter's Dream).
    EnableFlag(BossRushFlags.RequestBoss_ClericBeast)

    # --- 0 --- #
    DefineLabel(Label.L0)
    DisableFlag(BossRushFlags.ChoosingRandomBoss)  # just in case


def EnableRandomBossWarpFlag():
    """ 6684: Enable a random boss warp flag whose dead flag is disabled.

    Keeps restarting until a flag is enabled for a non-dead boss. Of course, this could theoretically take forever if
    you're infinitely unlucky, but in reality it's fine and too annoying to do anything better (like randomly ordering
    1-22 and trying each one in turn).

    This event ID used to kick the player out of the DLC if they lost access.
    """
    EnableFlag(BossRushFlags.ChoosingRandomBoss)

    DisableFlagRange((BossRushFlags.RequestBoss_ClericBeast, BossRushFlags.RequestBoss_MoonPresence))
    EnableRandomFlagInRange((BossRushFlags.RequestBoss_ClericBeast, BossRushFlags.RequestBoss_MoonPresence))

    SkipLinesIfFlagOff(2, BossRushFlags.RequestBoss_ClericBeast)
    RestartIfFlagOn(BossRushFlags.BossDead_ClericBeast)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.RequestBoss_FatherGascoigne)
    RestartIfFlagOn(BossRushFlags.BossDead_FatherGascoigne)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.RequestBoss_BloodStarvedBeast)
    RestartIfFlagOn(BossRushFlags.BossDead_BloodStarvedBeast)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.RequestBoss_WitchesOfHemwick)
    RestartIfFlagOn(BossRushFlags.BossDead_WitchesOfHemwick)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.RequestBoss_VicarAmelia)
    RestartIfFlagOn(BossRushFlags.BossDead_VicarAmelia)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.RequestBoss_DarkbeastPaarl)
    RestartIfFlagOn(BossRushFlags.BossDead_DarkbeastPaarl)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.RequestBoss_ShadowsOfYharnam)
    RestartIfFlagOn(BossRushFlags.BossDead_ShadowsOfYharnam)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.RequestBoss_Rom)
    RestartIfFlagOn(BossRushFlags.BossDead_Rom)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.RequestBoss_Amygdala)
    RestartIfFlagOn(BossRushFlags.BossDead_Amygdala)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.RequestBoss_MartyrLogarius)
    RestartIfFlagOn(BossRushFlags.BossDead_MartyrLogarius)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.RequestBoss_TheOneReborn)
    RestartIfFlagOn(BossRushFlags.BossDead_TheOneReborn)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.RequestBoss_CelestialEmissary)
    RestartIfFlagOn(BossRushFlags.BossDead_CelestialEmissary)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.RequestBoss_Ebrietas)
    RestartIfFlagOn(BossRushFlags.BossDead_Ebrietas)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.RequestBoss_Micolash)
    RestartIfFlagOn(BossRushFlags.BossDead_Micolash)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.RequestBoss_MergosWetNurse)
    RestartIfFlagOn(BossRushFlags.BossDead_MergosWetNurse)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.RequestBoss_Ludwig)
    RestartIfFlagOn(BossRushFlags.BossDead_Ludwig)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.RequestBoss_LivingFailures)
    RestartIfFlagOn(BossRushFlags.BossDead_LivingFailures)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.RequestBoss_LadyMaria)
    RestartIfFlagOn(BossRushFlags.BossDead_LadyMaria)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.RequestBoss_Laurence)
    RestartIfFlagOn(BossRushFlags.BossDead_Laurence)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.RequestBoss_OrphanOfKos)
    RestartIfFlagOn(BossRushFlags.BossDead_OrphanOfKos)
    Goto(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.RequestBoss_Gehrman)
    RestartIfFlagOn(BossRushFlags.BossDead_Gehrman)
    Goto(Label.L0)

    # --- 0 ---
    DefineLabel(Label.L0)

    SkipLinesIfFlagOff(2, BossRushFlags.RequestBoss_MoonPresence)
    EnableFlag(BossRushFlags.MoonPresenceRequested)  # tells Hunter's Dream which boss to prepare
    SkipLines(1)
    DisableFlag(BossRushFlags.MoonPresenceRequested)  # just in case

    DisableFlag(BossRushFlags.ChoosingRandomBoss)  # boss warps allowed again


def WarpBackToDream():
    """ 6685: Warp back to Hunter's Dream when requested.

    This event ID used to play some random sounds in the DLC.
    """
    IfFlagOn(-1, BossRushFlags.RequestDreamReturn)
    IfCharacterHasSpecialEffect(-1, PLAYER, BossRushEffects.ImmediateDreamReturnRequest)
    IfConditionTrue(0, -1)

    DisableFlag(BossRushFlags.RequestDreamReturn)
    WarpPlayerToRespawnPoint(BossRushWarpPoints.HuntersDream)


def ManageGems():
    """ 6692: Check which gem player has and apply effect. Checks every second as long as player has no gem effects.

    19410: +18% Slash
    20410: +18% Blunt
    21410: +18% Piercing
    22410: +18% Neutral (Guns)
    23410: +15% Arcane (Magic element)
    24410: +15% Fire (Fire element)
    25410: +15% Bolt (Lightning element)
    26410: +15% Physical
    27410: +13% All
    """

    for offset, effect in zip(
        (0, 10, 20, 30, 40, 50, 60, 70, 80),
        (19410, 20410, 21410, 22410, 23410, 24410, 25410, 26410, 27410),
    ):
        SkipLinesIfFlagOff(1, 12112600 + offset + 9)
        AddSpecialEffect(PLAYER, effect, affect_npc_part_hp=False)

    # Waits until player has no gem effects (e.g. they swapped weapons) before running again, with a minimum wait of
    # one second.
    Wait(1.0)
    for effect in (19410, 20410, 21410, 22410, 23410, 24410, 25410, 26410, 27410):
        IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, effect)
    IfConditionTrue(0, 1)
    return RESTART


def ManageNormalRunes():
    """ 6693: Check which rune player has and apply effect. """

    for offset, effect in zip(
        (0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180),
        (
            103002, 105002, 107002, 108002, 110002, 112002, 118002, 119002, 121002, 122002,
            123002, 125002, 126002, 127002, 128002, 129002, 134004, 136004, 141002,
        ),
    ):
        SkipLinesIfFlagOff(1, 12112700 + offset + 9)
        AddSpecialEffect(PLAYER, effect, affect_npc_part_hp=False)

    # Only runs once per load.
    return


def ManageCovenantRunes():
    """ 6694: Check which covenant rune player has and apply effect.

    180000: +2% Blood Vial (Radiance)
    180010: Heal below 12.5% HP (Corruption)
    180020: +3 stamina recovery (Hunter)
    250, 252, 253, 180050: Beast
    255, 257, 180060: Milkweed
    """

    # Radiance
    SkipLinesIfFlagOff(1, 12112909)
    AddSpecialEffect(PLAYER, 180000, affect_npc_part_hp=False)

    # Corruption
    SkipLinesIfFlagOff(1, 12112919)
    AddSpecialEffect(PLAYER, 180010, affect_npc_part_hp=False)

    # Hunter
    SkipLinesIfFlagOff(1, 12112929)
    AddSpecialEffect(PLAYER, 180020, affect_npc_part_hp=False)

    # Beast
    SkipLinesIfFlagOff(4, 12112939)
    AddSpecialEffect(PLAYER, 250, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 252, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 253, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 180050, affect_npc_part_hp=False)

    # Milkweed
    SkipLinesIfFlagOff(3, 12112949)
    AddSpecialEffect(PLAYER, 255, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 257, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 180060, affect_npc_part_hp=False)

    # Only runs once per load.
    return


def MonitorGemPurchase():
    """ 6695: Monitor whenever player purchases a new gem, and control flags.

    This extra layer of flags is necessary to properly control effects in above events, as otherwise multiple gems could
    be bought in sequence and mess up the shop flags.

    Normally we would use slots for this, but I'm too lazy to find event ID ranges.
    """
    if not InsideMap(HUNTERS_DREAM):
        return  # only needs to run in Dream

    SkipLinesIfFlagOn(12, 12112609)
    SkipLinesIfFlagOff(11, 12112600)
    RemoveGoodFromPlayer(4420)
    RemoveGoodFromPlayer(4421)
    RemoveGoodFromPlayer(4422)
    RemoveGoodFromPlayer(4423)
    RemoveGoodFromPlayer(4424)
    RemoveGoodFromPlayer(4425)
    RemoveGoodFromPlayer(4426)
    RemoveGoodFromPlayer(4427)
    DisableFlagRange((12112600, 12112699))
    EnableFlag(12112600)
    EnableFlag(12112609)
    SkipLinesIfFlagOn(12, 12112619)
    SkipLinesIfFlagOff(11, 12112610)
    RemoveGoodFromPlayer(4419)
    RemoveGoodFromPlayer(4421)
    RemoveGoodFromPlayer(4422)
    RemoveGoodFromPlayer(4423)
    RemoveGoodFromPlayer(4424)
    RemoveGoodFromPlayer(4425)
    RemoveGoodFromPlayer(4426)
    RemoveGoodFromPlayer(4427)
    DisableFlagRange((12112600, 12112699))
    EnableFlag(12112610)
    EnableFlag(12112619)
    SkipLinesIfFlagOn(12, 12112629)
    SkipLinesIfFlagOff(11, 12112620)
    RemoveGoodFromPlayer(4419)
    RemoveGoodFromPlayer(4420)
    RemoveGoodFromPlayer(4422)
    RemoveGoodFromPlayer(4423)
    RemoveGoodFromPlayer(4424)
    RemoveGoodFromPlayer(4425)
    RemoveGoodFromPlayer(4426)
    RemoveGoodFromPlayer(4427)
    DisableFlagRange((12112600, 12112699))
    EnableFlag(12112620)
    EnableFlag(12112629)
    SkipLinesIfFlagOn(12, 12112639)
    SkipLinesIfFlagOff(11, 12112630)
    RemoveGoodFromPlayer(4419)
    RemoveGoodFromPlayer(4420)
    RemoveGoodFromPlayer(4421)
    RemoveGoodFromPlayer(4423)
    RemoveGoodFromPlayer(4424)
    RemoveGoodFromPlayer(4425)
    RemoveGoodFromPlayer(4426)
    RemoveGoodFromPlayer(4427)
    DisableFlagRange((12112600, 12112699))
    EnableFlag(12112630)
    EnableFlag(12112639)
    SkipLinesIfFlagOn(12, 12112649)
    SkipLinesIfFlagOff(11, 12112640)
    RemoveGoodFromPlayer(4419)
    RemoveGoodFromPlayer(4420)
    RemoveGoodFromPlayer(4421)
    RemoveGoodFromPlayer(4422)
    RemoveGoodFromPlayer(4424)
    RemoveGoodFromPlayer(4425)
    RemoveGoodFromPlayer(4426)
    RemoveGoodFromPlayer(4427)
    DisableFlagRange((12112600, 12112699))
    EnableFlag(12112640)
    EnableFlag(12112649)
    SkipLinesIfFlagOn(12, 12112659)
    SkipLinesIfFlagOff(11, 12112650)
    RemoveGoodFromPlayer(4419)
    RemoveGoodFromPlayer(4420)
    RemoveGoodFromPlayer(4421)
    RemoveGoodFromPlayer(4422)
    RemoveGoodFromPlayer(4423)
    RemoveGoodFromPlayer(4425)
    RemoveGoodFromPlayer(4426)
    RemoveGoodFromPlayer(4427)
    DisableFlagRange((12112600, 12112699))
    EnableFlag(12112650)
    EnableFlag(12112659)
    SkipLinesIfFlagOn(12, 12112669)
    SkipLinesIfFlagOff(11, 12112660)
    RemoveGoodFromPlayer(4419)
    RemoveGoodFromPlayer(4420)
    RemoveGoodFromPlayer(4421)
    RemoveGoodFromPlayer(4422)
    RemoveGoodFromPlayer(4423)
    RemoveGoodFromPlayer(4424)
    RemoveGoodFromPlayer(4426)
    RemoveGoodFromPlayer(4427)
    DisableFlagRange((12112600, 12112699))
    EnableFlag(12112660)
    EnableFlag(12112669)
    SkipLinesIfFlagOn(12, 12112679)
    SkipLinesIfFlagOff(11, 12112670)
    RemoveGoodFromPlayer(4419)
    RemoveGoodFromPlayer(4420)
    RemoveGoodFromPlayer(4421)
    RemoveGoodFromPlayer(4422)
    RemoveGoodFromPlayer(4423)
    RemoveGoodFromPlayer(4424)
    RemoveGoodFromPlayer(4425)
    RemoveGoodFromPlayer(4427)
    DisableFlagRange((12112600, 12112699))
    EnableFlag(12112670)
    EnableFlag(12112679)
    SkipLinesIfFlagOn(12, 12112689)
    SkipLinesIfFlagOff(11, 12112680)
    RemoveGoodFromPlayer(4419)
    RemoveGoodFromPlayer(4420)
    RemoveGoodFromPlayer(4421)
    RemoveGoodFromPlayer(4422)
    RemoveGoodFromPlayer(4423)
    RemoveGoodFromPlayer(4424)
    RemoveGoodFromPlayer(4425)
    RemoveGoodFromPlayer(4426)
    DisableFlagRange((12112600, 12112699))
    EnableFlag(12112680)
    EnableFlag(12112689)

    # Re-checks every second.
    Wait(1.0)
    return RESTART


def MonitorNormalRunePurchase():
    """ 6696: Monitor whenever player purchases a new normal Caryll Rune, and control flags. """
    if not InsideMap(HUNTERS_DREAM):
        return  # only needs to run in Dream

    SkipLinesIfFlagOn(22, 12112709)
    SkipLinesIfFlagOff(21, 12112700)
    RemoveGoodFromPlayer(4504)
    RemoveGoodFromPlayer(4505)
    RemoveGoodFromPlayer(4506)
    RemoveGoodFromPlayer(4507)
    RemoveGoodFromPlayer(4508)
    RemoveGoodFromPlayer(4513)
    RemoveGoodFromPlayer(4514)
    RemoveGoodFromPlayer(4516)
    RemoveGoodFromPlayer(4517)
    RemoveGoodFromPlayer(4518)
    RemoveGoodFromPlayer(4520)
    RemoveGoodFromPlayer(4521)
    RemoveGoodFromPlayer(4522)
    RemoveGoodFromPlayer(4523)
    RemoveGoodFromPlayer(4524)
    RemoveGoodFromPlayer(4529)
    RemoveGoodFromPlayer(4531)
    RemoveGoodFromPlayer(4540)
    DisableFlagRange((12112700, 12112899))
    EnableFlag(12112700)
    EnableFlag(12112709)
    SkipLinesIfFlagOn(22, 12112719)
    SkipLinesIfFlagOff(21, 12112710)
    RemoveGoodFromPlayer(4503)
    RemoveGoodFromPlayer(4505)
    RemoveGoodFromPlayer(4506)
    RemoveGoodFromPlayer(4507)
    RemoveGoodFromPlayer(4508)
    RemoveGoodFromPlayer(4513)
    RemoveGoodFromPlayer(4514)
    RemoveGoodFromPlayer(4516)
    RemoveGoodFromPlayer(4517)
    RemoveGoodFromPlayer(4518)
    RemoveGoodFromPlayer(4520)
    RemoveGoodFromPlayer(4521)
    RemoveGoodFromPlayer(4522)
    RemoveGoodFromPlayer(4523)
    RemoveGoodFromPlayer(4524)
    RemoveGoodFromPlayer(4529)
    RemoveGoodFromPlayer(4531)
    RemoveGoodFromPlayer(4540)
    DisableFlagRange((12112700, 12112899))
    EnableFlag(12112710)
    EnableFlag(12112719)
    SkipLinesIfFlagOn(22, 12112729)
    SkipLinesIfFlagOff(21, 12112720)
    RemoveGoodFromPlayer(4503)
    RemoveGoodFromPlayer(4504)
    RemoveGoodFromPlayer(4506)
    RemoveGoodFromPlayer(4507)
    RemoveGoodFromPlayer(4508)
    RemoveGoodFromPlayer(4513)
    RemoveGoodFromPlayer(4514)
    RemoveGoodFromPlayer(4516)
    RemoveGoodFromPlayer(4517)
    RemoveGoodFromPlayer(4518)
    RemoveGoodFromPlayer(4520)
    RemoveGoodFromPlayer(4521)
    RemoveGoodFromPlayer(4522)
    RemoveGoodFromPlayer(4523)
    RemoveGoodFromPlayer(4524)
    RemoveGoodFromPlayer(4529)
    RemoveGoodFromPlayer(4531)
    RemoveGoodFromPlayer(4540)
    DisableFlagRange((12112700, 12112899))
    EnableFlag(12112720)
    EnableFlag(12112729)
    SkipLinesIfFlagOn(22, 12112739)
    SkipLinesIfFlagOff(21, 12112730)
    RemoveGoodFromPlayer(4503)
    RemoveGoodFromPlayer(4504)
    RemoveGoodFromPlayer(4505)
    RemoveGoodFromPlayer(4507)
    RemoveGoodFromPlayer(4508)
    RemoveGoodFromPlayer(4513)
    RemoveGoodFromPlayer(4514)
    RemoveGoodFromPlayer(4516)
    RemoveGoodFromPlayer(4517)
    RemoveGoodFromPlayer(4518)
    RemoveGoodFromPlayer(4520)
    RemoveGoodFromPlayer(4521)
    RemoveGoodFromPlayer(4522)
    RemoveGoodFromPlayer(4523)
    RemoveGoodFromPlayer(4524)
    RemoveGoodFromPlayer(4529)
    RemoveGoodFromPlayer(4531)
    RemoveGoodFromPlayer(4540)
    DisableFlagRange((12112700, 12112899))
    EnableFlag(12112730)
    EnableFlag(12112739)
    SkipLinesIfFlagOn(22, 12112749)
    SkipLinesIfFlagOff(21, 12112740)
    RemoveGoodFromPlayer(4503)
    RemoveGoodFromPlayer(4504)
    RemoveGoodFromPlayer(4505)
    RemoveGoodFromPlayer(4506)
    RemoveGoodFromPlayer(4508)
    RemoveGoodFromPlayer(4513)
    RemoveGoodFromPlayer(4514)
    RemoveGoodFromPlayer(4516)
    RemoveGoodFromPlayer(4517)
    RemoveGoodFromPlayer(4518)
    RemoveGoodFromPlayer(4520)
    RemoveGoodFromPlayer(4521)
    RemoveGoodFromPlayer(4522)
    RemoveGoodFromPlayer(4523)
    RemoveGoodFromPlayer(4524)
    RemoveGoodFromPlayer(4529)
    RemoveGoodFromPlayer(4531)
    RemoveGoodFromPlayer(4540)
    DisableFlagRange((12112700, 12112899))
    EnableFlag(12112740)
    EnableFlag(12112749)
    SkipLinesIfFlagOn(22, 12112759)
    SkipLinesIfFlagOff(21, 12112750)
    RemoveGoodFromPlayer(4503)
    RemoveGoodFromPlayer(4504)
    RemoveGoodFromPlayer(4505)
    RemoveGoodFromPlayer(4506)
    RemoveGoodFromPlayer(4507)
    RemoveGoodFromPlayer(4513)
    RemoveGoodFromPlayer(4514)
    RemoveGoodFromPlayer(4516)
    RemoveGoodFromPlayer(4517)
    RemoveGoodFromPlayer(4518)
    RemoveGoodFromPlayer(4520)
    RemoveGoodFromPlayer(4521)
    RemoveGoodFromPlayer(4522)
    RemoveGoodFromPlayer(4523)
    RemoveGoodFromPlayer(4524)
    RemoveGoodFromPlayer(4529)
    RemoveGoodFromPlayer(4531)
    RemoveGoodFromPlayer(4540)
    DisableFlagRange((12112700, 12112899))
    EnableFlag(12112750)
    EnableFlag(12112759)
    SkipLinesIfFlagOn(22, 12112769)
    SkipLinesIfFlagOff(21, 12112760)
    RemoveGoodFromPlayer(4503)
    RemoveGoodFromPlayer(4504)
    RemoveGoodFromPlayer(4505)
    RemoveGoodFromPlayer(4506)
    RemoveGoodFromPlayer(4507)
    RemoveGoodFromPlayer(4508)
    RemoveGoodFromPlayer(4514)
    RemoveGoodFromPlayer(4516)
    RemoveGoodFromPlayer(4517)
    RemoveGoodFromPlayer(4518)
    RemoveGoodFromPlayer(4520)
    RemoveGoodFromPlayer(4521)
    RemoveGoodFromPlayer(4522)
    RemoveGoodFromPlayer(4523)
    RemoveGoodFromPlayer(4524)
    RemoveGoodFromPlayer(4529)
    RemoveGoodFromPlayer(4531)
    RemoveGoodFromPlayer(4540)
    DisableFlagRange((12112700, 12112899))
    EnableFlag(12112760)
    EnableFlag(12112769)
    SkipLinesIfFlagOn(22, 12112779)
    SkipLinesIfFlagOff(21, 12112770)
    RemoveGoodFromPlayer(4503)
    RemoveGoodFromPlayer(4504)
    RemoveGoodFromPlayer(4505)
    RemoveGoodFromPlayer(4506)
    RemoveGoodFromPlayer(4507)
    RemoveGoodFromPlayer(4508)
    RemoveGoodFromPlayer(4513)
    RemoveGoodFromPlayer(4516)
    RemoveGoodFromPlayer(4517)
    RemoveGoodFromPlayer(4518)
    RemoveGoodFromPlayer(4520)
    RemoveGoodFromPlayer(4521)
    RemoveGoodFromPlayer(4522)
    RemoveGoodFromPlayer(4523)
    RemoveGoodFromPlayer(4524)
    RemoveGoodFromPlayer(4529)
    RemoveGoodFromPlayer(4531)
    RemoveGoodFromPlayer(4540)
    DisableFlagRange((12112700, 12112899))
    EnableFlag(12112770)
    EnableFlag(12112779)
    SkipLinesIfFlagOn(22, 12112789)
    SkipLinesIfFlagOff(21, 12112780)
    RemoveGoodFromPlayer(4503)
    RemoveGoodFromPlayer(4504)
    RemoveGoodFromPlayer(4505)
    RemoveGoodFromPlayer(4506)
    RemoveGoodFromPlayer(4507)
    RemoveGoodFromPlayer(4508)
    RemoveGoodFromPlayer(4513)
    RemoveGoodFromPlayer(4514)
    RemoveGoodFromPlayer(4517)
    RemoveGoodFromPlayer(4518)
    RemoveGoodFromPlayer(4520)
    RemoveGoodFromPlayer(4521)
    RemoveGoodFromPlayer(4522)
    RemoveGoodFromPlayer(4523)
    RemoveGoodFromPlayer(4524)
    RemoveGoodFromPlayer(4529)
    RemoveGoodFromPlayer(4531)
    RemoveGoodFromPlayer(4540)
    DisableFlagRange((12112700, 12112899))
    EnableFlag(12112780)
    EnableFlag(12112789)
    SkipLinesIfFlagOn(22, 12112799)
    SkipLinesIfFlagOff(21, 12112790)
    RemoveGoodFromPlayer(4503)
    RemoveGoodFromPlayer(4504)
    RemoveGoodFromPlayer(4505)
    RemoveGoodFromPlayer(4506)
    RemoveGoodFromPlayer(4507)
    RemoveGoodFromPlayer(4508)
    RemoveGoodFromPlayer(4513)
    RemoveGoodFromPlayer(4514)
    RemoveGoodFromPlayer(4516)
    RemoveGoodFromPlayer(4518)
    RemoveGoodFromPlayer(4520)
    RemoveGoodFromPlayer(4521)
    RemoveGoodFromPlayer(4522)
    RemoveGoodFromPlayer(4523)
    RemoveGoodFromPlayer(4524)
    RemoveGoodFromPlayer(4529)
    RemoveGoodFromPlayer(4531)
    RemoveGoodFromPlayer(4540)
    DisableFlagRange((12112700, 12112899))
    EnableFlag(12112790)
    EnableFlag(12112799)
    SkipLinesIfFlagOn(22, 12112809)
    SkipLinesIfFlagOff(21, 12112800)
    RemoveGoodFromPlayer(4503)
    RemoveGoodFromPlayer(4504)
    RemoveGoodFromPlayer(4505)
    RemoveGoodFromPlayer(4506)
    RemoveGoodFromPlayer(4507)
    RemoveGoodFromPlayer(4508)
    RemoveGoodFromPlayer(4513)
    RemoveGoodFromPlayer(4514)
    RemoveGoodFromPlayer(4516)
    RemoveGoodFromPlayer(4517)
    RemoveGoodFromPlayer(4520)
    RemoveGoodFromPlayer(4521)
    RemoveGoodFromPlayer(4522)
    RemoveGoodFromPlayer(4523)
    RemoveGoodFromPlayer(4524)
    RemoveGoodFromPlayer(4529)
    RemoveGoodFromPlayer(4531)
    RemoveGoodFromPlayer(4540)
    DisableFlagRange((12112700, 12112899))
    EnableFlag(12112800)
    EnableFlag(12112809)
    SkipLinesIfFlagOn(22, 12112819)
    SkipLinesIfFlagOff(21, 12112810)
    RemoveGoodFromPlayer(4503)
    RemoveGoodFromPlayer(4504)
    RemoveGoodFromPlayer(4505)
    RemoveGoodFromPlayer(4506)
    RemoveGoodFromPlayer(4507)
    RemoveGoodFromPlayer(4508)
    RemoveGoodFromPlayer(4513)
    RemoveGoodFromPlayer(4514)
    RemoveGoodFromPlayer(4516)
    RemoveGoodFromPlayer(4517)
    RemoveGoodFromPlayer(4518)
    RemoveGoodFromPlayer(4521)
    RemoveGoodFromPlayer(4522)
    RemoveGoodFromPlayer(4523)
    RemoveGoodFromPlayer(4524)
    RemoveGoodFromPlayer(4529)
    RemoveGoodFromPlayer(4531)
    RemoveGoodFromPlayer(4540)
    DisableFlagRange((12112700, 12112899))
    EnableFlag(12112810)
    EnableFlag(12112819)
    SkipLinesIfFlagOn(22, 12112829)
    SkipLinesIfFlagOff(21, 12112820)
    RemoveGoodFromPlayer(4503)
    RemoveGoodFromPlayer(4504)
    RemoveGoodFromPlayer(4505)
    RemoveGoodFromPlayer(4506)
    RemoveGoodFromPlayer(4507)
    RemoveGoodFromPlayer(4508)
    RemoveGoodFromPlayer(4513)
    RemoveGoodFromPlayer(4514)
    RemoveGoodFromPlayer(4516)
    RemoveGoodFromPlayer(4517)
    RemoveGoodFromPlayer(4518)
    RemoveGoodFromPlayer(4520)
    RemoveGoodFromPlayer(4522)
    RemoveGoodFromPlayer(4523)
    RemoveGoodFromPlayer(4524)
    RemoveGoodFromPlayer(4529)
    RemoveGoodFromPlayer(4531)
    RemoveGoodFromPlayer(4540)
    DisableFlagRange((12112700, 12112899))
    EnableFlag(12112820)
    EnableFlag(12112829)
    SkipLinesIfFlagOn(22, 12112839)
    SkipLinesIfFlagOff(21, 12112830)
    RemoveGoodFromPlayer(4503)
    RemoveGoodFromPlayer(4504)
    RemoveGoodFromPlayer(4505)
    RemoveGoodFromPlayer(4506)
    RemoveGoodFromPlayer(4507)
    RemoveGoodFromPlayer(4508)
    RemoveGoodFromPlayer(4513)
    RemoveGoodFromPlayer(4514)
    RemoveGoodFromPlayer(4516)
    RemoveGoodFromPlayer(4517)
    RemoveGoodFromPlayer(4518)
    RemoveGoodFromPlayer(4520)
    RemoveGoodFromPlayer(4521)
    RemoveGoodFromPlayer(4523)
    RemoveGoodFromPlayer(4524)
    RemoveGoodFromPlayer(4529)
    RemoveGoodFromPlayer(4531)
    RemoveGoodFromPlayer(4540)
    DisableFlagRange((12112700, 12112899))
    EnableFlag(12112830)
    EnableFlag(12112839)
    SkipLinesIfFlagOn(22, 12112849)
    SkipLinesIfFlagOff(21, 12112840)
    RemoveGoodFromPlayer(4503)
    RemoveGoodFromPlayer(4504)
    RemoveGoodFromPlayer(4505)
    RemoveGoodFromPlayer(4506)
    RemoveGoodFromPlayer(4507)
    RemoveGoodFromPlayer(4508)
    RemoveGoodFromPlayer(4513)
    RemoveGoodFromPlayer(4514)
    RemoveGoodFromPlayer(4516)
    RemoveGoodFromPlayer(4517)
    RemoveGoodFromPlayer(4518)
    RemoveGoodFromPlayer(4520)
    RemoveGoodFromPlayer(4521)
    RemoveGoodFromPlayer(4522)
    RemoveGoodFromPlayer(4524)
    RemoveGoodFromPlayer(4529)
    RemoveGoodFromPlayer(4531)
    RemoveGoodFromPlayer(4540)
    DisableFlagRange((12112700, 12112899))
    EnableFlag(12112840)
    EnableFlag(12112849)
    SkipLinesIfFlagOn(22, 12112859)
    SkipLinesIfFlagOff(21, 12112850)
    RemoveGoodFromPlayer(4503)
    RemoveGoodFromPlayer(4504)
    RemoveGoodFromPlayer(4505)
    RemoveGoodFromPlayer(4506)
    RemoveGoodFromPlayer(4507)
    RemoveGoodFromPlayer(4508)
    RemoveGoodFromPlayer(4513)
    RemoveGoodFromPlayer(4514)
    RemoveGoodFromPlayer(4516)
    RemoveGoodFromPlayer(4517)
    RemoveGoodFromPlayer(4518)
    RemoveGoodFromPlayer(4520)
    RemoveGoodFromPlayer(4521)
    RemoveGoodFromPlayer(4522)
    RemoveGoodFromPlayer(4523)
    RemoveGoodFromPlayer(4529)
    RemoveGoodFromPlayer(4531)
    RemoveGoodFromPlayer(4540)
    DisableFlagRange((12112700, 12112899))
    EnableFlag(12112850)
    EnableFlag(12112859)
    SkipLinesIfFlagOn(22, 12112869)
    SkipLinesIfFlagOff(21, 12112860)
    RemoveGoodFromPlayer(4503)
    RemoveGoodFromPlayer(4504)
    RemoveGoodFromPlayer(4505)
    RemoveGoodFromPlayer(4506)
    RemoveGoodFromPlayer(4507)
    RemoveGoodFromPlayer(4508)
    RemoveGoodFromPlayer(4513)
    RemoveGoodFromPlayer(4514)
    RemoveGoodFromPlayer(4516)
    RemoveGoodFromPlayer(4517)
    RemoveGoodFromPlayer(4518)
    RemoveGoodFromPlayer(4520)
    RemoveGoodFromPlayer(4521)
    RemoveGoodFromPlayer(4522)
    RemoveGoodFromPlayer(4523)
    RemoveGoodFromPlayer(4524)
    RemoveGoodFromPlayer(4531)
    RemoveGoodFromPlayer(4540)
    DisableFlagRange((12112700, 12112899))
    EnableFlag(12112860)
    EnableFlag(12112869)
    SkipLinesIfFlagOn(22, 12112879)
    SkipLinesIfFlagOff(21, 12112870)
    RemoveGoodFromPlayer(4503)
    RemoveGoodFromPlayer(4504)
    RemoveGoodFromPlayer(4505)
    RemoveGoodFromPlayer(4506)
    RemoveGoodFromPlayer(4507)
    RemoveGoodFromPlayer(4508)
    RemoveGoodFromPlayer(4513)
    RemoveGoodFromPlayer(4514)
    RemoveGoodFromPlayer(4516)
    RemoveGoodFromPlayer(4517)
    RemoveGoodFromPlayer(4518)
    RemoveGoodFromPlayer(4520)
    RemoveGoodFromPlayer(4521)
    RemoveGoodFromPlayer(4522)
    RemoveGoodFromPlayer(4523)
    RemoveGoodFromPlayer(4524)
    RemoveGoodFromPlayer(4529)
    RemoveGoodFromPlayer(4540)
    DisableFlagRange((12112700, 12112899))
    EnableFlag(12112870)
    EnableFlag(12112879)
    SkipLinesIfFlagOn(22, 12112889)
    SkipLinesIfFlagOff(21, 12112880)
    RemoveGoodFromPlayer(4503)
    RemoveGoodFromPlayer(4504)
    RemoveGoodFromPlayer(4505)
    RemoveGoodFromPlayer(4506)
    RemoveGoodFromPlayer(4507)
    RemoveGoodFromPlayer(4508)
    RemoveGoodFromPlayer(4513)
    RemoveGoodFromPlayer(4514)
    RemoveGoodFromPlayer(4516)
    RemoveGoodFromPlayer(4517)
    RemoveGoodFromPlayer(4518)
    RemoveGoodFromPlayer(4520)
    RemoveGoodFromPlayer(4521)
    RemoveGoodFromPlayer(4522)
    RemoveGoodFromPlayer(4523)
    RemoveGoodFromPlayer(4524)
    RemoveGoodFromPlayer(4529)
    RemoveGoodFromPlayer(4531)
    DisableFlagRange((12112700, 12112899))
    EnableFlag(12112880)
    EnableFlag(12112889)

    # Re-checks every second.
    Wait(1.0)
    return RESTART


def MonitorCovenantRunePurchase():
    """ 6697: Monitor whenever player purchases a new Covenant Rune, and control flags. """
    if not InsideMap(HUNTERS_DREAM):
        return  # only needs to run in Dream

    SkipLinesIfFlagOn(8, 12112909)  # rune must not already be "active"
    SkipLinesIfFlagOff(7, 12112900)  # rune must be purchased
    RemoveGoodFromPlayer(4610)
    RemoveGoodFromPlayer(4620)
    RemoveGoodFromPlayer(4640)
    RemoveGoodFromPlayer(4650)
    DisableFlagRange((12112900, 12112999))  # all runes purchaseable and inactive...
    EnableFlag(12112900)  # ...except this rune is not purchaseable...
    EnableFlag(12112909)  # ...and this rune is "active" for effect

    SkipLinesIfFlagOn(8, 12112919)  # rune must not already be "active"
    SkipLinesIfFlagOff(7, 12112910)  # rune must be purchased
    RemoveGoodFromPlayer(4600)
    RemoveGoodFromPlayer(4620)
    RemoveGoodFromPlayer(4640)
    RemoveGoodFromPlayer(4650)
    DisableFlagRange((12112900, 12112999))  # all runes purchaseable and inactive...
    EnableFlag(12112910)  # ...except this rune is not purchaseable...
    EnableFlag(12112919)  # ...and this rune is "active" for effect

    SkipLinesIfFlagOn(8, 12112929)  # rune must not already be "active"
    SkipLinesIfFlagOff(7, 12112920)  # rune must be purchased
    RemoveGoodFromPlayer(4600)
    RemoveGoodFromPlayer(4610)
    RemoveGoodFromPlayer(4640)
    RemoveGoodFromPlayer(4650)
    DisableFlagRange((12112900, 12112999))  # all runes purchaseable and inactive...
    EnableFlag(12112920)  # ...except this rune is not purchaseable...
    EnableFlag(12112929)  # ...and this rune is "active" for effect

    SkipLinesIfFlagOn(8, 12112939)  # rune must not already be "active"
    SkipLinesIfFlagOff(7, 12112930)  # rune must be purchased
    RemoveGoodFromPlayer(4600)
    RemoveGoodFromPlayer(4610)
    RemoveGoodFromPlayer(4620)
    RemoveGoodFromPlayer(4650)
    DisableFlagRange((12112900, 12112999))  # all runes purchaseable and inactive...
    EnableFlag(12112930)  # ...except this rune is not purchaseable...
    EnableFlag(12112939)  # ...and this rune is "active" for effect

    SkipLinesIfFlagOn(8, 12112949)  # rune must not already be "active"
    SkipLinesIfFlagOff(7, 12112940)  # rune must be purchased
    RemoveGoodFromPlayer(4600)
    RemoveGoodFromPlayer(4610)
    RemoveGoodFromPlayer(4620)
    RemoveGoodFromPlayer(4640)
    DisableFlagRange((12112900, 12112999))  # all runes purchaseable and inactive...
    EnableFlag(12112940)  # ...except this rune is not purchaseable...
    EnableFlag(12112949)  # ...and this rune is "active" for effect

    # Re-checks every second.
    Wait(1.0)
    return RESTART
