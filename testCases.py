import unittest

from Assignment03 import US02,US05,us03_birth_b4_death,us04_marr_b4_divorce,userstory1,userstory8
from parserLogic import file_reading_gen

class TestContainer(unittest.TestCase):
        
    
    #-------------------Aishwarya's Tetst Case Section Start--------------------#

    def test_US02(self):
        #all values of birthdays and death days given
        si1={'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf1={'@F1@': {'Married': '1990-06-15', 'Divorced': '1998-06-15', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}
        
        #birthdays missing
        si2={'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': 'NA', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf2={'@F1@': {'Married': '1990-06-15', 'Divorced': '1998-06-15', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}
        
        #marriage dates missing
        si4={'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf4={'@F1@': {'Married': 'NA', 'Divorced': '1998-06-15', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}
        
        #marriage before birthday
        si5={'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf5={'@F1@': {'Married': '1950-01-01', 'Divorced': '1998-06-15', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}
        

        for i in range(1):
            print("\n\n All values of birthdays and death days given\n")
            #all values of birthdays and death days given
            self.assertEqual(US02(si1,sf1),"True")
           

            print("\n\n Birthdays missing\n")
            #birthdays missing
            self.assertEqual(US02(si2,sf2),"True")
         

            print("\n\n Marriage dates missing\n")
            #marriage dates missing
            self.assertEqual(US02(si4,sf4),"True")
            
        
            print("\n\n Marriage before birth\n")
            #marriage before birthday
            self.assertEqual(US02(si5,sf5),"True")
          

        
    def test_US05(self):
        #all values of birthdays and death days given
        si1={'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf1={'@F1@': {'Married': '1990-06-15', 'Divorced': '1998-06-15', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}
        
        #deathdates missing
        si3={'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf3={'@F1@': {'Married': '1990-06-15', 'Divorced': '1998-06-15', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}
        
        #marriage dates missing
        si4={'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf4={'@F1@': {'Married': 'NA', 'Divorced': '1998-06-15', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}
    
        #death before marriage
        si6={'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '1980-08-15', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf6={'@F1@': {'Married': '1990-06-15', 'Divorced': '1998-06-15', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}
        
        for i in range(1):
            print("\n\n All values of birthdays and death days given\n")
            #all values of birthdays and death days given
            self.assertEqual(US05(si1,sf1),"True")

            print("\n\n Deathdates missing\n")
            #deathdates missing
            self.assertEqual(US05(si3,sf3),"True")

            print("\n\n Marriage dates missing\n")
            #marriage dates missing
            self.assertEqual(US05(si4,sf4),"True")

            print("\n\n Death before marriage\n")
            #death before marriage
            self.assertEqual(US05(si6,sf6),"True")

    #-------------------Aishwarya's Tetst Case Section End--------------------#

    #-------------------Abhijeet's Tetst Case Section Start--------------------#

    def test_us03_birth_b4_death(self):
        #all values of birthdays and death days given
        si1={'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        
        #death before birth
        si5={'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '2000-01-01', 'Death': '1996-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '2000-08-04', 'Death': '1978-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        

    
        print("\n\n All values of birthdays and death days given(test_us03_birth_b4_death)\n")
        #all values of birthdays and death days given
        self.assertEqual(us03_birth_b4_death(si1),"False")

        print("\n\n Deaths before birth(test_us03_birth_b4_death)")
        #birth before birthday
        self.assertEqual(us03_birth_b4_death(si5),"True")


    def test_us04_marr_b4_divorce(self):
        #all values of birthdays and death days given
        sf1={'@F1@': {'Married': '1990-06-15', 'Divorced': '1998-06-15', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}
        
        #birthdays missing
        sf2={'@F1@': {'Married': '1990-06-15', 'Divorced': 'NA', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}
        
        #death dates missing
        sf4={'@F1@': {'Married': 'NA', 'Divorced': '1998-06-15', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}
        
        #death before birth
        sf5={'@F1@': {'Married': '1983-01-01', 'Divorced': '1950-06-15', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}
        

    
        print("\n\n All values of divorce and death dates given(test_us04_marr_b4_divorce)\n")
        #all values of birthdays and death days given
        self.assertEqual(us04_marr_b4_divorce(sf1),"False")

        print("\n\n Divorce before Marriage(test_us04_marr_b4_divorce)")
        #birth before birthday
        self.assertEqual(us04_marr_b4_divorce(sf5),"True")


    #-------------------Abhijeet's Tetst Case Section End--------------------#

    #-------------------Dinessh's Tetst Case Section Start--------------------#
    
    def test_userstory1(self):

        #all dates are before today's date
        si1={'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1900-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf1={'@F1@': {'Married': '1990-06-15', 'Divorced': '1998-06-15', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}
        
        #all dates are future dates
        si3={'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '2030-01-01', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '2045-08-04', 'Death': '2070-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf3={'@F1@': {'Married': '2021-06-15', 'Divorced': '2055-06-15', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        print("\n\n Dates are Before today's date")
        self.assertEqual(userstory1(si1,sf1),"FALSE")
        print("\n\n Future Dates")
        self.assertEqual(userstory1(si3,sf3),"TRUE")

    def test_userstory8(self):

        #all birthdates are after marriage date of their parents
        si1={'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': 'NA', 'FAMS': {1: '@F1@', 2: '@F2@'}, 'FAMC': 'NA'}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F2@'}, 'FAMC': 'NA'}, '@I3@': {'Name': 'Payal /Nawar/', 'Gender': 'F', 'Birthday': '1975-04-03', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': 'NA'}, '@I4@': {'Name': 'Rani /Nawar/', 'Gender': 'F', 'Birthday': '1994-11-10', 'Death': 'NA', 'FAMS': {1: '@F3@'}, 'FAMC': '@F1@'}}
        sf1={'@F1@': {'Married': '2000-06-15', 'Divorced': 'NA', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I3@', 'Wife Name': 'Payal /Nawar/', 'Children': {1: '@I4@', 2: '@I5@'}}}
        
        #all birthdates are before marriage date of their parents
        si2={'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': 'NA', 'FAMS': {1: '@F1@', 2: '@F2@'}, 'FAMC': 'NA'}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F2@'}, 'FAMC': 'NA'}, '@I3@': {'Name': 'Payal /Nawar/', 'Gender': 'F', 'Birthday': '1975-04-03', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': 'NA'}, '@I4@': {'Name': 'Rani /Nawar/', 'Gender': 'F', 'Birthday': '1994-11-10', 'Death': 'NA', 'FAMS': {1: '@F3@'}, 'FAMC': '@F1@'}}
        sf2={'@F1@': {'Married': '1960-06-15', 'Divorced': 'NA', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I3@', 'Wife Name': 'Payal /Nawar/', 'Children': {1: '@I4@', 2: '@I5@'}}}
        
        #all marriage date are NA
        si3={'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': 'NA', 'FAMS': {1: '@F1@', 2: '@F2@'}, 'FAMC': 'NA'}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F2@'}, 'FAMC': 'NA'}, '@I3@': {'Name': 'Payal /Nawar/', 'Gender': 'F', 'Birthday': '1975-04-03', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': 'NA'}, '@I4@': {'Name': 'Rani /Nawar/', 'Gender': 'F', 'Birthday': '1994-11-10', 'Death': 'NA', 'FAMS': {1: '@F3@'}, 'FAMC': '@F1@'}}
        sf3={'@F1@': {'Married': 'NA', 'Divorced': 'NA', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I3@', 'Wife Name': 'Payal /Nawar/', 'Children': {1: '@I4@', 2: '@I5@'}}}
        
        print("\n\n Birthdates are After marriage date of their parents")
        self.assertEqual(userstory8(si1,sf1),"TRUE")
        print("\n\n Birthdates are Before marriage date of their parents")
        self.assertEqual(userstory8(si2,sf2),"FALSE")
        print("\n\n Marriage date are NA")
        self.assertEqual(userstory8(si3,sf3),"NA")

    #-------------------Dinesh's Tetst Case Section End--------------------#
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
