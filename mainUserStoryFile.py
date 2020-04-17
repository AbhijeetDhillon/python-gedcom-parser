from datetime import datetime
import datetime
import json
import fileinput
import unittest
from prettytable import PrettyTable
from parserLogic import calcAge, file_reading_gen, dateCalc
from collections import OrderedDict
from operator import getitem


#----------Pretty Table Starts--------------#

def formingPrettyTable(familyDetails, indiDetails):

    fam_details = familyDetails
    ind_details = indiDetails
    x = PrettyTable()

    x2 = PrettyTable()

    x.field_names = ["ID", "Name", "Gender", "Birthday",
                     "Age", "Alive", "Death", "Child", "Spouse"]

    x2.field_names = ["ID", "Married", "Divorced", "Husband ID",
                      "Husband Name", "Wife ID", "Wife Name", "Children"]

    for key, value in ind_details.items():
        # alive or not
        if value['Death'] == 'NA':
            alive = 'True'
        elif value['Death'] == 'dead':
            alive = 'False'
            value['Death'] = 'NA'
        else:
            alive = 'False'
        age = calcAge(value['Birthday'])

        # FAMC
        if value['FAMC'] == 'NA':
            fc = 'NA'
        else:
            fc = "{'" + value['FAMC'][1:-1]+"'}"

        # FAMS
        if value['FAMS'] == {}:
            sf = 'NA'
        else:
            sf = value['FAMS']
            sf = list(sf.values())  # converts the list
            sf = [s.replace('@', '') for s in sf]  # strips @ from id
            sf = set(sf)  # convert to set
        # add rows
        x.add_row([key[1:-1], value['Name'], value['Gender'],
                   value['Birthday'], age, alive, value['Death'], fc, sf])

    for key, value in fam_details.items():
        if value['Children'] == {}:
            ch = "NA"
        else:
            ch = value['Children']
            ch = list(ch.values())  # converts the list
            ch = [s.replace('@', '') for s in ch]  # strips @ from id
            ch = set(ch)  # convert to set

        x2.add_row([key[1:-1], value['Married'], value['Divorced'], value['Husband Id']
                    [1:-1], value['Husband Name'], value['Wife Id'][1:-1], value['Wife Name'], ch])

    # print result
    print("\n\n\n Individuals")
    print(x)
    print("\n\n\n  Family")
    print(x2)

#---------------Pretty Table ends---------------#


# --------Implement User Stories------------#


# Aishwarya's Section Start
# user story 02
def US02(i, f):
    datelist = []
    for k, v in i.items():
        y = [k[1:-1], v["Birthday"]]
        datelist.append(y)

    ls = []
    for v in f.values():
        if(v["Married"] != "NA"):
            x = [v["Married"], v["Husband Id"][1:-1], v["Wife Id"][1:-1]]
            ls.append(x)
        else:
            x = ["NA", v["Husband Id"][1:-1], v["Wife Id"][1:-1]]
            ls.append(x)

    result = []
    for a in ls:
        hid = a[1]
        wid = a[2]
        l_datelist = len(datelist)
        for i in range(l_datelist):
            if(datelist[i][0] == hid):
                hdate = datelist[i][1]
                a = a + [hdate]
        for i in range(l_datelist):
            if(datelist[i][0] == wid):
                wdate = datelist[i][1]
                a = a + [wdate]
        d = [a[0], hid, hdate, wid, wdate]
        result.append(d)

    ct = 0
    for x in f:
        result[ct].append(x[1:-1])
        ct += 1

    # print("\n\n\n User Story 02 - Birth Before Marriage")
    hflag = "False"
    wflag = "False"
    y1 = PrettyTable()
    y1.field_names = ["ID", "Married date", "Husband Birthday", "Wife Birthdate",
                      "Birth Before Marriage(Husband)", "Birth Before Marriage(Wife)"]
    for e in result:
        if(e[0] == "NA"):
            hflag = "NA"
            wflag = "NA"
            # print("ERROR: Family: US02:",e[5],": Marriage date not given")
    #    y1.add_row([e[5],e[0],e[2],e[4],hflag,wflag])
        else:
            # if(e[0] > e[2]):
            #   hflag="True"
            #   print("ERROR: Family: US02:",e[5],": Husband's birthdate ",e[2]," before marriage date ",e[0])
            # if(e[0] > e[4]):
            #   wflag="True"
            #   print("ERROR: Family: US02:",e[5],": Wife's birthdate ",e[4]," before marriage date ",e[0])
            if(e[0] < e[2]):
                hflag = "False"
                print("ERROR: Family: US02:",
                      e[5], ": Husband's birthdate ", e[2], " after marriage date ", e[0])
            if(e[0] < e[4]):
                wflag = "False"
                print("ERROR: Family: US02:",
                      e[5], ": Wife's birthdate ", e[4], " after marriage date ", e[0])
            if(e[2] == "NA"):
                hflag = "NA"
            #   print("ERROR: Family: US02:",e[5],": Husband birth date not given")
            if(e[4] == "NA"):
                wflag = "NA"
            #   print("ERROR: Family: US02:",e[5],": Wife birth date not given")
            # y1.add_row([e[5],e[0],e[2],e[4],hflag,wflag])

    # print(y1)
    return "True"

