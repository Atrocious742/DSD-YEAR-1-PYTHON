def lab_results_unit_cover():
    def typeTest():
        test = input("what test type you have: ")
        if test == "glucose":
            print("type 1 for mg/dl")
            print("type 2 for mmol/L")
            glucose()
        elif test == "cholesterol":
            print("type 1 for mg/dl")
            print("type 2 for mmol/L")
            cholesterol()
        else:
            print("try again")
            typeTest()

    def glucose():
        glucosecheck = int(input("what unit do you want to convert to?"))
        if glucosecheck == 1:
            glu = int(input("how much glucose do you want to enter in mg/dl: "))
            glu_tot = glu * 18
            print("total glucose is", glu_tot)
            typeTest()
        elif glucosecheck == 2:
            ulg = int(input("how much glucose do you want to enter in mmol/L"))
            ulg_tot = ulg / 18 
            print("total glucose is", ulg_tot)
            typeTest()
        else:
            print("INVALID INPUT!")
            glucose()

    def cholesterol():
        cholesterol_check = int(input("what unit do you want to convert to?"))
        if cholesterol_check == 2:
            cho = int(input("how much cholesterol do you want to enter in mg/dl: "))
            cho_tot = cho * 18
            print("total cholesterol is", glu_tot)
            typeTest()
        elif cholesterol_check == 2:
            ohc = int(input("how much cholesterol do you want to enter in mmol/L"))
            ohc_tot = ohc / 18 
            print("total cholesterol is", ohc_tot)
            typeTest()
        else:
            print("INVALID INPUT!")
            cholesterol()
    typeTest()        
lab_results_unit_cover()