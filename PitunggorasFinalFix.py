#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Pitunggoras:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def Operasi(self):
        if (self.z == 0):
            return (self.x**2 + self.y**2)**(1/2)
        if (self.x == 0):
            return (self.z**2 - self.y**2)**(1/2)
        if (self.y == 0):
            return (self.z**2 - self.x**2)**(1/2)


# In[4]:


pythagoras2 = Pitunggoras(x = float(input("Masukkan nilai x = ")), y = float(input("Masukkan nilai y = ")), z = float(input("Masukkan nilai z = ")))
    
print("Hasilnya adalah ", pythagoras2.Operasi())
k=input("press close to exit")


# In[ ]:




