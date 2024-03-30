from xlsx_parse import *
from operations import *
from alpha_level import *
from relations import *
from rank import *
from print import *
from many_exp_solution import *

exp_1=expert_data[1]
print("\nЕксперт 1:")
print_matrix(exp_1)

exp_2=expert_data[2]
print("\nЕксперт 2:")
print_matrix(exp_2)

print("\nОперація об'єднання:")
print_matrix(fuzzy_union(exp_1, exp_2))
print("\nОперація перетину:")
print_matrix(fuzzy_intersection(exp_1, exp_2))
print("\nОперація доповнення для матриці НВ експерта 1:")
print_matrix(fuzzy_complement(exp_1))
print("\nОперація доповнення для матриці НВ експерта 2:")
print_matrix(fuzzy_complement(exp_2))
print("\nКомпозиція матриць НВ для експертів 1 та 2:")
print_matrix(fuzzy_composition(exp_1, exp_2))

print("\nAlpha рівень матриці для експерта 1:")
alpha=0.5
print("\nAlpha рівень для", alpha, ":")
print(alpha_cut(exp_1, alpha))
alpha=0.9
print("\nAlpha рівень для", alpha, ":")
print(alpha_cut(exp_1, alpha))

print("\nВідношення для матриці експерта 1:")
print("Матриця НВ експерта 1:")
print_matrix(exp_1)

print("\nВідношення строгої переваги:")
strict_exp_1=strict_preference_relation(exp_1)
print_matrix(strict_exp_1)

print("\nВідношення байдужості:")
print_matrix(indifference_relation(exp_1))

print("\nВідношення квазіеквівалентності:")
print_matrix(quasi_equivalence_relation(exp_1))

exp_1_solution=max_col(strict_exp_1)
print("\nРішення:")
print_set(exp_1_solution)
print("\nРанжування:")
print_rank(rank_list(exp_1_solution))

print("\nДля 5 експертів:")
print("\nЗгортка P:")
P_sol=P_solution(expert_data)
print_matrix(P_sol)
strict_P=strict_preference_relation(P_sol)
print("\nСтрога перевага P:")
print_matrix(strict_P)
P_solution=max_col(strict_P)
print("\nРішення для P:")
print_set(P_solution)

print("\nЗгортка Q:")
Q_sol=Q_solution(expert_data,coefs)
print_matrix(Q_sol)
strict_Q=strict_preference_relation(Q_sol)
print("\nСтрога перевага Q:")
print_matrix(strict_Q)
Q_solution=max_col(strict_Q)
print("\nРішення для Q:")
print_set(Q_solution)
print("\nПеретин отриманих множин:")
print_set(fuzzy_intersection(P_solution,Q_solution))
print("\nРанжування:")
print_rank(rank_list(fuzzy_intersection(P_solution,Q_solution)))

