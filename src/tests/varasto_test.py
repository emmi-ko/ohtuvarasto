import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.testivarasto = Varasto(-1, -2)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)


    def test_tilavuus_virhe(self):
        self.assertEqual(self.testivarasto.tilavuus, 0.0)

    def test_saldo_tilavuus_sama(self):
        self.valivarasto = Varasto(2,3)
        self.assertEqual(self.valivarasto.tilavuus, self.valivarasto.saldo)

    def test_saldo_virhe(self):
        self.assertEqual(self.testivarasto.saldo, self.testivarasto.tilavuus)

    def test_varasto_lisays_liikaa(self):
        self.testivarasto.lisaa_varastoon(2)
        saatu_maara = self.testivarasto.saldo
        self.assertEqual(saatu_maara, 0)

    def test_varasto_lisays_virhe(self):
        self.assertEqual(self.testivarasto.lisaa_varastoon(-1), -1)

    def test_varastosta_otto_virhe(self):
        self.assertEqual(self.testivarasto.ota_varastosta(-1), 0.0)

    def test_varastosta_otto(self):
        self.varasto.lisaa_varastoon(2)
        self.assertEqual(self.varasto.ota_varastosta(2), 2)

    def test_varastotas_otto_kaikki(self):
        self.varasto.lisaa_varastoon(2)
        self.assertEqual(self.varasto.ota_varastosta(3), 2)
    
    def test_str(self):
        self.assertEqual(self.varasto.__str__(), "saldo = 0, vielä tilaa 10")

    



