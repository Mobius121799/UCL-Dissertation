import json

import numpy as np
import matplotlib.pyplot as plt
import csv

# test_dict = {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
# with open("T_CP0.json","w") as f:
#     json.dump(test_dict, f)
# [298.15, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000]
# [298.15, 300, 400, 500, 600, 700, 800, 900, 1000]
R = 8.314510
name_of_molecule = 'H2'
T_lower = np.array([298.15, 300.0, 350.0, 400.0, 450.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0])
y_lower = np.array([28.836, 28.849, 29.081, 29.181, 29.229, 29.26, 29.327, 29.441, 29.624, 29.881, 30.205])
T_lower_list = T_lower.tolist()
T = np.arange(1000, 6100, 100)
y = np.array([30.205, 30.581, 30.992, 31.423, 31.861, 32.298, 32.725, 33.139, 33.537, 33.917, 34.28, 34.624, 34.952, 35.263, 35.559, 35.842, 36.111, 36.37, 36.618, 36.856, 37.087, 37.311, 37.528, 37.74, 37.946, 38.149, 38.348, 38.544, 38.738, 38.928, 39.116, 39.301, 39.484, 39.665, 39.842, 40.017, 40.188, 40.355, 40.518, 40.676, 40.829, 40.976, 41.117, 41.252, 41.379, 41.498, 41.609, 41.712, 41.806, 41.89, 41.965])
T_list = T.tolist()
print(T_lower)

y_lower_list = y_lower.tolist()

y_list = y.tolist()
if y_list != []:
    # with open("T_CP0.json", 'r') as load_f:
    #     load_dict = json.load(load_f)
    # load_dict[name_of_molecule] = [T_lower_list, y_lower_list, T_list, y_list]
    #
    # with open("T_CP0.json", "w") as dump_f:
    #     json.dump(load_dict, dump_f)

    CP0_lower = (np.multiply(np.multiply(T_lower, y_lower), T_lower)) / R
    z1_lower = np.polyfit(T_lower, CP0_lower, 6)
    p1_lower = np.poly1d(z1_lower)
    print(CP0_lower)
    print(p1_lower)
    yvals_lower = ((p1_lower(T_lower) / T_lower) / T_lower) * R
    z1_lower = z1_lower.tolist()
    z1_lower = [str(i) for i in z1_lower]
    z1_lower.insert(0, '298.15-1000')
    z1_lower.insert(0, name_of_molecule)
    print(z1_lower)

    CP0 = (np.multiply(np.multiply(T, y), T)) / R
    z1 = np.polyfit(T, CP0, 6)
    p1 = np.poly1d(z1)
    print(CP0)
    print(p1)
    print(type(p1))
    yvals = ((p1(T) / T) / T) * R
    print(type(yvals))
    z1 = z1.tolist()
    z1 = [str(i) for i in z1]
    z1.insert(0, '1000-6000')
    z1.insert(0, name_of_molecule)
    print(z1)

    # header = ['name_of_gas','temperature scope', 'a7', 'a6', 'a5', 'a4', 'a3', 'a2', 'a1']
    # with open('nasa_polynomials.csv', 'w', encoding='utf-8', newline='') as nasa_poly_lower:
    #     writer = csv.writer(nasa_poly_lower)
    #     writer.writerow(header)

    # with open('nasa_polynomials.csv', 'a+', encoding='utf-8', newline='') as nasa_poly_lower:
    #     writer = csv.writer(nasa_poly_lower)
    #     writer.writerow(z1_lower)
    #     writer.writerow(z1)

    fig, (axes1, axes2) = plt.subplots(1, 2, figsize=(15, 5))
    plt.subplots_adjust(wspace=0.5, hspace=0)
    # plot 298.15-1000
    axes1.plot(T_lower, yvals_lower, 'r', label='polyfit values')
    axes1.scatter(T_lower, y_lower, label='original values')
    axes1_residual = axes1.twinx()
    # residual = np.maximum((yvals_lower - y_lower), - (yvals_lower - y_lower))
    residual_lower = yvals_lower - y_lower
    residual_lower_std = np.std(residual_lower, ddof=1)
    print('The standard deviation of residuals in 298.15-1000K is ' + str(residual_lower_std))
    axes1_residual.plot(T_lower, residual_lower, 'b', label='residual')
    axes1.set_xlabel('T(K)')
    axes1.set_ylabel('CP0_lower')
    axes1_residual.set_ylabel('Residual')
    axes1.legend(loc=2)
    axes1_residual.legend(loc=0)
    axes1.set_title('poly_fitting 298.15-1000', fontsize='small')
    # plot 1000-6000
    axes2.plot(T, yvals, 'r', label='polyfit values')
    axes2.scatter(T, y, label='original values')
    axes2_residual = axes2.twinx()
    # residual = np.maximum((yvals - y), - (yvals - y))
    residual = yvals - y
    residual_std = np.std(residual, ddof=1)
    print('The standard deviation of residuals in 1000-6000K is ' + str(residual_std))
    axes2_residual.plot(T, residual, 'b', label='residual')
    axes2.set_xlabel('T(K)')
    axes2.set_ylabel('CP0')
    axes2_residual.set_ylabel('Residual')
    axes2.legend(loc=2)
    axes2_residual.legend(loc=0)
    axes2.set_title('poly_fitting 1000-6000', fontsize='small')
    plt.savefig(name_of_molecule + ' fitting.png')
    plt.show()
else:
    with open("T_CP0.json", 'r') as load_f:
        load_dict = json.load(load_f)
        print(load_dict)
    load_dict[name_of_molecule] = [T_lower_list, y_lower_list]
    print(load_dict)

    with open("T_CP0.json", "w") as dump_f:
        json.dump(load_dict, dump_f)

    CP0_lower = (np.multiply(np.multiply(T_lower, y_lower), T_lower)) / R
    print(CP0_lower)
    z1_lower = np.polyfit(T_lower, CP0_lower, 6)
    p1_lower = np.poly1d(z1_lower)
    print(p1_lower)
    yvals_lower = ((p1_lower(T_lower) / T_lower) / T_lower) * R
    z1_lower = z1_lower.tolist()
    z1_lower = [str(i) for i in z1_lower]
    z1_lower.insert(0, '298.15-1000')
    z1_lower.insert(0, name_of_molecule)
    print(z1_lower)

    with open('nasa_polynomials.csv', 'a+', encoding='utf-8', newline='') as nasa_poly_lower:
        writer = csv.writer(nasa_poly_lower)
        writer.writerow(z1_lower)

    fig, axes1 = plt.subplots(1, 1, figsize=(10, 5))
    # plot 298.15-1000
    axes1.plot(T_lower, yvals_lower, 'r', label='polyfit values')
    axes1.scatter(T_lower, y_lower, label='original values')
    axes1.vlines(T_lower, yvals_lower, y_lower)
    axes1.set_xlabel('T(K)')
    axes1.set_ylabel('CP0_lower')
    axes1.legend(loc=2)
    axes1.set_title('poly_fitting 298.15-1000', fontsize='small')
    plt.savefig(name_of_molecule + ' fitting.png')
    plt.show()
