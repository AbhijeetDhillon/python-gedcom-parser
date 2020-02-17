
# Dictionary
li = {"0": ["INDI", "FAM", "HEAD", "TRLR", "NOTE"], "1": ["NAME", "SEX", "BIRT","DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"], "2": ["DATE"]}

ind_details = {}

# gedcom parser
def file_reading_gen(path, sep):
    file = open(path, "r")
    for line in file:
        # print("-->",line.strip("\n"))
        liner = line.split()
        individual_id = ""
        name = ""
        sex = ""
        birt = ""
        deat = ""
        famc = []
        fams = []
        fam = ""
        marr = ""
        husb = ""
        wife = ""
        chil = ""
        div = ""
        date = ""
        idcount=0
        if liner[0] in ["0", "1", "2"]:
            for key, values in li.items():

                if liner[0] == key:
                    if liner[1] in values and liner[1] not in ["INDI", "FAM"]:
                        # print("<--", liner[0], sep, liner[1],sep, "Y", sep, ' '.join(liner[2::]))
                        # print(' '.join(liner[2::]))
                        if liner[1] == "NAME":
                            name = (' '.join(liner[2::]))
                            print(name)
                        elif liner[1] == "SEX":
                            sex = (' '.join(liner[2::]))
                            print(sex)
                        elif liner[1] == "FAMS":
                            fams.append(' '.join(liner[2::]))
                            print(fams)
                        elif liner[1] == "FAMC":
                            famc.append(' '.join(liner[2::]))
                            print(famc)
                        elif liner[1] == "HUSB":
                            husb = ' '.join(liner[2::])
                            print(husb)
                        elif liner[1] == "WIFE":
                            wife = ' '.join(liner[2::])
                            print(wife)
                        elif liner[1] == "CHIL":
                            chil = ' '.join(liner[2::])
                            print(chil)
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
                            elif dcount == True:
                                deat = ' '.join(liner[2::])
                            elif marrcount == True:
                                marr = ' '.join(liner[2::])
                            elif divcount == True:
                                div = ' '.join(liner[2::])
                            print(birt,deat,marr,div)

                    elif len(liner) > 2 and (liner[2] in ["INDI", "FAM"]):
                        # pass
                        # print("<--", liner[0], sep, liner[2], sep, "Y",sep, liner[1], sep, ' '.join(liner[3::]))
                        bcount = False
                        dcount = False
                        marrcount = False
                        divcount = False
                        # print(liner)
                        if liner[2] == "INDI":
                            # if idcount == "1":
                            # print(name)
                            ind_details[id] = {"ID":individual_id,"Name":name,'Gender':sex,'Birthday':birt,'Death':deat,'FAMS':fams,'FAMC':famc}
                            individual_id = liner[1]
                            # print(individual_id)
                            idcount = 1
                        else:
                            fam = liner[1]

                    else:
                        # print("<--",liner[0],sep,liner[1],sep,"N",sep,' '.join(liner[2::]))
                        pass
        else:
            # print("<--",liner[0],sep,liner[1],sep,"N",sep,' '.join(liner[2::]))
            pass



# function calling
file_reading_gen("D:\Assgnments\CS 555\Assignment 3\Family.ged", "|")
print(ind_details)
