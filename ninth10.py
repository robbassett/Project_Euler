from utils import *
import time
import itertools

# PROJECT EULER 81
def euler81():
    d = open('aux/e81.dat','r').readlines()
    m = np.zeros((len(d),len(d)))
    for i in range(len(d)):
        m[i] = np.array(d[i].split(',')).astype(int)

    min_sum = np.zeros(m.shape)
    min_sum[0,0] = m[0,0]
    for i in range(1,m.shape[0]):
        min_sum[0,i] = m[0,i] + min_sum[0,i-1]
        min_sum[i,0] = m[i,0] + min_sum[i-1,0]

    for i in range(1,m.shape[0]):
        min_sum[i,i] = m[i,i] + min([min_sum[i-1,i],min_sum[i,i-1]])
        for j in range(i+1,m.shape[0]):
            min_sum[i,j] = m[i,j] + min([min_sum[i,j-1],min_sum[i-1,j]])
            min_sum[j,i] = m[j,i] + min([min_sum[j,i-1],min_sum[j-1,i]])
        
    return int(min_sum[-1,-1])

# PROJECT EULER 82
def euler82():
    
    d = open('aux/e81.dat','r').readlines()
    m = np.zeros((len(d),len(d)))
    for i in range(len(d)):
        m[i] = np.array(d[i].split(',')).astype(int)
        
    min_sum = np.zeros((m.shape[0],*m.shape))
    min_sum[:,:,0] = m[:,0]
    for k in range(m.shape[0]-1):
        for v in range(m.shape[0]):
            min_sum[v,v,k+1] = min_sum[v,v,k] + m[v,k+1]
            for i in range(v-1,-1,-1): min_sum[v,i,k+1] = min_sum[v,i+1,k+1] + m[i,k+1]
            for i in range(v+1,m.shape[0]): min_sum[v,i,k+1] = min_sum[v,i-1,k+1] + m[i,k+1]

        col_min = min_sum.min(axis=0)
        for v in range(m.shape[0]): min_sum[v] = np.copy(col_min)

    min_sum = min_sum.min(axis=0)
    return int(min_sum[:,-1].min())
        
if __name__ == '__main__':
    # EIGHTY ONE:
    st = time.time()
    print(f'Problem 81: {euler81()} ({time.time()-st} s)')
    
    # EIGHTY TWO:
    st = time.time()
    print(f'Problem 82: {euler82()} ({time.time()-st} s)')
