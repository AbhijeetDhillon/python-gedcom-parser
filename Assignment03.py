# Dictionary
import dateutil.parser as dparser
from datetime import datetime
import dateutil.parser
import datetime
import json
import fileinput

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
    

def file_reading_gen(path):
    file = open(path, "r")
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
    # initialize_var()
    for line in file:
        # print("-->",line.strip("\n")) 
        liner = line.split()
        # print(liner[0])


        if(liner == []):
            continue

        elif liner[0] in ["0", "1", "2"]:
            for key, values in li.items():

                if liner[0] == key:
                    if liner[1] in values and liner[1] not in ["INDI", "FAM"]:
                        # print("<--", liner[0], sep, liner[1],sep, "Y", sep, ' '.join(liner[2::]))
                        # print(' '.join(liner[2::]))
                        if liner[1] == "NAME":
                            name = (' '.join(liner[2::]))
                            # print(name)
                        elif liner[1] == "SEX":
                            sex = (' '.join(liner[2::]))
                            # print(sex)
                        elif liner[1] == "FAMS":
                            fams[fs]=(' '.join(liner[2::]))
                            fs = fs + 1
                            # print("---------------------------------")
                            # print(fam_details)
                            # print(fams)
                        elif liner[1] == "FAMC":
                            famc = (' '.join(liner[2::]))
                            # fc = fc + 1
                            # print(famc)
                        elif liner[1] == "HUSB":
                            husb = ' '.join(liner[2::])
                            # print(husb)
                        elif liner[1] == "WIFE":
                            wife = ' '.join(liner[2::])
                            # print(wife)
                        elif liner[1] == "CHIL":
                            chil[cs] = (' '.join(liner[2::]))
                            cs = cs+1

                            # print(chil)
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
                                # if(deat == "NA"):
                                #     deat = "dead"
                                dcount = False
                            if marrcount == True:
                                marr = ' '.join(liner[2::])
                                marr = dateCalc(marr)
                                marrcount = False
                                # print("marr"+marr)
                            if divcount == True:
                                div = ' '.join(liner[2::])
                                div = dateCalc(div)
                                divcount = False
                                # print("div"+div)
                            # print(birt, deat, marr, div)

                    elif (liner[0] == '0' and liner[2] in ["INDI", "FAM"]):
                            # pass
                            # print(liner[1])
                            # print("<--", liner[0], sep, liner[2], sep, "Y",sep, liner[1], sep, ' '.join(liner[3::]))
                            bcount = False
                            dcount = False
                            marrcount = False
                            divcount = False
                            if idcount == 1:
                                ind_details[individual_id] = {"Name": name, 'Gender': sex, 'Birthday': birt, 'Death': deat, 'FAMS': fams, 'FAMC': famc}
                                    # if(sex == 'F'):
                                    #     fam_details[fkey]['Wife name']=name
                                    # else:
                                    #     fam_details[fkey]['Husband name']=name
                            if fcount ==1:
                                fam_details[fam] = {"Married": marr, 'Divorced': div, 'Husband Id': husb, 'Husband Name': ind_details.get(husb,{}).get('Name'), 'Wife Id': wife, 'Wife Name':ind_details.get(wife,{}).get('Name'),'Children':chil }

                            # print(liner)
                            if liner[2] == "INDI":
                                # if idcount == 1:
                                #     ind_details[individual_id] = {"Name": name, 'Gender': sex, 'Birthday': birt, 'Death': deat, 'FAMS': fams, 'FAMC': famc}
                                #     if(sex == 'F'):
                                #         fam_details[fkey]['Wife name']=name
                                #     else:
                                #         fam_details[fkey]['Husband name']=name
                                    # print(marr)

                                # print(ind_details,"----------------------------------------------")
                                individual_id,name,sex,birt,deat,fams,famc,fam,marr,husb,wife,chil,div,date,fs=initialize_var(individual_id,name,sex,birt,deat,fams,famc,fam,marr,husb,wife,chil,div,date,fs)
                                individual_id = liner[1]
                                # print(individual_id)
                                idcount = 1
                            elif liner[2] == "FAM":
                                # print(liner[1])
                                # individual_id,name,sex,birt,deat,fams,famc,fam,marr,husb,wife,chil,div,date,fs=initialize_var(individual_id,name,sex,birt,deat,fams,famc,fam,marr,husb,wife,chil,div,date,fs)
                                # print(ind_details.get(husb,{}).get('Name'))
                            

                                
                                
                                marr,div,husb,wife,chil = 'NA','NA',0,0,{}
                                fam = liner[1]
                                # ind_details[fam] = {"Name": name, 'Gender': sex, 'Birthday': birt, 'Death': deat, 'FAMS': fams, 'FAMC': famc}
                                fcount = 1

                    elif((liner[1] in ["_CURRENT"])):
                        fcount = fam_details[fam] = {"Married": marr, 'Divorced': div, 'Husband Id': husb, 'Husband Name': ind_details.get(husb,{}).get('Name'), 'Wife Id': wife, 'Wife Name':ind_details.get(wife,{}).get('Name'),'Children':chil }

                        # print(liner[1])
                        # trlr = True
                        # print("<--",liner[0],sep,liner[1],sep,"N",sep,' '.join(liner[2::]))
                        # pass
        else:
            # print(liner[1])
            # print("<--",liner[0],sep,liner[1],sep,"N",sep,' '.join(liner[2::]))
            pass


# function calling
# file_reading_gen("000.ged")
filename1="000.ged"
filename="Keanu_Reeves_Family.ged"
file_reading_gen(filename1)
# print(fam_details)


# for x in fam_details.items():
#     print(x)

# for x in ind_details.items():
#     print(x)

# pretty table
from prettytable import PrettyTable
    
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
    # print(value['Children'])
    if value['Children'] == {} :
        ch = "NA"
        # ch = set(ch)
    else:
        ch = value['Children']   
        ch = list(ch.values())   #converts the list  
        ch = [s.replace('@', '') for s in ch]   #strips @ from id
        # print(ch)
        ch=set(ch)  #convert to set
        # print(ch)
    x2.add_row([key[1:-1],value['Married'],value['Divorced'],value['Husband Id'][1:-1],value['Husband Name'],value['Wife Id'][1:-1],value['Wife Name'],ch])

# print result
print("\n\n\n Individuals")
print(x)
print("\n\n\n  Family")
print(x2)
