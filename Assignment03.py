from datetime import datetime
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

    us03_birth_b4_death(ind_details)
    us04_marr_b4_divorce(fam_details)
    US02(ind_details,fam_details)
    US05(ind_details,fam_details)
    userstory1(ind_details,fam_details)
    userstory8(ind_details,fam_details)

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
#user story 02
def US02(i,f):
    datelist=[]
    for k,v in i.items():
        y=[k[1:-1],v["Birthday"]]
        datelist.append(y)

    ls=[]
    for v in f.values():
        if(v["Married"] != "NA"):
            x=[v["Married"],v["Husband Id"][1:-1],v["Wife Id"][1:-1]]
            ls.append(x)  
        else:
            x=["NA",v["Husband Id"][1:-1],v["Wife Id"][1:-1]]
            ls.append(x)  

    result = []
    for a in ls:
        hid=a[1]
        wid=a[2]
        l_datelist=len(datelist)
        for i in range(l_datelist):
            if(datelist[i][0]==hid):
                hdate=datelist[i][1]
                a = a + [hdate]
        for i in range(l_datelist):    
            if(datelist[i][0]==wid):
                wdate=datelist[i][1]
                a = a + [wdate]
        d=[a[0],hid,hdate,wid,wdate]
        result.append(d)

    ct=0
    for x in f:
      result[ct].append(x[1:-1])
      ct+=1
    

    print("\n\n\n User Story 02 - Birth Before Marriage")
    hflag="False"
    wflag="False"
    y1 = PrettyTable()
    y1.field_names = ["ID", "Married date", "Husband Birthday", "Wife Birthdate","Birth Before Marriage(Husband)","Birth Before Marriage(Wife)"]
    for e in result:
      if(e[0]=="NA"):
        hflag="NA"
        wflag="NA"
        y1.add_row([e[5],e[0],e[2],e[4],hflag,wflag])
      else:
        if(e[0] > e[2]):
          hflag="True"
        if(e[0] > e[4]):
          wflag="True"
        if(e[2]=="NA"):
          hflag="NA"
        if(e[4]=="NA"):
          wflag="NA"
        y1.add_row([e[5],e[0],e[2],e[4],hflag,wflag])

      
    print(y1)
    return "True"

#user story 05
def US05(i,f):
    datelist=[]
    for k,v in i.items():
        if(v["Death"]!="NA"):
            y=[k[1:-1],v["Death"]]
            datelist.append(y)
        else:
            y=[k[1:-1],"NA"]
            datelist.append(y)

    ls=[]
    for v in f.values():
        if(v["Married"] != "NA"):
            x=[v["Married"],v["Husband Id"][1:-1],v["Wife Id"][1:-1]]
            ls.append(x)
            
        else:
            x=["NA",v["Husband Id"][1:-1],v["Wife Id"][1:-1]]
            ls.append(x)
           

    result = []
    for a in ls:
        hid=a[1]
        wid=a[2]
        l_datelist=len(datelist)
        
        for i in range(l_datelist):
            if(datelist[i][0]==hid):
                hdate=datelist[i][1]
                a.insert(3,hdate)
                
            elif(datelist[i][0]==wid):
                 wdate=datelist[i][1]
                 a.insert(4,wdate)
                 
            else:
                hdate="NA"
                a = a + [hdate]
               

        d=[a[0],hid,hdate,wid,wdate]
        result.append(d)

    ct=0
    for x in f:
      result[ct].append(x[1:-1])
      ct+=1

    hflag="False"
    wflag="False"
    y1 = PrettyTable()
    y1.field_names = ["ID", "Married date", "Husband Death date", "Wife Death date","Marriage Before Death(Husband)","Marriage Before Death(Wife)"]
    print("\n\n\n User Story 05 - Marriage Before Death")
    for e in result:
      if(e[0]=="NA"):
        hflag="NA"
        wflag="NA"
        y1.add_row([e[5],e[0],e[2],e[4],hflag,wflag])
      else:
        if(e[0] < e[2]):
          hflag="True"
        if(e[0] < e[4]):
          wflag="True"
        if(e[2]=="NA"):
          hflag="NA"
        if(e[4]=="NA"):
          wflag="NA"
        y1.add_row([e[5],e[0],e[2],e[4],hflag,wflag])
      
    print(y1)
    return "True"



#Aishwarya's Section End



