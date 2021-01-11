#!/usr/bin/env python
# coding: utf-8

# In[164]:


import numpy as np


# In[295]:


f = open('C:/Users/HP/Downloads/_3a8d746cf4d86fba2f31586f239d11fd_sentences (6).txt')


# In[303]:


with open('C:/Users/HP/Downloads/_3a8d746cf4d86fba2f31586f239d11fd_sentences (6).txt', 'r') as cat:
    sentences = []
    for line in cat:
        line_list = re.split('\n\\r.', line.lower())
        sentences += line_list


# In[296]:


f_1 = f.read()


# In[297]:


import re
f_2 = re.split('[^a-z]', f_1.lower())


# In[299]:


f_2 = [x for x in f_2 if x]
print(f_2)


# In[300]:


words={}
numb=0
for w in f_2:
    if w not in words:
        words[w] = numb
        numb += 1


# In[364]:


words


# In[365]:


words_T = dict(zip(words.values(), words.keys()))


# In[366]:


words_T


# In[367]:


matrix = np.zeros((len(sentences), len(words_T)))


# In[368]:


matrix.shape


# In[369]:


for i in range(len(sentences)):
    for j in range(len(words_T)):
        matrix[i][j] = sentences[i].count(words_T[j])
        


# In[370]:


matrix


# In[371]:


from scipy.spatial import distance
cos_matrix = []
for i in range(len(sentences)):
    cos_matrix.append(distance.cosine(matrix[0], matrix[i]))
cos_matrix = np.array(cos_matrix) 
print (cos_matrix)


# In[361]:


a=np.sort(cos_matrix)


# In[362]:


a


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




