# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import math
import matplotlib.pyplot as plt


# %%
def exponential_pdf(y,l = 1.0):
    return l * np.exp(-l * y)


# %%
t = np.linspace(0,10,100)
p_exp = exponential_pdf(t)


# %%
plt.plot(t,p_exp)
plt.title('Exponential Distribution pdf')


# %%
z = np.random.uniform(size=1000)
y = -np.log(z)


# %%
plt.hist(y,50,density=True,label='approximated')
plt.plot(t,p_exp,label='true',color='red')
plt.legend()
plt.show()


# %%
# cauchy distribution
def cauchy_pdf(y):
    return 1.0/np.pi *(1.0 / (1+ y**2))


# %%
t= np.linspace(-5,5,100)
p_cauchy = cauchy_pdf(t)


# %%
plt.plot(t,p_cauchy)
plt.title('Cauchy pdf')
plt.show()


# %%
z = np.random.uniform(0,1,size=1000)
y_cauchy = np.arctanh(np.pi * (z - 0.5))


# %%
plt.hist(y_cauchy,50,density=True,label='generated')
plt.plot(t,p_cauchy,color='red',label='expected pdf')
plt.legend()
plt.title('Generating a cauchy pdf samples using inverse transform method')
plt.show()


# %%
y = np.linspace(-100,100,100)
z = 1.0/np.pi *np.arctan(y)+ 0.5
z_tanh = 1.0/np.pi *np.tanh(y) + 0.5
z_samples = np.linspace(0,1,100)
y_samples = np.tan(np.pi * (z_samples - 0.5))


# %%
plt.plot(y,z,label='arctan')
plt.plot(y,z_tanh,label='tanh')
plt.plot(y_samples,z_samples,label='inv')
plt.legend()
plt.show()


# %%



