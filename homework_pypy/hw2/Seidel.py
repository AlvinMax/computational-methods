
# coding: utf-8

# In[ ]:


import numpy as np


# In[177]:


def read_matrix():
    f = open('test.txt', 'r')
    m = []
    for line in f:
        m.append([float(x) for x in line.split()])
    return m


# In[178]:


m = read_matrix()
b = np.array([x[-1:] for x in m])
m = np.array([x[:-1] for x in m])
# mt = m.transpose()
# m = mt.dot(m)
# b = mt.dot(b)


# In[179]:


#m = np.matrix(m)
b


# In[180]:


#m = np.random.rand(3, 3)
B = np.tril(m)
C = np.triu(m, k=1)
B_inv = np.linalg.inv(B)

eigenvalues = np.linalg.eig(-B_inv.dot(C))[0]
print(eigenvalues)
if not all([abs(x) <= 1 for x in eigenvalues]):
    print("Вы проиграли")

def next(x_k):
    return -B_inv.dot(C).dot(x_k) + B_inv.dot(b)
m


# In[181]:


n = 5
BB = np.zeros((n, n))
for i in range(0, n):
    for j in range(0, n):
        BB[i][j] = -m[i][j] / m[i][i] if i != j else 0
B1 = np.tril(BB)
B2 = np.triu(BB)
BB


# In[183]:


def check(x):
    x = [a[0] for a in x]
    for line in m:
        res = sum([a[0] * a[1] for a in zip(line, x)])
        print(res)

def should_finish(prev, curr, eps=0.0001):
    #return np.linalg.norm(prev - curr) < eps * (1 - np.linalg.norm(BB)) / np.linalg.norm(B2)
    return np.linalg.norm(prev - curr) / np.linalg.norm(curr) < eps


# In[185]:


prev = np.array([[0], [0], [0], [0], [0]])
curr = next(prev)
cnt = 1
while not should_finish(prev, curr, eps=0.0000001):
    # print(x)
    prev = curr
    curr = next(curr)
    cnt += 1
print(curr)
print(cnt)
print(check(curr))


# In[ ]:


prev = np.array([[0], [0], [0], [0], [0]])
curr = next(prev)
cnt = 1
w = 2
while not should_finish(prev, curr, eps=0.0000001):
    # print(x)
    prev = curr
    curr = next(curr)
    curr += (w - 1) * (curr - prev)
    cnt += 1
print(curr)
print(cnt)
print(check(curr))


# In[161]:


B1.dot(curr) + B2.dot(curr) + b


# In[182]:


(1 - np.linalg.norm(BB)) / np.linalg.norm(B2)
np.linalg.norm(BB, ord=1)


# In[176]:


for i in range(0, 5):
    for j in range(0, 5):
        print(1 / (1.0 + i + j), end=' ')
    print()

