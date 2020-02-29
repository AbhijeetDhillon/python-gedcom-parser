import dateutil.parser as dparser
from datetime import datetime
import dateutil.parser
import datetime
import json
import fileinput
import unittest
from prettytable import PrettyTable

li = {"0": ["INDI", "FAM", "HEAD", "TRLR", "NOTE"], "1": ["NAME", "SEX", "BIRT",
                                                          "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"], "2": ["DATE"]}
# imports

ind_details = {}
fam_details = {}
# gedcom parser


def initialize_var(individual_id, name, sex, birt, deat, fams, famc, fam, marr, husb, wife, chil, div, date, fs):

    individual_id = ""
    name = ""
    sex = ""
    birt = "NA"
    deat = 'NA'
    famc = 'NA'
    fams = {}
    fam = ""
    marr = ""
    husb = ""
    wife = ""
    chil = {}
    div = ""
    date = ""
    fs = 1
    # fc = 1
     # idcount = 0
    return individual_id, name, sex, birt, deat, fams, famc, fam, marr, husb, wife, chil, div, date, fs


def dateCalc(dat):

    try:
        if(len(datetime.datetime.strptime(dat,'%d %b %Y').strftime('%Y-%m-%d')) == 10):
           return datetime.datetime.strptime(dat,'%d %b %Y').strftime('%Y-%m-%d') 

    except ValueError:
           if((len(dat)==4)):
               return dat
           else:
               return 'NA'
      


def calcAge(dob):
    if(dob == "NA"):
        return "NA"
    else:
        from datetime import datetime, date
        today = date.today()
        born = datetime.strptime(dob,'%Y-%m-%d')
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        return age
    

#-------------Parser Starts----------#

def file_reading_gen(path):
    file = open(path, "r")
    ind_details = {}
    fam_details = {}
    individual_id = ""
    name = ""
    sex = ""
    birt = ""
    deat = ""
    fs = 1
    cs=1
    # fc = 1
    famc = ""
    fams = {}
    fam = ""
    marr = ""
    husb = ""
    wife = ""
    chil = {}
    div = ""
    date = ""
    idcount = 0
    fcount = 0
   
    for line in file:

        liner = line.split()
        if(liner == []):
            continue

        elif liner[0] in ["0", "1", "2"]:
            for key, values in li.items():

                if liner[0] == key:
                    if liner[1] in values and liner[1] not in ["INDI", "FAM"]:
                        if liner[1] == "NAME":
                            name = (' '.join(liner[2::]))
                        elif liner[1] == "SEX":
                            sex = (' '.join(liner[2::]))
                        elif liner[1] == "FAMS":
                            fams[fs]=(' '.join(liner[2::]))
                            fs = fs + 1
                        elif liner[1] == "FAMC":
                            famc = (' '.join(liner[2::]))
                        elif liner[1] == "HUSB":
                            husb = ' '.join(liner[2::])
                        elif liner[1] == "WIFE":
                            wife = ' '.join(liner[2::])
                        elif liner[1] == "CHIL":
                            chil[cs] = (' '.join(liner[2::]))
                            cs = cs+1
                        elif liner[1] == "BIRT":
                            bcount = True
                        elif liner[1] == "DEAT":
                            dcount = True
                            deat="dead"
                        elif liner[1] == "MARR":
                            marrcount = True
                        elif liner[1] == "DIV":
                            divcount = True
                        elif liner[1] == "DATE":
                            if bcount == True:
                                birt = ' '.join(liner[2::])
                                birt = dateCalc(birt)
                                bcount = False
                                
                            if dcount == True:
                                deat = ' '.join(liner[2::])
                                deat = dateCalc(deat)
                                dcount = False
                            if marrcount == True:
                                marr = ' '.join(liner[2::])
                                marr = dateCalc(marr)
                                marrcount = False
                            if divcount == True:
                                div = ' '.join(liner[2::])
                                div = dateCalc(div)
                                divcount = False

                    elif (liner[0] == '0' and liner[2] in ["INDI", "FAM"]):
                            bcount = False
                            dcount = False
                            marrcount = False
                            divcount = False
                            if idcount == 1:
                                ind_details[individual_id] = {"Name": name, 'Gender': sex, 'Birthday': birt, 'Death': deat, 'FAMS': fams, 'FAMC': famc}
                                   
                            if fcount ==1:
                                fam_details[fam] = {"Married": marr, 'Divorced': div, 'Husband Id': husb, 'Husband Name': ind_details.get(husb,{}).get('Name'), 'Wife Id': wife, 'Wife Name':ind_details.get(wife,{}).get('Name'),'Children':chil }

                            if liner[2] == "INDI":
                                individual_id,name,sex,birt,deat,fams,famc,fam,marr,husb,wife,chil,div,date,fs=initialize_var(individual_id,name,sex,birt,deat,fams,famc,fam,marr,husb,wife,chil,div,date,fs)
                                individual_id = liner[1]
                                idcount = 1
                            elif liner[2] == "FAM":
                                marr,div,husb,wife,chil = 'NA','NA',0,0,{}
                                fam = liner[1]
                                fcount = 1

                    elif((liner[1] in ["_CURRENT"])):
                        fcount = fam_details[fam] = {"Married": marr, 'Divorced': div, 'Husband Id': husb, 'Husband Name': ind_details.get(husb,{}).get('Name'), 'Wife Id': wife, 'Wife Name':ind_details.get(wife,{}).get('Name'),'Children':chil }

        else:
            pass
    formingPrettyTable(fam_details,ind_details)

    #---------Start Calling User Story Test Cases-------------#

    US03(ind_details)

    #---------End Calling User Story Test Cases---------------#

