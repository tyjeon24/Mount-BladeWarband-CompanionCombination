from itertools import combinations

# 11 or more companion is impossible according to the calculation.
NUMBER_OF_COMPANIONS = 10

########################################################################
# Make relationship table.
# Example) Alayen
# Alayen likes Ymira : relationships_dict["Alayen"]["Ymira"] = 1
# Alayen dislikes Marnid : relationships_dict["Alayen"]["Marnid"] = -1
# Alayen dislikes Nizar : relationships_dict["Alayen"]["Nizar"] = -1
relationships_dict = {
    "Alayen": {"Ymira": 1, "Marnid": -1, "Nizar": -1},
    "Artimenner": {"Lezalit": 1, "Jeremus": -1, "Klethi": -1},
    "Baheshtur": {"Rolf": 1, "Katrin": -1, "Marnid": -1},
    "Borcha": {"Marnid": 1, "Deshavi": -1, "Klethi": -1},
    "Bunduk": {"Katrin": 1, "Lezalit": -1, "Rolf": -1},
    "Deshavi": {"Klethi": 1, "Borcha": -1, "Rolf": -1},
    "Firentis": {"Jeremus": 1, "Nizar": -1, "Katrin": -1},
    "Jeremus": {"Firentis": 1, "Artimenner": -1, "Matheld": -1},
    "Katrin": {"Bunduk": 1, "Firentis": -1, "Baheshtur": -1},
    "Klethi": {"Deshavi": 1, "Borcha": -1, "Artimenner": -1},
    "Lezalit": {"Artimenner": 1, "Ymira": -1, "Bunduk": -1},
    "Marnid": {"Borcha": 1, "Alayen": -1, "Baheshtur": -1},
    "Matheld": {"Nizar": 1, "Ymira": -1, "Jeremus": -1},
    "Nizar": {"Matheld": 1, "Firentis": -1, "Alayen": -1},
    "Rolf": {"Baheshtur": 1, "Deshavi": -1, "Bunduk": -1},
    "Ymira": {"Alayen": 1, "Matheld": -1, "Lezalit": -1},
}


########################################################################
# Calculate relationship value.
# Check all the companion's relationship value is positive or 0.
def check_possible_combination(number):
    for hero_combination in list(combinations(relationships_dict.keys(), number)):
        calculation_log = "Calculation : \n"
        for companion in hero_combination:
            relationship_value = 0
            calculation_log += f"\t{companion} "
            for target in hero_combination:
                if relationships_dict[companion].get(target) == 1:
                    calculation_log += f"likes {target}(+1) "
                if relationships_dict[companion].get(target) == -1:
                    calculation_log += f"dislikes {target}(-1) "
                relationship_value += relationships_dict[companion].get(target, 0)
            calculation_log += f"= {relationship_value}\n"
            if relationship_value < 0:
                break
        else:
            print(f"Possible companion combination : {hero_combination}")
            print(calculation_log)


check_possible_combination(NUMBER_OF_COMPANIONS)
