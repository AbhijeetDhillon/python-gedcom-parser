# Dictionary
li = {"0": ["INDI", "FAM", "HEAD", "TRLR", "NOTE"], "1": ["NAME", "SEX", "BIRT",
                                                          "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"], "2": ["DATE"]}


ind_details = {}

# gedcom parser


def initialize_var():
    individual_id = ""
    name = ""
    sex = ""
    birt = ""
    deat = ""
    # famc = []
    # fams = []
    fam = ""
    marr = ""
    husb = ""
    wife = ""
    chil = ""
    div = ""
    date = ""
    fs = 1
    fc = 1
    # idcount = 0


def file_reading_gen(path):
    file = open(path, "r")
    individual_id = ""
    name = ""
    sex = ""
    birt = ""
    deat = ""
    fs = 1
    fc = 1
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
        # print("-->",line.strip("\n"))
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
                            #print(fams)
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
                            if dcount == True:
                                deat = ' '.join(liner[2::])
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
                        # print(liner)
                        if liner[2] == "INDI":
                            if idcount == 1:
                                ind_details[individual_id] = {"Name": name, 'Gender': sex, 'Birthday': birt, 'Death': deat, 'FAMS': fams, 'FAMC': famc}
                            #print(ind_details,"----------------------------------------------")
                            initialize_var()
                            fams={}
                            # famc={}
                            fs = 1
                            fc = 1
                            individual_id = liner[1]
                            #print(individual_id)
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
file_reading_gen("Family.ged")
print(ind_details)

