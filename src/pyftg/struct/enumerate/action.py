from enum import Enum

class Action(Enum):
    NEUTRAL = 0
    STAND = 1
    FORWARD_WALK = 2
    DASH = 3
    BACK_STEP = 4
    CROUCH = 5
    JUMP = 6
    FOR_JUMP = 7
    BACK_JUMP = 8
    AIR = 9
    STAND_GUARD = 10
    CROUCH_GUARD = 11
    AIR_GUARD = 12
    STAND_GUARD_RECOV = 13
    CROUCH_GUARD_RECOV = 14
    AIR_GUARD_RECOV = 15
    STAND_RECOV = 16
    CROUCH_RECOV = 17
    AIR_RECOV = 18
    CHANGE_DOWN = 19
    DOWN = 20
    RISE = 21
    LANDING = 22
    THROW_A = 23
    THROW_B = 24
    THROW_HIT = 25
    THROW_SUFFER = 26
    STAND_A = 27
    STAND_B = 28
    CROUCH_A = 29
    CROUCH_B = 30
    AIR_A = 31
    AIR_B = 32
    AIR_DA = 33
    AIR_DB = 34
    STAND_FA = 35
    STAND_FB = 36
    CROUCH_FA = 37
    CROUCH_FB = 38
    AIR_FA = 39
    AIR_FB = 40
    AIR_UA = 41
    AIR_UB = 42
    STAND_D_DF_FA = 43
    STAND_D_DF_FB = 44
    STAND_F_D_DFA = 45
    STAND_F_D_DFB = 46
    STAND_D_DB_BA = 47
    STAND_D_DB_BB = 48
    AIR_D_DF_FA = 49
    AIR_D_DF_FB = 50
    AIR_F_D_DFA = 51
    AIR_F_D_DFB = 52
    AIR_D_DB_BA = 53
    AIR_D_DB_BB = 54
    STAND_D_DF_FC = 55

    def __str__(self):
        return self.name