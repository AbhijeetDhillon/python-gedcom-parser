import unittest

from mainUserStoryFile import US02, US05, us03_birth_b4_death, us04_marr_b4_divorce, userstory1, userstory8, us06_div_b4_death, us07_age_lessthan_150, userstory09, userstory10, US15, US18, us16_male_last_name, us23_sameName_sameBirthDate, US22, US25, userstory35, userstory36, us24_uniqueFamily_bySpouses, us28_sibilings_byAge, userstory38, userstory39
from parserLogic import file_reading_gen


class TestContainer(unittest.TestCase):

    #-------------------Aishwarya's Test Case Section Start--------------------#

    def test_US02(self):
        # all values of birthdays and death days given
        si1 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf1 = {'@F1@': {'Married': '1990-06-15', 'Divorced': '1998-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        # birthdays missing
        si2 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': 'NA', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf2 = {'@F1@': {'Married': '1990-06-15', 'Divorced': '1998-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        # marriage dates missing
        si4 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf4 = {'@F1@': {'Married': 'NA', 'Divorced': '1998-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        # marriage before birthday
        si5 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf5 = {'@F1@': {'Married': '1950-01-01', 'Divorced': '1998-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        for i in range(1):
            print("\n\n All values of birthdays and death days given\n")
            # all values of birthdays and death days given
            self.assertEqual(US02(si1, sf1), "True")

            print("\n\n Birthdays missing\n")
            # birthdays missing
            self.assertEqual(US02(si2, sf2), "True")

            print("\n\n Marriage dates missing\n")
            # marriage dates missing
            self.assertEqual(US02(si4, sf4), "True")

            print("\n\n Marriage before birth\n")
            # marriage before birthday
            self.assertEqual(US02(si5, sf5), "True")

    def test_US05(self):

        # all values of birthdays and death days given
        si1 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf1 = {'@F1@': {'Married': '1990-06-15', 'Divorced': '1998-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        # deathdates missing
        si3 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf3 = {'@F1@': {'Married': '1990-06-15', 'Divorced': '1998-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        # marriage dates missing
        si4 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf4 = {'@F1@': {'Married': 'NA', 'Divorced': '1998-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        # death before marriage
        si6 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '1980-08-15', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf6 = {'@F1@': {'Married': '1990-06-15', 'Divorced': '1998-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        for i in range(1):
            print("\n\n All values of birthdays and death days given\n")
            # all values of birthdays and death days given
            self.assertEqual(US05(si1, sf1), "True")

            print("\n\n Deathdates missing\n")
            # deathdates missing
            self.assertEqual(US05(si3, sf3), "True")

            print("\n\n Marriage dates missing\n")
            # marriage dates missing
            self.assertEqual(US05(si4, sf4), "True")

            print("\n\n Death before marriage\n")
            # death before marriage
            self.assertEqual(US05(si6, sf6), "True")

    def test_US15(self):
        # no children
        si1 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf1 = {'@F1@': {'Married': '1990-06-15', 'Divorced': '1998-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {}}}

        # greater than 15 children
        si2 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf2 = {'@F1@': {'Married': '1990-06-15', 'Divorced': '1998-06-15', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I8@',
                                                                                                                                                                                                2: '@I9@', 3: '@I10@', 4: '@I11@', 5: '@I12@', 6: '@I13@', 7: '@I14@', 8: '@I15@', 9: '@I16@', 10: '@I17@', 11: '@I7@', 12: '@I18@', 13: '@I19@', 14: '@I20@', 15: '@I21@', 16: '@I22@'}}}

        for i in range(1):
            print("\n\n No children \n")
            # no children
            self.assertEqual(US15(si1, sf1), "True")

            print("\n\n Greater than 15 children\n")
            # greater than 15 children
            self.assertEqual(US15(si2, sf2), "True")

    def test_US18(self):
        # no children
        si1 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf1 = {'@F1@': {'Married': '1990-06-15', 'Divorced': '1998-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {}}}

        # siblings are married
        si2 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf2 = {'@F1@': {'Married': '1990-06-15', 'Divorced': '1998-06-15', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/',
                        'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I1@', 2: '@I2@', }}}

        for i in range(1):
            print("\n\n No children \n")
            # no children
            self.assertEqual(US18(si1, sf1), "True")

            print("\n\n siblings are married\n")
            # greater than 15 children
            self.assertEqual(US18(si2, sf2), "True")

    def test_US22(self):

        si1 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I1@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf1 = {'@F1@': {'Married': '1990-06-15', 'Divorced': '1998-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        for i in range(1):
            print("\n\n Unique individual and family id \n")
            # unique id
            self.assertEqual(US22(si1, sf1), "True")

    def test_US25(self):

        si1 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '2000-08-01', 'FAMS': {}, 'FAMC': {}},
               '@I2@': {'Name': 'Smit /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {}, 'FAMC': {}}}
        sf1 = {'@F1@': {'Married': '1990-06-15', 'Divorced': '1998-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Smit /Nawar/', 'Children': {}}}

        for i in range(1):
            print("\n\n Unique first names in family \n")
            # unique id
            self.assertEqual(US25(si1, sf1), "True")

    #-------------------Aishwarya's Tetst Case Section End--------------------#

    #-------------------Abhijeet's Tetst Case Section Start--------------------#

    def test_us03_birth_b4_death(self):
        # all values of birthdays and death days given
        si1 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}

        # death before birth
        si5 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '2000-01-01', 'Death': '1996-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '2000-08-04', 'Death': '1978-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}

        print(
            "\n\n All values of birthdays and death days given(test_us03_birth_b4_death)\n")
        # all values of birthdays and death days given
        self.assertEqual(us03_birth_b4_death(si1), "False")

        print("\n\n Deaths before birth(test_us03_birth_b4_death)")
        # birth before birthday
        self.assertEqual(us03_birth_b4_death(si5), "True")

    def test_us04_marr_b4_divorce(self):
        # all values of birthdays and death days given
        sf1 = {'@F1@': {'Married': '1990-06-15', 'Divorced': '1998-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        # birthdays missing
        sf2 = {'@F1@': {'Married': '1990-06-15', 'Divorced': 'NA', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        # death dates missing
        sf4 = {'@F1@': {'Married': 'NA', 'Divorced': '1998-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        # death before birth
        sf5 = {'@F1@': {'Married': '1983-01-01', 'Divorced': '1950-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        print(
            "\n\n All values of divorce and death dates given(test_us04_marr_b4_divorce)\n")
        # all values of birthdays and death days given
        self.assertEqual(us04_marr_b4_divorce(sf1), "False")

        print("\n\n Divorce before Marriage(test_us04_marr_b4_divorce)")
        # birth before birthday
        self.assertEqual(us04_marr_b4_divorce(sf5), "True")

    def test_us06_div_b4_death(self):

        si1 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1900-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf1 = {'@F1@': {'Married': '1990-06-15', 'Divorced': '2300-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        si2 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1900-01-01', 'Death': '2002-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf2 = {'@F1@': {'Married': '1990-06-15', 'Divorced': '2001-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        si3 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1900-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2004-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf3 = {'@F1@': {'Married': '1990-06-15', 'Divorced': '2001-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        si4 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1900-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf4 = {'@F1@': {'Married': '1990-06-15', 'Divorced': '1900-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        self.assertEqual(us06_div_b4_death(si1, sf1), "True")
        self.assertEqual(us06_div_b4_death(si2, sf2), "True")
        self.assertEqual(us06_div_b4_death(si3, sf3), "True")
        self.assertEqual(us06_div_b4_death(si4, sf4), "False")

    def test_us07_age_lessthan_150(self):

        si1 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1800-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        si2 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}

        self.assertEqual(us07_age_lessthan_150(si1), "True")
        self.assertEqual(us07_age_lessthan_150(si2), "False")

    def test_us16_male_last_name(self):

        si1 = {'@I4@': {'Name': 'Jack /Panchal/', 'Gender': 'M', 'Birthday': '1900-01-01',
                        'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I5@'}}}
        sf1 = {'@F1@': {'Married': '1990-06-15', 'Divorced': '2300-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        si2 = {'@I4@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1900-01-01',
                        'Death': '2002-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I5@'}}}
        sf2 = {'@F1@': {'Married': '1990-06-15', 'Divorced': '2001-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Pappu /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        self.assertEqual(us16_male_last_name(si1, sf1), "True")
        self.assertEqual(us16_male_last_name(si2, sf2), "False")

    def test_us23_sameName_sameBirthDate(self):

        si1 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1800-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Smit /Nawar/', 'Gender': 'F', 'Birthday': '1800-01-01', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        si2 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}

        self.assertEqual(us23_sameName_sameBirthDate(si1), "True")
        self.assertEqual(us23_sameName_sameBirthDate(si2), "False")

    def test_us24_uniqueFamily_bySpouses(self):

        sf1 = {'@F1@': {'Married': '1990-06-15', 'Divorced': '2001-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Pappu /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}},
               '@F2@': {'Married': '1990-06-15', 'Divorced': '2009-06-15', 'Husband Id': '@I8@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Hi Xie /Nawar/', 'Children': {1: '@I8@'}}}

        sf2 = {'@F1@': {'Married': '1990-06-15', 'Divorced': '2001-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Pappu /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}},
               '@F2@': {'Married': '1990-06-15', 'Divorced': '2009-06-15', 'Husband Id': '@I8@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I8@'}}}

        self.assertEqual(us24_uniqueFamily_bySpouses(sf1), "False")
        self.assertEqual(us24_uniqueFamily_bySpouses(sf2), "True")

    def test_us28_sibilings_byAge(self):

        si1 = {'@I4@': {'Name': 'Smitesh /Nawar/', 'Gender': 'M', 'Birthday': '1900-01-01', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I5@': {'Name': 'Yi Xieyesh /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I6@': {'Name': 'Yiyesh /Nawar/', 'Gender': 'M', 'Birthday': '1970-08-04', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I7@': {'Name': 'YiXie /Nawar/', 'Gender': 'F', 'Birthday': '1975-08-04', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf1 = {'@F1@': {'Married': '1990-06-15', 'Divorced': '2300-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@', 2: '@I5@', 3: '@I6@', 4: '@I7@'}}}

        self.assertEquals(us28_sibilings_byAge(si1, sf1), "Ordered")

    #-------------------Abhijeet's Tetst Case Section End--------------------#

    #-------------------Dinessh's Tetst Case Section Start--------------------#

    def test_userstory1(self):

        # all dates are before today's date
        si1 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1900-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf1 = {'@F1@': {'Married': '1990-06-15', 'Divorced': '1998-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        # all dates are future dates
        si3 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '2030-01-01', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}},
               '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '2045-08-04', 'Death': '2070-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf3 = {'@F1@': {'Married': '2021-06-15', 'Divorced': '2055-06-15', 'Husband Id': '@I1@',
                        'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        print("\n\n Dates are Before today's date")
        self.assertEqual(userstory1(si1, sf1), "FALSE")
        print("\n\n Future Dates")
        self.assertEqual(userstory1(si3, sf3), "TRUE")

    def test_userstory8(self):

        # all birthdates are after marriage date of their parents
        si1 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': 'NA', 'FAMS': {1: '@F1@', 2: '@F2@'}, 'FAMC': 'NA'}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F2@'},
                                                                                                                                                                'FAMC': 'NA'}, '@I3@': {'Name': 'Payal /Nawar/', 'Gender': 'F', 'Birthday': '1975-04-03', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': 'NA'}, '@I4@': {'Name': 'Rani /Nawar/', 'Gender': 'F', 'Birthday': '1994-11-10', 'Death': 'NA', 'FAMS': {1: '@F3@'}, 'FAMC': '@F1@'}}
        sf1 = {'@F1@': {'Married': '2000-06-15', 'Divorced': 'NA', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/',
                        'Wife Id': '@I3@', 'Wife Name': 'Payal /Nawar/', 'Children': {1: '@I4@', 2: '@I5@'}}}

        # all birthdates are before marriage date of their parents
        si2 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': 'NA', 'FAMS': {1: '@F1@', 2: '@F2@'}, 'FAMC': 'NA'}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F2@'},
                                                                                                                                                                'FAMC': 'NA'}, '@I3@': {'Name': 'Payal /Nawar/', 'Gender': 'F', 'Birthday': '1975-04-03', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': 'NA'}, '@I4@': {'Name': 'Rani /Nawar/', 'Gender': 'F', 'Birthday': '1994-11-10', 'Death': 'NA', 'FAMS': {1: '@F3@'}, 'FAMC': '@F1@'}}
        sf2 = {'@F1@': {'Married': '1960-06-15', 'Divorced': 'NA', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/',
                        'Wife Id': '@I3@', 'Wife Name': 'Payal /Nawar/', 'Children': {1: '@I4@', 2: '@I5@'}}}

        # all marriage date are NA
        si3 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': 'NA', 'FAMS': {1: '@F1@', 2: '@F2@'}, 'FAMC': 'NA'}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F2@'},
                                                                                                                                                                'FAMC': 'NA'}, '@I3@': {'Name': 'Payal /Nawar/', 'Gender': 'F', 'Birthday': '1975-04-03', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': 'NA'}, '@I4@': {'Name': 'Rani /Nawar/', 'Gender': 'F', 'Birthday': '1994-11-10', 'Death': 'NA', 'FAMS': {1: '@F3@'}, 'FAMC': '@F1@'}}
        sf3 = {'@F1@': {'Married': 'NA', 'Divorced': 'NA', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/',
                        'Wife Id': '@I3@', 'Wife Name': 'Payal /Nawar/', 'Children': {1: '@I4@', 2: '@I5@'}}}

        print("\n\n Birthdates are After marriage date of their parents")
        self.assertEqual(userstory8(si1, sf1), "TRUE")
        print("\n\n Birthdates are Before marriage date of their parents")
        self.assertEqual(userstory8(si2, sf2), "FALSE")
        print("\n\n Marriage date are NA")
        self.assertEqual(userstory8(si3, sf3), "NA")

    def test_userstory09(self):

        # all birthdates are after marriage date of their parents
        si1 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '1975-01-01', 'FAMS': {1: '@F1@', 2: '@F2@'}, 'FAMC': 'NA'}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F2@'},
                                                                                                                                                                        'FAMC': 'NA'}, '@I3@': {'Name': 'Payal /Nawar/', 'Gender': 'F', 'Birthday': '1975-04-03', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': 'NA'}, '@I4@': {'Name': 'Rani /Nawar/', 'Gender': 'F', 'Birthday': '1995-11-10', 'Death': 'NA', 'FAMS': {1: '@F3@'}, 'FAMC': '@F1@'}}
        sf1 = {'@F1@': {'Married': '1970-06-15', 'Divorced': 'NA', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/',
                        'Wife Id': '@I3@', 'Wife Name': 'Payal /Nawar/', 'Children': {1: '@I4@', 2: '@I5@'}}}

        print("\n\n Birth Before Death of Parents")
        self.assertEqual(userstory09(si1, sf1), "FALSE")

    def test_userstory10(self):

        si1 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': 'NA', 'FAMS': {1: '@F1@', 2: '@F2@'}, 'FAMC': 'NA'}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F2@'},
                                                                                                                                                                'FAMC': 'NA'}, '@I3@': {'Name': 'Payal /Nawar/', 'Gender': 'F', 'Birthday': '1975-04-03', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': 'NA'}, '@I4@': {'Name': 'Rani /Nawar/', 'Gender': 'F', 'Birthday': '1994-11-10', 'Death': 'NA', 'FAMS': {1: '@F3@'}, 'FAMC': '@F1@'}}
        sf1 = {'@F1@': {'Married': '1970-06-15', 'Divorced': 'NA', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/',
                        'Wife Id': '@I3@', 'Wife Name': 'Payal /Nawar/', 'Children': {1: '@I4@', 2: '@I5@'}}}

        print("\n\n Marriage After 14")
        self.assertEqual(userstory10(si1, sf1), "TRUE")

    def test_userstory35(self):

        si1 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-03-010', 'Death': 'NA', 'FAMS': {1: '@F1@', 2: '@F2@'}, 'FAMC': 'NA'}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F2@'},
                                                                                                                                                                 'FAMC': 'NA'}, '@I3@': {'Name': 'Payal /Nawar/', 'Gender': 'F', 'Birthday': '1975-04-03', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': 'NA'}, '@I4@': {'Name': 'Rani /Nawar/', 'Gender': 'F', 'Birthday': '1994-11-10', 'Death': 'NA', 'FAMS': {1: '@F3@'}, 'FAMC': '@F1@'}}
        si2 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-05-05', 'Death': 'NA', 'FAMS': {1: '@F1@', 2: '@F2@'}, 'FAMC': 'NA'}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F2@'},
                                                                                                                                                                'FAMC': 'NA'}, '@I3@': {'Name': 'Payal /Nawar/', 'Gender': 'F', 'Birthday': '1975-04-03', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': 'NA'}, '@I4@': {'Name': 'Rani /Nawar/', 'Gender': 'F', 'Birthday': '1994-11-10', 'Death': 'NA', 'FAMS': {1: '@F3@'}, 'FAMC': '@F1@'}}

        print("\n\n Recent Birthdates")
        self.assertEqual(userstory35(si1), "TRUE")
        self.assertEqual(userstory35(si2), "FALSE")

    def test_userstory36(self):

        si1 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-03-010', 'Death': 'NA', 'FAMS': {1: '@F1@', 2: '@F2@'}, 'FAMC': 'NA'}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F2@'},
                                                                                                                                                                 'FAMC': 'NA'}, '@I3@': {'Name': 'Payal /Nawar/', 'Gender': 'F', 'Birthday': '1975-04-03', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': 'NA'}, '@I4@': {'Name': 'Rani /Nawar/', 'Gender': 'F', 'Birthday': '1994-11-10', 'Death': 'NA', 'FAMS': {1: '@F3@'}, 'FAMC': '@F1@'}}
        si2 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-05-05', 'Death': 'NA', 'FAMS': {1: '@F1@', 2: '@F2@'}, 'FAMC': 'NA'}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F2@'},
                                                                                                                                                                'FAMC': 'NA'}, '@I3@': {'Name': 'Payal /Nawar/', 'Gender': 'F', 'Birthday': '1975-04-03', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': 'NA'}, '@I4@': {'Name': 'Rani /Nawar/', 'Gender': 'F', 'Birthday': '1994-11-10', 'Death': 'NA', 'FAMS': {1: '@F3@'}, 'FAMC': '@F1@'}}

        print("\n\n Recent Deaths")
        self.assertEqual(userstory36(si1), "TRUE")
        self.assertEqual(userstory36(si2), "FALSE")

    def test_userstory38(self):

        si1 = {'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-04-20',
                        'Death': 'NA', 'FAMS': {1: '@F1@', 2: '@F2@'}, 'FAMC': 'NA'}}

        print("\n\n Upcoming Birthdates")
        self.assertEqual(userstory38(si1), "TRUE")

    def test_userstory39(self):

        sf1 = {'@F1@': {'Married': '1970-04-25', 'Divorced': 'NA', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/',
                        'Wife Id': '@I3@', 'Wife Name': 'Payal /Nawar/', 'Children': {1: '@I4@', 2: '@I5@'}}}

        print("\n\n Upcoming Marriage Anniversary")
        self.assertEqual(userstory39(sf1), "TRUE")

    #-------------------Dinesh's Tetst Case Section End--------------------#
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