#----------Parser Ends----------------------#
  

#----------Pretty Table Starts--------------#

def formingPrettyTable(familyDetails,indiDetails):

    fam_details = familyDetails
    ind_details = indiDetails
    x = PrettyTable()

    x2 = PrettyTable()

    x.field_names = ["ID", "Name", "Gender", "Birthday","Age","Alive","Death","Child","Spouse"]

    x2.field_names = ["ID", "Married", "Divorced", "Husband ID","Husband Name","Wife ID","Wife Name","Children"]

    for key,value in ind_details.items():
    # alive or not
        if value['Death'] == 'NA' : 
            alive = 'True' 
        elif value['Death'] == 'dead':
            alive = 'False'
            value['Death'] = 'NA' 
        else:
            alive = 'False'
        age = calcAge(value['Birthday'])

        # FAMC
        if value['FAMC'] == 'NA' :
            fc= 'NA'
        else:
            fc= "{'"+ value['FAMC'][1:-1]+"'}"
            
        # FAMS
        if value['FAMS'] == {} :
            sf= 'NA'
        else:
            sf = value['FAMS']   
            sf = list(sf.values())   #converts the list  
            sf = [s.replace('@', '') for s in sf]   #strips @ from id
            sf=set(sf)  #convert to set
        # add rows
        x.add_row([key[1:-1],value['Name'],value['Gender'],value['Birthday'],age,alive,value['Death'],fc,sf])

    for key, value in fam_details.items():
        if value['Children'] == {} :
            ch = "NA"
        else:
            ch = value['Children']   
            ch = list(ch.values())   #converts the list  
            ch = [s.replace('@', '') for s in ch]   #strips @ from id
            ch=set(ch)  #convert to set
               
        x2.add_row([key[1:-1],value['Married'],value['Divorced'],value['Husband Id'][1:-1],value['Husband Name'],value['Wife Id'][1:-1],value['Wife Name'],ch])

    # print result
    print("\n\n\n Individuals")
    print(x)
    print("\n\n\n  Family")
    print(x2)

#---------------Pretty Table ends---------------#


# --------Implement Test Cases------------#


#Aishwarya's Section Start


#Aishwarya's Section End



#Abhijeet's Section Start
def US03(indiDetails):

    ind_details = indiDetails
    prettyTable03 = PrettyTable()
    prettyTable03.field_names = ["Birth Date", "Death Date","DeathBeforeBirth"]
    deathBeforeBirth = []
    deathList = []
    birthlist = []
    isdeathBeforeBirth = False
    for key,value in ind_details.items():
        isdeathBeforeBirth = False
        if len(value['Death'])==10:
            deathList.append(value['Death'])
        else:
            deathList.append('NA')

        if len(value['Birthday'])==10:
            birthlist.append(value['Birthday'])
        else:
            birthlist.append('NA')

    for i in range(len(birthlist)):

        if(deathList[i] != "NA" and birthlist !="NA"):
            if(deathList[i]<birthlist[i]):
                deathBeforeBirth.append("True")
                isdeathBeforeBirth = True
            else:
                deathBeforeBirth.append("False")    

        else:
            deathBeforeBirth.append("NA")
        

        prettyTable03.add_row([birthlist[i],deathList[i],deathBeforeBirth[i]])
        
        
    print("\n\n\n User Story 03- Death Before Birth")
    print(prettyTable03)
    return isdeathBeforeBirth

#Abhijeet's Section End


#Dinesh's Section Start


#Dinesh's Section End



#------------------Start : Testing Function With Test Cases--------------------#

# class TestContainer(unittest.TestCase):
#     def US03Test(self):

#         test1 = {"Name": "Tester 1", 'Gender': "Male", 'Birthday': "2000-03-13", 'Death': "1999-03-17", 'FAMS': "F9", 'FAMC': "f9"}

#         """to verify that anagram_1st works properly"""
#         self.assertTrue(US03(test1, True))
#         # self.assertTrue(US03("", "dirtyroom"))
#         # self.assertTrue(US03("DORMITORY", "dirtyroom"))
#         # self.assertTrue(US03("122Dirtry", ""))
#         # self.assertTrue(US03("Iceman", "Cinema"))

if __name__ == '__main__':
    filename1="Family.ged"
    filename="Keanu_Reeves_Family.ged"
    file_reading_gen(filename1)
    #unittest.main(exit=False, verbosity=2)