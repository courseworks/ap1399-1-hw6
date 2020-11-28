import unittest
from aphw6 import read_data
from league import Team, Match, Weeks, League


class Test(unittest.TestCase):
    def test1_Match(self):
        x = Match('  A.C.Milan    3    -   1         Inter    ')
        r11 = (x.data()[0] == (1, 1, 0, 0, 3, 1, 2, 3))
        r12 = (x.data()[1] == (1, 0, 0, 1, 1, 3, -2, 0))
        self.assertEqual(r11 & r12, True)
    
    def test2_Weeks(self):
        m21 = Match('   Esteghlal    3   - 1      Zobahan  ')
        m22 = Match(' Golgohar    0   -      1      Perspolis  ')
        m23 = Match('    Nassaji   4 - 2   Peykan     ')
        m24 = Match('    Zobahan   3 - 0   Foolad     ')
        w21 = Weeks(10, [])
        w21.add_match(m21)
        w21.add_match(m22)
        w21.add_match(m23)
        w21.add_match(m24)
        self.assertEqual(len(w21.matches), 3)
        self.assertEqual(w21.matches[0].away, 'Zobahan')

    def test3_Weeks(self):
        m31 = Match('   Esteghlal    3   - 1      Zobahan  ')
        m32 = Match(' Golgohar    0   -      1      Perspolis  ')
        m33 = Match('    Nassaji   4 - 2   Peykan     ')
        w31 = Weeks(5)
        w31.add_match(m31)
        w31.add_match(m32)
        w31.add_match(m33)
        print(w31.matches)       #show the result in beautiful manner

    def test4_Team(self):
        m41 = Match('Liverpool    1   - 1          ManUtd  ')
        m42 = Match('        Arsenal    0   - 1          ManCity')
        t41 = Team('Liverpool')
        t42 = Team('ManUtd')
        self.assertEqual(t42.rank, 2)
        t41.add_match(m41)
        t41.add_match(m42)
        r = (t41.mp, t41.gf, t41.gd, t41.pts)
        self.assertEqual(r , (1,1,0,1))

    def test5_League(self):
        t51 = Team('Sevilla')
        t52 = Team('Valencia')
        t53 = Team('Barcelona')
        t54 = Team('Cadiz')
        m51 = Match('   Sevilla    3   - 1         Valencia  ')
        m52 = Match(' Barcelona    0   - 1          Cadiz  ')
        m53 = Match('Valencia    0   -    2      Barcelona  ')
        m54 = Match('   Cadiz 4 -    3 Sevilla')
        w51 = Weeks(1)
        w51.add_match(m51)
        w51.add_match(m52)
        w52 = Weeks(2)
        w52.add_match(m53)
        w52.add_match(m54)
        l5 = League([t52,t53,t51,t54], 1395)
        l5.add_week(w51)
        l5.add_week(w52)
        self.assertEqual(l5.all_standing[1][3].gd, -2)
        self.assertEqual(l5.all_standing[2][2].pts, 3)

    def test6_File(self):
        l = read_data('data.txt', 1399)
        s = (l.standing[0].name, l.standing[1].name, l.standing[2].name, l.standing[3].name)
        self.assertEqual(s, ("Nassaji", "Peykan", "Foolad", "Padide"))
        self.assertEqual(l.all_weeks[0].matches[0].home, "Foolad")

if __name__=='__main__':
    unittest.main()