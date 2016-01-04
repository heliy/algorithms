# coding: UTF-8

import numpy as np

def random_init(K, datamat):
    return datamat[np.random.choice(datamat.shape[0], K)]

def distance(mat, others):
    dis = np.zeros((mat.shape[0], others.shape[0]))
    for (i, sample) in enumerate(mat):
        t = np.repeat([sample], len(others), axis=0)
        dis[i] = ((t-others)**2).sum(axis=-1)
    return dis

def minmax_kmeans(K, datamat, inital_centers=None,
                  beta=0.1, p_max=0.5, p_step=0.01, eta=10**(-6), t_max=500):
    '''
    minmax-k-means cluster algorithm.

    Parameters
    -------
    K: cluster number : int
    datamat: shape is (n, m), where n is the number of samples and m is the dimension of space: numpy.array
    inital_center: shape is (K, m): numpy.array
    
    Returns: (catogory, center_points, eta_sum)
    -------
    catogory: catogory number of every sample, shape is (n,): numpy.array
    center_points: axis of center points, shape is (K, m): numpy.array
    eta_sum: weighted sum of all distances between sample and center points: float

    Notes
    ------
    Ref: [Tzirtzis et al, 2014]The MinMax k-Means clustering algorithm.
    '''
    if inital_centers is None:
        centers = random_init(K, datamat)
    else:
        assert len(inital_centers) == K
        centers = inital_centers

    t, p, p_init, empty = 0, 0, 0, False
    wk = np.ones((K))*(1/K)
    delta = np.zeros((datamat.shape[0], K))
    deltaP = delta.copy()
    wkP = wk.copy()
    eta_mae, eta_this = 0, 0
    while t < t_max:
        t += 1
        L2 = distance(datamat, centers)
        mink = np.argmin(L2*(wk**p), axis=1)
        delta = np.zeros(delta.shape)
        for i in range(K):
            delta[np.where(mink == i), i] = 1
        _, countk = np.unique(mink, return_counts=True)
        if empty or np.any(countk <= 1):
            empty = True
            p -= p_step
            if p < p_init:
                return None
            delta = deltaP.copy()
            wk = wkP.copy()
        for i in range(K):
            centers[i, :] = datamat[delta[:, i] == 1].mean(axis=0)
        if p < p_max and not empty:
            deltaP = delta.copy()
            wkP = wk.copy()
            p += p_step
        vk = np.array([distance(datamat[delta[:, i] == 1], centers[i]).sum() for i in range(K)])
        vkp = vk**(1/(1-p))
        for i in range(K):
            wk[i] = beta*wk[i]+(1-beta)*(vkp[i])/vkp.sum()
        eta_this = ((wk**p)*vk).sum()
        if abs(eta_this - eta_mae) < eta:
            break
        eta_mae = eta_this
    return (np.where(delta == 1)[1], centers, eta_this)