# user story 05


def US05(i, f):
    datelist = []
    for k, v in i.items():
        if(v["Death"] != "NA"):
            y = [k[1:-1], v["Death"]]
            datelist.append(y)
        else:
            y = [k[1:-1], "NA"]
            datelist.append(y)

    ls = []
    for v in f.values():
        if(v["Married"] != "NA"):
            x = [v["Married"], v["Husband Id"][1:-1], v["Wife Id"][1:-1]]
            ls.append(x)

        else:
            x = ["NA", v["Husband Id"][1:-1], v["Wife Id"][1:-1]]
            ls.append(x)

    result = []
    for a in ls:
        hid = a[1]
        wid = a[2]
        l_datelist = len(datelist)

        for i in range(l_datelist):
            if(datelist[i][0] == hid):
                hdate = datelist[i][1]
                a.insert(3, hdate)

            elif(datelist[i][0] == wid):
                wdate = datelist[i][1]
                a.insert(4, wdate)

            else:
                hdate = "NA"
                a = a + [hdate]

        d = [a[0], hid, hdate, wid, wdate]
        result.append(d)

    ct = 0
    for x in f:
        result[ct].append(x[1:-1])
        ct += 1

    hflag = "False"
    wflag = "False"
    y1 = PrettyTable()
    y1.field_names = ["ID", "Married date", "Husband Death date", "Wife Death date",
                      "Marriage Before Death(Husband)", "Marriage Before Death(Wife)"]
    # print("\n\n\n User Story 05 - Marriage Before Death")
    for e in result:
        if(e[0] == "NA"):
            hflag = "NA"
            wflag = "NA"
            # print("ERROR: Family: US05:",e[5],": Marriage date not given")
            # y1.add_row([e[5],e[0],e[2],e[4],hflag,wflag])
        else:
            # if(e[0] < e[2]):
            #   hflag="True"
            #   print("ERROR: Family: US05:",e[5],": Husband's deathdate ",e[2]," after marriage date ",e[0])
            # if(e[0] < e[4]):
            #   wflag="True"
            #   print("ERROR: Family: US05:",e[5],": Husband's deathdate ",e[2]," after marriage date ",e[0])
            if(e[0] > e[2]):
                hflag = "False"
                print("ERROR: Family: US05:",
                      e[5], ": Husband's deathdate ", e[2], " before marriage date ", e[0])
            if(e[0] > e[4]):
                wflag = "False"
                print("ERROR: Family: US05:",
                      e[5], ": Wife's deathdate ", e[2], " before marriage date ", e[0])
            if(e[2] == "NA"):
                hflag = "NA"
            #   print("ERROR: Family: US05:",e[5],": Husband's deathdate not given")
            if(e[4] == "NA"):
                wflag = "NA"
            #   print("ERROR: Family: US05:",e[5],": Wife's deathdate not given")
            # y1.add_row([e[5],e[0],e[2],e[4],hflag,wflag])

    # print(y1)
    return "True"

# sprint 2
# userstory 15


def US15(i, f):
    res = []
    key = []
    c = 0
    for y in f.keys():
        key.append(y[1:-1])
    for x in f.values():
        if(len(x["Children"]) >= 15):
            res.append("False")
            print("ERROR: Family: US15:  Family " +
                  key[c] + " has greater than or equal to 15 siblings")
        else:
            res.append("True")
        # print(key[c])
        c = c+1
    # print(len(res))
    return "True"


def US18(i, f):
    res = []
    fkey = []
    c = 0
    ids = []
    i = len(f)  # length of fam members
    for x in f.values():
        # 2d array of hid , wid
        ids.append([x["Husband Id"][1:-1], x["Wife Id"][1:-1]])
    for y in f.keys():  # key of family id
        fkey.append(y[1:-1])
    for x in f.values():
        child = []
        # hid=x["Husband Id"][1:-1]
        # wid=x["Wife Id"][1:-1]
        for z in x["Children"].values():
            child.append(z[1:-1])

        for item in range(i):
            hid = ids[item][0]
            wid = ids[item][1]
            # print(hid,wid)
            if(hid in child and wid in child):
                res.append("False")
                print("ERROR: Family: US18 Family " +
                      fkey[c]+" siblings are married")

            else:
                res.append("True")
        c = c+1

    return "True"

