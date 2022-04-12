class PC():

    def __init__(self, HP, DEX, CON, INT, WIS, CHA, PROF, AC, LVL) -> None:
        self.hp = HP
        self.dex = DEX
        self.con = CON
        self.int = INT
        self.wis = WIS
        self.cha = CHA
        self.prof = PROF
        self.ac = AC
        self.lvl = LVL

    def atacar():
        pass

    def saving_throw():
        pass

class Rogue(PC):
    
    def __init__(self, HP, DEX, CON, INT, WIS, CHA, PROF, AC, LVL) -> None:
        super().__init__(HP, DEX, CON, INT, WIS, CHA, PROF, AC, LVL)

    def sneak_attack():
        pass

class Wizard(PC):

    def __init__(self, HP, DEX, CON, INT, WIS, CHA, PROF, AC, LVL) -> None:
        super().__init__(HP, DEX, CON, INT, WIS, CHA, PROF, AC, LVL)
        if self.lvl == 2:
            pass

class Ranger(PC):

    def __init__(self, HP, DEX, CON, INT, WIS, CHA, PROF, AC, LVL) -> None:
        super().__init__(HP, DEX, CON, INT, WIS, CHA, PROF, AC, LVL)