#Abhijeet's Section Start
def us03_birth_b4_death(indiDetails):

    ind_details = indiDetails
    prettyTable03 = PrettyTable()
    prettyTable03.field_names = ["ID","Birth Date", "Death Date","DeathBeforeBirth"]
    deathBeforeBirth = []
    deathList = []
    birthlist = []
    idList = []
    isdeathBeforeBirth = "False"
    for key,value in ind_details.items():
    
        idList.append(key[1:-1])
        if len(value['Death'])==10:
            deathList.append(value['Death'])
        else:
            deathList.append('NA')

        if len(value['Birthday'])==10:
            birthlist.append(value['Birthday'])
        else:
            birthlist.append('NA')

    for i in range(len(birthlist)):

        if(deathList[i] != "NA" and birthlist[i] !="NA"):
            if(deathList[i]<birthlist[i]):
                deathBeforeBirth.append("True")
                isdeathBeforeBirth = "True"
            else:
                deathBeforeBirth.append("False")
                isdeathBeforeBirth = "False"    

        else:
            deathBeforeBirth.append("NA")
            isdeathBeforeBirth = "NA"
        

        prettyTable03.add_row([idList[i],birthlist[i],deathList[i],deathBeforeBirth[i]])
        
        
    print("\n\n\n User Story 03- Death Before Birth")
    print(prettyTable03)
    return isdeathBeforeBirth


def us04_marr_b4_divorce(famDetails):
    fam_details = famDetails
    prettyTable04 = PrettyTable()
    prettyTable04.field_names = ["ID","Marriage Date", "Divorce Date","DivorceBeforeMarriage"]
    divorceBeforeMarriage = []

    marriageList = []
    divorceList =[]
    idList = []
    isDivorceBeforeMarriage = "False"
    for key, value in fam_details.items():
        idList.append(key[1:-1])
        if len(value['Married']) == 10:
            marriageList.append(value['Married'])
        else:
            marriageList.append('NA')
        
        if len(value['Divorced']) == 10:
            divorceList.append(value['Divorced'])
        else:
            divorceList.append('NA')

    for i in range(len(marriageList)):

        if(divorceList[i] !='NA' and marriageList[i]!='NA'):

            if(divorceList[i]<marriageList[i]):
                divorceBeforeMarriage.append('True')
                isDivorceBeforeMarriage = "True"
            else:
                divorceBeforeMarriage.append('False')
                isDivorceBeforeMarriage = "False"
        else:
            divorceBeforeMarriage.append('NA')
            isDivorceBeforeMarriage = "NA"

        prettyTable04.add_row([idList[i],marriageList[i],divorceList[i],divorceBeforeMarriage[i]])

    print("\n\n\n User Story 04- Divorce Before Marriage")
    print(prettyTable04)
    return isDivorceBeforeMarriage   

#Abhijeet's Section End


#Dinesh's Section Start

def userstory1(indiDetails,familyDetails):
    
    today = datetime.datetime.now()
    today = datetime.datetime.strftime(today,'%Y-%m-%d')
    list_date=[]
    final_date_list=[]
    isDateBeforeToday ="False"

    for key,value in indiDetails.items():
        if (len(value['Birthday'])) == 10 :
            list_date.append(value['Birthday'])
        if (len(value['Death'])) == 10 :
            list_date.append(value['Death'])
    for key,value in familyDetails.items():
        if (len(value['Married'])) == 10 :
            list_date.append(value['Married'])
        if (len(value['Divorced'])) == 10 :
            list_date.append(value['Divorced'])
    

    prettyTable01 = PrettyTable()
    prettyTable01.field_names = [ "Today","Dates","DatesBeforeCurrentDate"]
    for i in range(len(list_date)):
    
        if list_date[i] < today:
            final_date_list.append("TRUE")
            isDateBeforeToday ="TRUE"

        else:
            final_date_list.append("FALSE")
            isDateBeforeToday ="FALSE"

        prettyTable01.add_row([today,list_date[i],final_date_list[i]])
    print("\n\n\n User Story 01- Dates Before Current Date")
    print(prettyTable01)
    return isDateBeforeToday


def userstory8(indiDetails,familyDetails):
    m = PrettyTable()
    isBirthBeforeMarriage = "NA"
    marriageDate = "NA"
    m.field_names=['Name','Birthday','Parent Marriage Date','IsBirthBeforeMarriage']
    for value in indiDetails.values():

        if (value['FAMC']) != "NA" and (value['Birthday']) != "NA" and (familyDetails[value['FAMC']]['Married']) != "NA" :
            if (familyDetails[value['FAMC']]['Married']) > (value['Birthday']) :
                isBirthBeforeMarriage = "TRUE"
                marriageDate = familyDetails[value['FAMC']]['Married']
            else:
                isBirthBeforeMarriage = "FALSE"
                marriageDate = familyDetails[value['FAMC']]['Married']
        
        else:
            isBirthBeforeMarriage = "NA"
            marriageDate = "NA"
        m.add_row([value['Name'],value['Birthday'],marriageDate,isBirthBeforeMarriage])
    print("\n\n\n User Story 08- Birth before marriage of parents")
    print(m)
    return isBirthBeforeMarriage
    