# Aishwarya's Section End


# Abhijeet's Section Start
def us03_birth_b4_death(indiDetails):

    ind_details = indiDetails
    prettyTable03 = PrettyTable()
    prettyTable03.field_names = [
        "ID", "Birth Date", "Death Date", "DeathBeforeBirth"]
    deathBeforeBirth = []
    deathList = []
    birthlist = []
    idList = []
    isdeathBeforeBirth = "False"
    for key, value in ind_details.items():

        idList.append(key[1:-1])
        if len(value['Death']) == 10:
            deathList.append(value['Death'])
        else:
            deathList.append('NA')

        if len(value['Birthday']) == 10:
            birthlist.append(value['Birthday'])
        else:
            birthlist.append('NA')

    for i in range(len(birthlist)):

        if(deathList[i] != "NA" and birthlist[i] != "NA"):
            if(deathList[i] < birthlist[i]):
                deathBeforeBirth.append("True")
                isdeathBeforeBirth = "True"
                print("ERROR: INDIVIDUAL: US03:",
                      idList[i], "Died", deathList[i], "before born", birthlist[i])

    return isdeathBeforeBirth


def us04_marr_b4_divorce(famDetails):
    fam_details = famDetails
    prettyTable04 = PrettyTable()
    prettyTable04.field_names = [
        "ID", "Marriage Date", "Divorce Date", "DivorceBeforeMarriage"]
    divorceBeforeMarriage = []

    marriageList = []
    divorceList = []
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

        if(divorceList[i] != 'NA' and marriageList[i] != 'NA'):

            if(divorceList[i] < marriageList[i]):
                divorceBeforeMarriage.append('True')
                isDivorceBeforeMarriage = "True"
                print("ERROR: Family: US04:", idList[i], "Divorce",
                      divorceList[i], "before married", marriageList[i])

    return isDivorceBeforeMarriage


def us06_div_b4_death(indiDetails, famDetails):

    isDivBeforeDeath = "False"
    for key, value in famDetails.items():
        if value['Divorced'] != 'NA' and len(value['Divorced']) == 10:
            husbandId = value['Husband Id']
            wifeId = value['Wife Id']
            if indiDetails[husbandId]['Death'] != 'NA' and len(indiDetails[husbandId]['Death']) == 10 and indiDetails[husbandId]['Death'] < value['Divorced']:
                isDivBeforeDeath = "True"
                print("ERROR: Family: US06:", key[1:-1], ": Divorced", value['Divorced'],
                      "after husband's (", husbandId, ")", "death on", indiDetails[husbandId]['Death'])
            elif indiDetails[wifeId]['Death'] != 'NA' and len(indiDetails[wifeId]['Death']) == 10 and indiDetails[wifeId]['Death'] < value['Divorced']:
                isDivBeforeDeath = "True"
                print("ERROR: Family: US06:", key[1:-1], ": Divorced", value['Divorced'],
                      "after wife's (", wifeId, ")", "death on", indiDetails[wifeId]['Death'])

    return isDivBeforeDeath


def us07_age_lessthan_150(indiDetails):
    isAgeAbove150 = "False"
    today = datetime.datetime.now()
    today = datetime.datetime.strftime(today, '%Y-%m-%d')
    for key, value in indiDetails.items():
        if len(value['Birthday']) == 10 and abs((datetime.datetime.strptime(today, '%Y-%m-%d') - datetime.datetime.strptime(value['Birthday'], '%Y-%m-%d')).days) > (150*365.24):
            isAgeAbove150 = "True"
            print("ERROR: INDIVIDUAL: US07:",
                  key[1:-1], ": More than 150 years old - Birth date", value['Birthday'])
    return isAgeAbove150

def us16_male_last_name(indiDetails, famDetails):
    isLastNameDifferent = "False"
    for key, value in famDetails.items():
        lastName = value['Husband Name'].split('/')[-2].lower()
        for i,cvalue in value["Children"].items():
            childKey = cvalue[1:-1]
            for ikey, ivalue in indiDetails.items():
                if ikey[1:-1] == childKey and ivalue["Gender"] == 'M':
                    cLastName = ivalue['Name'].split('/')[-2].lower()
                    cLastName = cLastName.lower()
                    if cLastName != lastName :
                        isLastNameDifferent = "True"
                        print("ERROR: FAMILY: US16:", key[1:-1], ": has MALE INDIVIDUAL",ikey[1:-1] ,"with a different last name",  
                        cLastName, "than FAMILY last name", lastName)
                        

    return isLastNameDifferent

