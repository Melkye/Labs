import experts

expert_1_evaluation = [
    [1, 0.1, 0.7, 8],
    [0.9, 1, 0.5, 0.6],
    [0.7, 0.1, 1, 0.9],
    [0.6, 0, 0.3, 1]
]

R_s = experts.get_R_s(expert_1_evaluation)
print("R_s:")
for line in R_s:
    for element in line:
        print('%1.1f' % round(element, 6), end=" ")
    print()

print()

mu_nd = experts.get_mu_nd(R_s)

print("mu_nd:")
for element in mu_nd:
    print('%1.1f' % round(element, 6), end=" ")

print()
print()

best = experts.select_best(mu_nd)
print(f"the best is №{best}")
