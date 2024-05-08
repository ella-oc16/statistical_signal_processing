import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# Define the coefficients of the transfer function in z-domain
numerator = [1]  # coefficients of the numerator
denominator = [1, -0.5, 0.9]  # coefficients of the denominator

# Create the transfer function
system = signal.TransferFunction(numerator, denominator)

def convert(r, theta):
    a = r*np.cos(theta)
    b = r*np.sin(theta)
    return a + 1j*b

def print_poles(system):
    poles = system.poles
    print('Poles in a+bi form:')
    for pole in poles:
        print(pole)
    print('Poles in re^itheta form:')
    for pole in poles:
        a, b = np.real(pole), np.imag(pole)
        r = np.sqrt(a**2 + b**2)
        theta = np.arctan(b/a)
        print((r, theta))

def pole_zero_plot(system):
    # Find the zeroes and poles of the transfer function
    zeroes = system.zeros
    poles = system.poles

    # Plot the zeroes and poles on the complex plane
    plt.scatter(np.real(zeroes), np.imag(zeroes), marker='o', color='blue', label='Zeroes')
    plt.scatter(np.real(poles), np.imag(poles), marker='x', color='red', label='Poles')

    # Create the real and imaginary axes 
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.title('Pole-Zero Plot')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.legend()
    plt.grid(True)

    # Plot the unit circle
    theta = np.linspace(0, 2*np.pi, 100)
    plt.plot(np.cos(theta), np.sin(theta), linestyle='dashed', color='green', label='Unit Circle')

    plt.show()
    return

def bode_plot(system):
    # Calculate the frequency response
    frequencies, magnitude, phase = signal.bode(system)

    # Convert frequencies to radians per second
    frequencies_rad = 2 * np.pi * frequencies

    # Plot the magnitude response
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.semilogx(frequencies_rad, magnitude, 'b')
    plt.title('Bode Plot - Magnitude Response')
    plt.xlabel('Frequency [Radians/s]')
    plt.ylabel('Magnitude [dB]')
    plt.grid(True)

    # Plot the phase response
    plt.subplot(2, 1, 2)
    plt.semilogx(frequencies_rad, phase, 'b')
    plt.title('Bode Plot - Phase Response')
    plt.xlabel('Frequency [Radians/s]')
    plt.ylabel('Phase [degrees]')
    plt.grid(True)

    plt.tight_layout()
    plt.show()
    return

def nyquist_plot(system):
    w, h = signal.freqresp(system)

    # Plot the Nyquist diagram
    plt.figure(figsize=(8, 8))
    plt.plot(h.real, h.imag, 'b')
    plt.title('Nyquist Diagram')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.grid(True)
    plt.axis('equal')  # Set equal scaling for x and y axes
    plt.show()
    return


print_poles(system)
pole_zero_plot(system)
bode_plot(system)
nyquist_plot(system)



