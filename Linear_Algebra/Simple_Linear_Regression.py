import numpy as np

# calculating coefficients

# data:
x = np.array([1, 2, 2, 3, 3, 4, 5, 6, 6, 6, 8, 10])
y = np.array([-890, -1411, -1560, -2220, -2091, -2878, -3537, -3268, -3920, -4163, -5471, -5157])

# Number of data:
n = np.size(x)

# calculate mean values:
m_x, m_y = np.mean(x), np.mean(y)

# calculating cross-deviation and squared deviation:
d_xy = np.sum(y*x) - n*m_y*m_x
d_xx = np.sum(x*x) - n*m_x*m_x

# calculating coefficients:
m = d_xy/d_xx
b = m_y - m*m_x

# print slope and intercept:
print(m,b)

