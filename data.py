from enum import Enum
class sheetConfig(Enum):
    MAIN_SHEET = 1
    COMBAT_SHEET = 2
    INVENTORY_SHEET = 3

    CHAR_NAME = "D3"
    BACKGROUND = "D9"
    SPECIES = "D13"
    CLASS = "V9"
    SUBCLASS = "V13"

    CURRENT_HP = "BG6"
    MAX_HP = "BP12"
    TEMP_HP = "BP6"
    LEVEL = "AO4"

    STR_MOD = "D39"
    DEX_MOD = "D60"
    CON_MOD = "D85"
    INT_MOD = "V28"
    WIS_MOD = "V57"
    CHA_MOD = "V86"

    STR_SCORE = "M40"
    DEX_SCORE = "M61"
    CON_SCORE = "M86"
    INT_SCORE = "AE29"
    WIS_SCORE = "AE58"
    CHA_SCORE = "AE87"

    WEAPONS = "AN39:BX59"

    PROFICIENT = "●"
    PROFICIENCY_BONUS = "D27"
    
    STR_SKILLS = "D53:J53"
    DEX_SKILLS = "D74:J78"
    INT_SKILLS = "V42:AJ5"
    WIS_SKILLS = "V71:AJ80"
    CHA_SKILLS = "V100:AJ107"

    INV_ONE = "C5:AD65"
    INV_TWO = "AG5:BH65"
    INV_THREE = "BK5:CL65"

    SPELLS = "D24:AX132"

config = sheetConfig