import pandas as pd
import numpy as np

def find_parameters(filename):

    # выгрузка данных
    dataDF = pd.read_excel('usa.xls')
    dataDF = dataDF.rename(columns=dataDF.iloc[0])
    dataDF = dataDF.rename(columns={'Год': 'year', 'ВВП(млн.$)': 'gdp', 'K(млн.$)': 'capital', 'L(тыс.чел.)': 'labour'})
    dataDF = dataDF.iloc[1:]

    # загружаем данные в массивы
    gdp_data = dataDF['gdp'].to_numpy().astype(float)
    capital_data = dataDF['capital'].to_numpy().astype(float)
    labour_data = dataDF['labour'].to_numpy().astype(float)

    # получаем логарифмы данных
    log_gdp = np.log(gdp_data)
    log_capital = np.log(capital_data)
    log_labour = np.log(labour_data)

    # суммируем каждый массив
    total_log_gdp = np.sum(log_gdp)
    total_log_capital = np.sum(log_capital)
    total_log_labour = np.sum(log_labour)

    # перемножаем и суммируем массивы
    total_log_capital_log_capital = np.sum(log_capital*log_capital)
    total_log_labour_log_labour = np.sum(log_labour*log_labour)
    total_log_capital_log_labour = np.sum(log_capital*log_labour)
    total_log_capital_log_gdp = np.sum(log_capital*log_gdp)
    total_log_labour_log_gdp = np.sum(log_labour*log_gdp)

    # решаем систему уравнений
    matrix = [[len(gdp_data), total_log_capital, total_log_labour],
              [total_log_capital, total_log_capital_log_capital, total_log_capital_log_labour],
              [total_log_labour, total_log_capital_log_labour, total_log_labour_log_labour]]
    vector = [total_log_gdp, total_log_capital_log_gdp, total_log_labour_log_gdp]
    inverse = np.linalg.inv(matrix)

    return np.dot(inverse, vector)


result = find_parameters('usa.xls')
print('Параметр А:', result[0])
print('Параметр альфа:', result[1])
print('Параметр бета:', result[2])
