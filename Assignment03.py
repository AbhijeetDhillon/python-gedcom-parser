from datetime import datetime
import datetime
import json
import fileinput
import unittest
from prettytable import PrettyTable
from parserLogic import calcAge,file_reading_gen,dateCalc


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
                print("ERROR: INDIVIDUAL: US03:",idList[i],"Died",deathList[i],"before born",birthlist[i])
            
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
                print("ERROR: Family: US04:",idList[i],"Divorce",divorceList[i],"before married",marriageList[i])

    return isDivorceBeforeMarriage   

#Abhijeet's Section End


#Dinesh's Section Start

def userstory1(indiDetails,familyDetails):
    
    today = datetime.datetime.now()
    today = datetime.datetime.strftime(today,'%Y-%m-%d')
    list_date=[]
    event_list =[]
    final_date_list=[]
    isDateBeforeToday ="FALSE"
    id_list =[]
    for key,value in indiDetails.items():
        
        if (len(value['Birthday'])) == 10 :
            id_list.append(key[1:-1])
            list_date.append(value['Birthday'])
            event_list.append("Birthday")
        if (len(value['Death'])) == 10 :
            id_list.append(key[1:-1])
            list_date.append(value['Death'])
            event_list.append("Death")
    for key,value in familyDetails.items():
        id_list.append(key[1:-1])    
        if (len(value['Married'])) == 10 :
            id_list.append(key[1:-1])
            list_date.append(value['Married'])
            event_list.append("Marriage")
        if (len(value['Divorced'])) == 10 :
            id_list.append(key[1:-1])
            list_date.append(value['Divorced'])
            event_list.append("Divorce")
    

    prettyTable01 = PrettyTable()
    prettyTable01.field_names = [ "Today","Dates","DatesBeforeCurrentDate"]
    for i in range(len(list_date)):
    
        if list_date[i] > today:
            final_date_list.append("TRUE")
            isDateBeforeToday ="TRUE"
            if(event_list[i] == "Marriage" or event_list[i] == "Divorce" ):
                print("FAMILY: US01:",id_list[i],event_list[i],list_date[i],"occurs in future")
            else:
                print("INDIVIDUAL: US01:",id_list[i],event_list[i],list_date[i],"occurs in future")
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



if __name__ == '__main__':


    
    filename1="Family.ged"
    filename="Keanu_Reeves_Family.ged"
    fam_details, ind_details = file_reading_gen(filename1)
    unittest.main(exit=False, verbosity=2)

    #Calling User Stories

    us03_birth_b4_death(ind_details)
    us04_marr_b4_divorce(fam_details)
    US02(ind_details,fam_details)
    US05(ind_details,fam_details)
    userstory1(ind_details,fam_details)
    userstory8(ind_details,fam_details)