def us23_sameName_sameBirthDate(indiDetails):
    isNameBirthSame  = "False"
    keyList = []
    for key, value in indiDetails.items():
        for nkey, nvalue in indiDetails.items():
            if(value['Name'] == nvalue['Name'] and value['Birthday'] == nvalue['Birthday'] and key != nkey and key not in keyList):
                isNameBirthSame  = "True"
                keyList.append(nkey)
                print("EEROR: INDIVIDUAL: US23:", nkey[1:-1], "has same name and birthdate as",key[1:-1])
            
        keyList.append(key)        

    return isNameBirthSame


def us24_uniqueFamily_bySpouses(famDetails):
    isSpouseDetailsSame  = "False"
    keyList = []
    for key, value in famDetails.items():
        for nkey, nvalue in famDetails.items():
            if(value['Wife Name'] == nvalue['Wife Name'] and value['Married'] == nvalue['Married'] and key != nkey and key not in keyList):
                isSpouseDetailsSame = "True"
                keyList.append(nkey)
                print("EEROR: FAMILY: US24: Family ", nkey[1:-1], "has same name(",value['Wife Name'],") and marriage date(",value['Married'],") of the spouse as Family",key[1:-1])
            
        keyList.append(key)        

    return isSpouseDetailsSame

def us28_sibilings_byAge(indiDetails, famDetails):
    ordelist = ""
    orderDict = PrettyTable()
    orderDict.field_names = ["Family ID", "Individual Id", "Name", "Birthdate","Age"]
    siblingDetails ={}
    today = datetime.datetime.now()
    today = datetime.datetime.strftime(today, '%Y-%m-%d')
    for key, value in famDetails.items():
        for i,cvalue in value["Children"].items():
            childKey = cvalue[1:-1]
            for ikey, ivalue in indiDetails.items():
                if ikey[1:-1] == childKey:
                    siblingDetails[ikey[1:-1]] ={}
                    siblingDetails[ikey[1:-1]]['Birthday']=ivalue['Birthday']
                    siblingDetails[ikey[1:-1]]['Name']=ivalue['Name']
                    siblingDetails[ikey[1:-1]]['Age']=abs((datetime.datetime.strptime(today, '%Y-%m-%d') - datetime.datetime.strptime(ivalue['Birthday'], '%Y-%m-%d')).days)//365

        
        sorted_keys = OrderedDict(sorted(siblingDetails.items(), key = lambda x: getitem(x[1], 'Age'),reverse=True))          
        for skey, svalue in sorted_keys.items():
            orderDict.add_row([key[1:-1],skey,svalue['Name'],svalue['Birthday'],svalue['Age']])
    
    print(orderDict)
    ordelist = "Ordered"
    return ordelist
# Abhijeet's Section End


# Dinesh's Section Start

def userstory1(indiDetails, familyDetails):

    today = datetime.datetime.now()
    today = datetime.datetime.strftime(today, '%Y-%m-%d')
    list_date = []
    event_list = []
    final_date_list = []
    isDateBeforeToday = "FALSE"
    id_list = []
    for key, value in indiDetails.items():

        if (len(value['Birthday'])) == 10:
            id_list.append(key[1:-1])
            list_date.append(value['Birthday'])
            event_list.append("Birthday")
        if (len(value['Death'])) == 10:
            id_list.append(key[1:-1])
            list_date.append(value['Death'])
            event_list.append("Death")
    for key, value in familyDetails.items():
        id_list.append(key[1:-1])
        if (len(value['Married'])) == 10:
            id_list.append(key[1:-1])
            list_date.append(value['Married'])
            event_list.append("Marriage")
        if (len(value['Divorced'])) == 10:
            id_list.append(key[1:-1])
            list_date.append(value['Divorced'])
            event_list.append("Divorce")

    prettyTable01 = PrettyTable()
    prettyTable01.field_names = ["Today", "Dates", "DatesBeforeCurrentDate"]
    for i in range(len(list_date)):

        if list_date[i] > today:
            final_date_list.append("TRUE")
            isDateBeforeToday = "TRUE"
            if(event_list[i] == "Marriage" or event_list[i] == "Divorce"):
                print("ERROR: FAMILY: US01:",
                      id_list[i], event_list[i], list_date[i], "occurs in future")
            else:
                print("ERROR: INDIVIDUAL: US01:",
                      id_list[i], event_list[i], list_date[i], "occurs in future")
    return isDateBeforeToday


