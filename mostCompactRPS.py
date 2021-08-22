import random as r
m,p,t=r.choice(['r','p','s']),input(),{'r':1,'p':2,'s':3}
if t[p]-t[m]==1:print(m+'w')
elif p==m:print('d')
else:print(m+'l')
