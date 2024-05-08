import numpy as np
import matplotlib.pyplot as plt

# Number of data points
N = 100

# Note - Noise is always zero mean Gaussian, sigma is the variance
def error_vector(N, sigma):
    return sigma * np.random.randn(N,1)

def constant_level_noise(theta=9):
    G_theta = np.full((N, 1), theta)
    x = G_theta + error_vector(N, sigma=0.1)

    n = np.arange(N) 
    x_expanded = np.repeat(np.expand_dims(n,-1), x.shape[-1], -1)       
    plt.plot(x_expanded,x) 

    plt.axhline(theta, color='red', linestyle='dashed')
    plt.xlabel('n')
    plt.ylabel('x_n')
    plt.title(f'Constant Level in Noise, θ = {theta}')
    plt.show()
    return

#constant_level_noise()

def sinusoid_model():
    omega = 0.1
    theta = np.random.rand(2, 1)    # coefficients a and b are generated randomly from range 0 to 1
    G_matrix = np.zeros((N, 2))

    for i in range(N):
        G_matrix[i, 0] = np.cos(i*omega) 
        G_matrix[i, 1] = np.sin(i*omega) 

    G_theta = np.matmul(G_matrix, theta)
    x = G_theta + error_vector(N, sigma=0.1)

    n = np.arange(N) 
    x_expanded = np.repeat(np.expand_dims(n,-1), x.shape[-1], -1)       
    plt.plot(x_expanded,x) 
    plt.plot(x_expanded, G_theta, color='gray', linestyle='dashed', label='Data Without Noise (Gθ)')

    plt.xlabel('n')
    plt.ylabel('x_n')
    plt.title(f'Sinusoid Model')
    plt.legend()
    plt.show()
    return

""""
Idea is, if we are just given the noisy waveform x_n that is plotted, can we estimate the parameters a and b in theta vector
"""

sinusoid_model()


pole1 = 0.99*np.exp(1j*0.1*np.pi)
pole2 = np.conj(pole1)
pole3 = 0.97*np.exp(1j*0.4*np.pi)
pole4 = np.conj(pole3)
e = error_vector(N=1000, sigma=1)
n = np.arange(1000) 
x_expanded = np.repeat(np.expand_dims(n,-1), e.shape[-1], -1)       
plt.plot(x_expanded,e) 
plt.title('Gaussian Noise with Zero Mean and Variance = 1')
plt.show()