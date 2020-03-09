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
    

    return fam_details,ind_details