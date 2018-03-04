import numpy as np
import pylab as pp
import scipy.stats as ss
alpha = 0.05

Samples = 1000000

norm = np.random.normal(0,1,Samples)
mu_a = 400
sigma_a = 40
mu_D = 0.1
sigma_D = 0.001

a = np.random.normal(mu_a,sigma_a,Samples)
#a = np.random.uniform(mu_a-sigma_a,mu_a+sigma_a,Samples)
D = np.random.normal(mu_D,sigma_D,Samples)
#D = np.random.uniform(0.05,0.15,Samples)
A = np.pi*D**2/4.
#A = np.random.normal(np.mean(A),np.std(A),Samples)

B = a / (9.81*A)

k2,p = ss.normaltest(a)
print("p= {:g}".format(p))
if p < alpha:  # null hypothesis: x comes from a normal distribution
	print("a doesn't look normal")
else:
	print("a looks normal")
	
k2,p = ss.normaltest(D)
print("p= {:g}".format(p))
if p < alpha:  # null hypothesis: x comes from a normal distribution
	print("D doesn't look normal")
else:
	print("D looks normal")
	
k2,p = ss.normaltest(A)
print("p= {:g}".format(p))
if p < alpha:  # null hypothesis: x comes from a normal distribution
	print("A doesn't look normal")
else:
	print("A looks normal")

k2,p = ss.normaltest(B)
print("p= {:g}".format(p))
if p < alpha:  # null hypothesis: x comes from a normal distribution
	print("B doesn't look normal")
else:
	print("B looks normal")

#fig, (ax1,ax2,ax3) = pp.subplots(1,3)
#ax1.hist(a,bins = 1000)
#ax2.hist(A,bins = 1000)
#ax3.hist(B,bins = 1000)
#pp.show()
z = np.polyfit(pp.sort(norm),pp.sort(B), 1)
p = np.poly1d(z)
pp.figure()
pp.plot(pp.sort(norm),pp.sort(B))
pp.plot(pp.sort(norm),p(pp.sort(norm)),"k--", linewidth=2)

pp.show()

