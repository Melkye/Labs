import pandas as pd
import numpy as np


# Функція для пошуку початковох клітинки в файлі
def find_cell_by_value(file_path, target_value):
    # Завантажуємо ексель файл в датафрейм
    df = pd.read_excel(file_path, header=None)
    # Шукаємо потрібне значення в датафреймі
    result = (df == target_value).stack()
    # Повертаємо координати знайденого значення
    row, col = result[result].index[0]

    return df, row + 1, col + 1  # Повертаємо файл і координати


def extract_table(df, start_row, start_col):
    # Витягаємо матрицю розмірністю 6х6, починаючи зі стартової координати
    table = df.iloc[start_row-1:start_row+5, start_col-1:start_col+5]
    table_matrix = table.to_numpy()  # Переганяємо пандас-датафрейм в матрицю

    return table_matrix  # Повертаємо матрицю


def extract_expert_data(df, start_row, start_col):
    # Витягаємо дані всіх експертів починаючи з початкової клітинки
    expert_data = {}
    for i in range(5):
        expert_data[i + 1] = extract_table(df,
                                           start_row, start_col + 3 + i * 8)

    coefs = [round(df.at[start_row + 6, start_col + 2 + i * 8], 9)
             for i in range(5)]

    return expert_data, coefs  # Повертаємо матриці експертів і коефіцієнти


# if __name__ == "__main__":
df, start_row, start_col = find_cell_by_value("Variants.xlsx", "ВАР 1")
expert_data, coefs = extract_expert_data(df, start_row, start_col)