def userstory8(indiDetails, familyDetails):
    # print("\n\n\n User Story 08- Birth before marriage of parents")
    # m = PrettyTable()
    isBirthBeforeMarriage = "NA"
    # marriageDate = "NA"
    # m.field_names=['Name','Birthday','Parent Marriage Date','IsBirthBeforeMarriage']
    for key, value in indiDetails.items():

        if (value['FAMC']) != "NA" and (value['Birthday']) != "NA" and (familyDetails[value['FAMC']]['Married']) != "NA":
            if (familyDetails[value['FAMC']]['Married']) > (value['Birthday']):
                isBirthBeforeMarriage = "TRUE"
                # marriageDate = familyDetails[value['FAMC']]['Married']
                print("ERROR: Family: US08:", " Child ", key[1:-1], "born ", value['Birthday'],
                      "before marriage date on ", familyDetails[value['FAMC']]['Married'])
            else:
                isBirthBeforeMarriage = "FALSE"
                # marriageDate = familyDetails[value['FAMC']]['Married']

        else:
            isBirthBeforeMarriage = "NA"

            # marriageDate = "NA"
        # m.add_row([value['Name'],value['Birthday'],marriageDate,isBirthBeforeMarriage])

    # print(m)
    return isBirthBeforeMarriage


def userstory09(indiDetails, familyDetails):
    # Birth before death of parents

    isBirthBeforeDeath = "NA"
    # print("\n\n\n", indiDetails, "\n\n\n\n", familyDetails)
    for key, value in indiDetails.items():
        if(value['FAMC']) != "NA" and (value['Birthday']) != "NA":
            HId = familyDetails[value['FAMC']]['Husband Id']
            WId = familyDetails[value['FAMC']]['Wife Id']
            if (indiDetails[WId]['Death']) != "NA" or (indiDetails[HId]['Death']) != "NA":
                if((indiDetails[WId]['Death']) > value['Birthday'] and (indiDetails[HId]['Death']) > value['Birthday']):
                    isBirthBeforeDeath = "TRUE"
                else:
                    print("ERROR: INDIVIDUAL: US09:",
                          key[1:-1], ":Birth is After death of Parents")
                    isBirthBeforeDeath = "FALSE"
            else:
                isBirthBeforeDeath = "FALSE"
    return isBirthBeforeDeath


def userstory10(indiDetails, familyDetails):
    # Marriage after 14
    marriageAfter14 = "NA"
    today = datetime.datetime.now()
    today = datetime.datetime.strftime(today, '%Y-%m-%d')

    for key, value in indiDetails.items():
        if len(value['Birthday']) == 10 and value['FAMS'] != "NA" and value['FAMS'] != {}:
            for valueDet in value['FAMS'].values():
                bDate = datetime.datetime.strptime(
                    value['Birthday'], '%Y-%m-%d')

                if valueDet in familyDetails and familyDetails[valueDet]['Married'] != "NA":
                    mDate = datetime.datetime.strptime(
                        familyDetails[valueDet]['Married'], '%Y-%m-%d')
                    if((mDate.year - bDate.year - ((mDate.month, mDate.day) < (bDate.month, bDate.day)) < 14)):
                        marriageAfter14 = "TRUE"
                        print("ERROR: INDIVIDUAL: US10:",
                              key[1:-1], ":Marriage is done before 14 ")

                    else:
                        marriageAfter14 = "FALSE"

    return marriageAfter14


# Dinesh's Section End


# --------End User Stories------------#

if __name__ == '__main__':

    filename1 = "Family.ged"
    filename = "New-Family.ged"
    fam_details, ind_details = file_reading_gen(filename)
    formingPrettyTable(fam_details, ind_details)
    # unittest.main(exit=False, verbosity=2)

    # Calling User Stories
    print("\n\n\n")
    us03_birth_b4_death(ind_details)
    us04_marr_b4_divorce(fam_details)
    US02(ind_details, fam_details)
    US05(ind_details, fam_details)
    userstory1(ind_details, fam_details)
    userstory8(ind_details, fam_details)

    # sprint2
    US15(ind_details, fam_details)
    US18(ind_details, fam_details)
    userstory09(ind_details, fam_details)
    userstory10(ind_details, fam_details)
    us06_div_b4_death(ind_details, fam_details)
    us07_age_lessthan_150(ind_details)

    #sprint3
    us16_male_last_name(ind_details, fam_details)
    us23_sameName_sameBirthDate(ind_details)