#Dinesh's Section End



#------------------Start : Testing Function With Test Cases--------------------#

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
            self.assertEqual(US05(si1,sf1),"True")

            print("\n\n Birthdays missing\n")
            #birthdays missing
            self.assertEqual(US02(si2,sf2),"True")
            self.assertEqual(US05(si2,sf2),"True")

            print("\n\n Marriage dates missing\n")
            #marriage dates missing
            self.assertEqual(US02(si4,sf4),"True")
            self.assertEqual(US05(si4,sf4),"True")
        
            print("\n\n Marriage before birth\n")
            #marriage before birthday
            self.assertEqual(US02(si5,sf5),"True")
            self.assertEqual(US05(si5,sf5),"True")

        
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
            self.assertEqual(US02(si1,sf1),"True")
            self.assertEqual(US05(si1,sf1),"True")

            print("\n\n Deathdates missing\n")
            #deathdates missing
            self.assertEqual(US02(si3,sf3),"True")
            self.assertEqual(US05(si3,sf3),"True")

            print("\n\n Marriage dates missing\n")
            #marriage dates missing
            self.assertEqual(US02(si4,sf4),"True")
            self.assertEqual(US05(si4,sf4),"True")

            print("\n\n Death before marriage\n")
            #death before marriage
            self.assertEqual(US02(si6,sf6),"True")
            self.assertEqual(US05(si6,sf6),"True")

    #-------------------Aishwarya's Tetst Case Section End--------------------#

    #-------------------Abhijeet's Tetst Case Section Start--------------------#

    def test_us03_birth_b4_death(self):
        #all values of birthdays and death days given
        si1={'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        
        #birthdays missing
        si2={'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': 'NA', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': 'NA', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        
        #death dates missing
        si4={'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        
        #death before birth
        si5={'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '2000-01-01', 'Death': '1996-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '2000-08-04', 'Death': '1978-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        

    
        print("\n\n All values of birthdays and death days given(test_us03_birth_b4_death)\n")
        #all values of birthdays and death days given
        self.assertEqual(us03_birth_b4_death(si1),"False")

        print("\n\n Birthdays missing (test_us03_birth_b4_death)")
        #birthdays missing
        self.assertEqual(us03_birth_b4_death(si2),"NA")

        print("\n\n Death dates missing(test_us03_birth_b4_death)")
        #birth dates missing
        self.assertEqual(us03_birth_b4_death(si4),"NA")
    
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

        print("\n\n Divorce dates missing (test_us04_marr_b4_divorce)")
        #birthdays missing
        self.assertEqual(us04_marr_b4_divorce(sf2),"NA")

        print("\n\n Marriage dates missing(test_us04_marr_b4_divorce)")
        #birth dates missing
        self.assertEqual(us04_marr_b4_divorce(sf4),"NA")
    
        print("\n\n Divorce before Marriage(test_us04_marr_b4_divorce)")
        #birth before birthday
        self.assertEqual(us04_marr_b4_divorce(sf5),"True")


    #-------------------Abhijeet's Tetst Case Section End--------------------#

    #-------------------Dinessh's Tetst Case Section Start--------------------#
    
    def test_userstory1(self):

        #all dates are before today's date
        si1={'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '1966-01-01', 'Death': '2000-08-01', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '1978-08-04', 'Death': '2000-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf1={'@F1@': {'Married': '1990-06-15', 'Divorced': '1998-06-15', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}
        
        #all dates are future dates
        si3={'@I1@': {'Name': 'Smit /Nawar/', 'Gender': 'M', 'Birthday': '2030-01-01', 'Death': 'NA', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}, '@I2@': {'Name': 'Yi Xie /Nawar/', 'Gender': 'F', 'Birthday': '2045-08-04', 'Death': '2070-08-05', 'FAMS': {1: '@F1@'}, 'FAMC': {1: '@I4@'}}}
        sf3={'@F1@': {'Married': '2021-06-15', 'Divorced': '2055-06-15', 'Husband Id': '@I1@', 'Husband Name': 'Smit /Nawar/', 'Wife Id': '@I2@', 'Wife Name': 'Yi Xie /Nawar/', 'Children': {1: '@I4@'}}}

        print("\n\n Dates are Before today's date")
        self.assertEqual(userstory1(si1,sf1),"TRUE")
        print("\n\n Future Dates")
        self.assertEqual(userstory1(si3,sf3),"FALSE")

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
    filename1="000.ged"
    filename="Keanu_Reeves_Family.ged"
    file_reading_gen(filename1)
    unittest.main(exit=False, verbosity=2)
