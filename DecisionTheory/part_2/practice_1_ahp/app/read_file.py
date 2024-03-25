experts = 4
criteria_num = 6
alternatives_num = 7

mpp_experts = []

# First expert
mpp_criteria_1_Expert = []

mpp_alternatives_1_Criteria_1_Expert = []
mpp_alternatives_2_Criteria_1_Expert = []
mpp_alternatives_3_Criteria_1_Expert = []
mpp_alternatives_4_Criteria_1_Expert = []
mpp_alternatives_5_Criteria_1_Expert = []
mpp_alternatives_6_Criteria_1_Expert = []

# Second expert
mpp_criteria_2_Expert = []

mpp_alternatives_1_Criteria_2_Expert = []
mpp_alternatives_2_Criteria_2_Expert = []
mpp_alternatives_3_Criteria_2_Expert = []
mpp_alternatives_4_Criteria_2_Expert = []
mpp_alternatives_5_Criteria_2_Expert = []
mpp_alternatives_6_Criteria_2_Expert = []

# Third expert
mpp_criteria_3_Expert = []

mpp_alternatives_1_Criteria_3_Expert = []
mpp_alternatives_2_Criteria_3_Expert = []
mpp_alternatives_3_Criteria_3_Expert = []
mpp_alternatives_4_Criteria_3_Expert = []
mpp_alternatives_5_Criteria_3_Expert = []
mpp_alternatives_6_Criteria_3_Expert = []

# Forth expert
mpp_criteria_4_Expert = []

mpp_alternatives_1_Criteria_4_Expert = []
mpp_alternatives_2_Criteria_4_Expert = []
mpp_alternatives_3_Criteria_4_Expert = []
mpp_alternatives_4_Criteria_4_Expert = []
mpp_alternatives_5_Criteria_4_Expert = []
mpp_alternatives_6_Criteria_4_Expert = []

with open("var_1.txt", "r", encoding="utf8") as file:
    contents = file.readlines()
    expert_start_file_indices = [i for i, x in enumerate(
        contents) if "_______________" in x]

# Write to mpp_experts
for i in range(experts):
    mpp_experts.append([float(num) for num in contents[2+i].split()])

# Write to all other
for index in expert_start_file_indices:
    if mpp_criteria_1_Expert == []:
        for crit_num in range(criteria_num):
            mpp_criteria_1_Expert.append(
                [float(num) for num in contents[index+crit_num+1].split()])

        for alt_num in range(alternatives_num):
            mpp_alternatives_1_Criteria_1_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num].split()])
            mpp_alternatives_2_Criteria_1_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num + alternatives_num + 1].split()])
            mpp_alternatives_3_Criteria_1_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num + (alternatives_num + 1)*2].split()])
            mpp_alternatives_4_Criteria_1_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num + (alternatives_num + 1)*3].split()])
            mpp_alternatives_5_Criteria_1_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num + (alternatives_num + 1)*4].split()])
            mpp_alternatives_6_Criteria_1_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num + (alternatives_num + 1)*5].split()])

    elif mpp_criteria_2_Expert == []:
        for crit_num in range(criteria_num):
            mpp_criteria_2_Expert.append(
                [float(num) for num in contents[index + crit_num + 1].split()])

        for alt_num in range(alternatives_num):
            mpp_alternatives_1_Criteria_2_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num].split()])
            mpp_alternatives_2_Criteria_2_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num + alternatives_num + 1].split()])
            mpp_alternatives_3_Criteria_2_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num + (alternatives_num + 1) * 2].split()])
            mpp_alternatives_4_Criteria_2_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num + (alternatives_num + 1) * 3].split()])
            mpp_alternatives_5_Criteria_2_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num + (alternatives_num + 1) * 4].split()])
            mpp_alternatives_6_Criteria_2_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num + (alternatives_num + 1) * 5].split()])

    elif mpp_criteria_3_Expert == []:
        for crit_num in range(criteria_num):
            mpp_criteria_3_Expert.append(
                [float(num) for num in contents[index + crit_num + 1].split()])

        for alt_num in range(alternatives_num):
            mpp_alternatives_1_Criteria_3_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num].split()])
            mpp_alternatives_2_Criteria_3_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num + alternatives_num + 1].split()])
            mpp_alternatives_3_Criteria_3_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num + (alternatives_num + 1) * 2].split()])
            mpp_alternatives_4_Criteria_3_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num + (alternatives_num + 1) * 3].split()])
            mpp_alternatives_5_Criteria_3_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num + (alternatives_num + 1) * 4].split()])
            mpp_alternatives_6_Criteria_3_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num + (alternatives_num + 1) * 5].split()])

    elif mpp_criteria_4_Expert == []:
        for crit_num in range(criteria_num):
            mpp_criteria_4_Expert.append(
                [float(num) for num in contents[index + crit_num + 1].split()])

        for alt_num in range(alternatives_num):
            mpp_alternatives_1_Criteria_4_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num].split()])
            mpp_alternatives_2_Criteria_4_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num + alternatives_num + 1].split()])
            mpp_alternatives_3_Criteria_4_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num + (alternatives_num + 1) * 2].split()])
            mpp_alternatives_4_Criteria_4_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num + (alternatives_num + 1) * 3].split()])
            mpp_alternatives_5_Criteria_4_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num + (alternatives_num + 1) * 4].split()])
            mpp_alternatives_6_Criteria_4_Expert.append(
                [float(num) for num in contents[index + criteria_num + 2 + alt_num + (alternatives_num + 1) * 5].split()])
