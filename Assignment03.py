# Dictionary
li = {"0": ["INDI", "FAM", "HEAD", "TRLR", "NOTE"], "1": ["NAME", "SEX", "BIRT",
                                                          "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"], "2": ["DATE"]}
#imports
import json
import datetime

ind_details = {}
fam_details = {}
# gedcom parser


def initialize_var(individual_id,name,sex,birt,deat,fams,famc,fam,marr,husb,wife,chil,div,date,fs):
    
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
    chil = ""
    div = ""
    date = ""
    fs = 1
    #fc = 1
     # idcount = 0
    return individual_id,name,sex,birt,deat,fams,famc,fam,marr,husb,wife,chil,div,date,fs


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
    # fc = 1
    famc = ""
    fams = {}
    fam = ""
    marr = ""
    husb = ""
    wife = ""
    chil = ""
    div = ""
    date = ""
    idcount = 0
    # initialize_var()
    for line in file:
        #print("-->",line.strip("\n"))
        liner = line.split()
        #print(liner)

        if liner[0] in ["0", "1", "2"]:
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
                            fkey=(' '.join(liner[2::]))[1:-1]
                            # print("---------------------------------")
                            # fam_details[fkey]={'Married':'','Divorced':'','Husband ID':'','Husband Name':'','Wife ID':'','Wife Name':'','Children':''}
                            fam_details[fkey]={'ID':fkey}
                            #print(fam_details)
                            #print(fams)
                        elif liner[1] == "FAMC":
                            famc = (' '.join(liner[2::]))
                            # fc = fc + 1
                            # print(famc)
                        elif liner[1] == "HUSB":
                            husb = ' '.join(liner[2::])
                            #fam_details[fkey]['Husband ID']=husb
                            #print(husb)
                        elif liner[1] == "WIFE":
                            wife = ' '.join(liner[2::])
                            #fam_details[fkey]['Wife ID']= wife
                            #print(wife)
                        elif liner[1] == "CHIL":
                            chil = ' '.join(liner[2::])
                            # print(chil)
                        elif liner[1] == "BIRT":
                            bcount = True
                        elif liner[1] == "DEAT":
                            dcount = True
                        elif liner[1] == "MARR":
                            marrcount = True
                        elif liner[1] == "DIV":
                            divcount = True
                        elif liner[1] == "DATE":
                            if bcount == True:
                                birt = ' '.join(liner[2::])
                                birt = datetime.datetime.strptime(birt,'%d %b %Y').strftime('%Y-%m-%d')
                                
                            if dcount == True:
                                deat = ' '.join(liner[2::])
                                deat = datetime.datetime.strptime(deat, '%d %b %Y').strftime('%Y-%m-%d')
                                #print(deat)
                            if marrcount == True:
                                marr = ' '.join(liner[2::])
                            if divcount == True:
                                div = ' '.join(liner[2::])
                            # print(birt, deat, marr, div)

                    elif len(liner) > 2 and (liner[2] in ["INDI", "FAM"]):
                        # pass
                        # print("<--", liner[0], sep, liner[2], sep, "Y",sep, liner[1], sep, ' '.join(liner[3::]))
                        bcount = False
                        dcount = False
                        marrcount = False
                        divcount = False
                        if idcount == 1:
                                ind_details[individual_id] = {"Name": name, 'Gender': sex, 'Birthday': birt, 'Death': deat, 'FAMS': fams, 'FAMC': famc}
                                if(sex == 'F'):
                                    fam_details[fkey]['Wife name']=name
                                else:
                                    fam_details[fkey]['Husband name']=name
                        # print(liner)
                        if liner[2] == "INDI":
                            # if idcount == 1:
                            #     ind_details[individual_id] = {"Name": name, 'Gender': sex, 'Birthday': birt, 'Death': deat, 'FAMS': fams, 'FAMC': famc}
                            #     if(sex == 'F'):
                            #         fam_details[fkey]['Wife name']=name
                            #     else:
                            #         fam_details[fkey]['Husband name']=name
                                #print(marr)

                            #print(ind_details,"----------------------------------------------")
                            individual_id,name,sex,birt,deat,fams,famc,fam,marr,husb,wife,chil,div,date,fs=initialize_var(individual_id,name,sex,birt,deat,fams,famc,fam,marr,husb,wife,chil,div,date,fs)
                            individual_id = liner[1]
                            #print(individual_id)
                            idcount = 1
                        elif liner[2] == "FAM":
                            # print(liner[1])
                            fam = liner[1]

                    else:
                        # print("<--",liner[0],sep,liner[1],sep,"N",sep,' '.join(liner[2::]))
                        pass
        else:
            # print("<--",liner[0],sep,liner[1],sep,"N",sep,' '.join(liner[2::]))
            pass


# function calling
file_reading_gen("Family.ged")
print(fam_details)

#pretty table
from prettytable import PrettyTable
    
x = PrettyTable()

x.field_names = ["ID", "Name", "Gender", "Birthday","Age","Alive","Death","Child","Spouse"]

for key,value in ind_details.items():
    #alive or not
    if value['Death'] == 'NA' : 
        alive = 'True' 
    else:
        alive = 'False'
    age = calcAge(value['Birthday'])
   
    #FAMC
    if value['FAMC'] == 'NA' :
        fc= 'NA'
    else:
        fc= "{'"+ value['FAMC'][1:-1]+"'}"
       
    #FAMS
    if value['FAMS'] == {} :
        sf= 'NA'
    else:
        sf = value['FAMS']   
        sf = list(sf.values())   #converts the list  
        sf = [s.replace('@', '') for s in sf]   #strips @ from id
        sf=set(sf)  #convert to set
    #add rows
    x.add_row([key[1:-1],value['Name'],value['Gender'],value['Birthday'],age,alive,value['Death'],fc,sf])

#print result
print("\n\n\n Individuals")
print(x)
