import matplotlib.pyplot as plt
import numpy as np
R = 8.314510
# T_lower = np.array([298.15, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000])
T_lower = np.arange(1000, 6100, 100)
NASA_this = np.array([5.89E-16,

-6.92E-12

,

4.08E-08,

-2.40733E-04,

8.899313192,

-5.785149833E+03
,

2.053269068E+06


])
NASA_rong = np.array([-3.27E-14,

3.30E-10,

-1.44E-06,

3.404E-03



,

3.857735



,

-2.16907E+03,

1.016956E+06



])
NASA_std = np.array([-4.822380530E-15,

9.426468930E-11,

-6.836830480E-07,

2.291998307E-03,

4.646110780

,

-2.412698562E+03,

1.034972096E+06


])

Poly_this = np.poly1d(NASA_this)
Poly_rong = np.poly1d(NASA_rong)
Poly_std = np.poly1d(NASA_std)
print(Poly_this)
print(Poly_rong)
print(Poly_std)
fig, ax = plt.subplots()
# x = np.arange(298.15, 1000, 0.01)
y_this = ((Poly_this(T_lower) / T_lower) / T_lower) * R
ax.plot(T_lower, y_this, 'r', label='this work')
y_rong = ((Poly_rong(T_lower) / T_lower) / T_lower) * R
ax.plot(T_lower, y_rong, 'g', label='rong wang')
y_std = ((Poly_std(T_lower) / T_lower) / T_lower) * R
ax.plot(T_lower, y_std, 'b', label='McBride et al.')
ax.set_xlabel('T(K)')
ax.set_ylabel('CP0_lower')
ax.set_title('The comparison figure of H2O in 1000-6000K')
ax.legend()

plt.show()