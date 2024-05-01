import numpy as np
from scipy.stats import norm

from main import *

# Calcul du prix de l'option avec la formule de BS
def blackScholes(r, S, K, T, sigma, type=Type_Opt):
    d1 = (np.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    try:
        if type == "C":
            price = S * norm.cdf(d1, 0, 1) - K * np.exp(-r * T) * norm.cdf(d2, 0, 1)
        elif type == "P":
            price = K * np.exp(-r * T) * norm.cdf(-d2, 0, 1) - S * norm.cdf(-d1, 0, 1)
        return price
    except:
        print("Please confirm option type, either 'C' for Call or 'P' for Put")


# Calcul du DELTA
def delta_calc(r, S, K, T, sigma, type=Type_Opt):
    d1 = (np.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    try:
        if type == "C":
            delta_calc = norm.cdf(d1, 0, 1)
        elif type == "P":
            delta_calc = -norm.cdf(-d1, 0, 1)
        return delta_calc
    except:
        print("Please confirm option type, either 'C' for Call or 'P' for Put")


# Calcul du GAMMA
def gamma_calc(r, S, K, T, sigma, type=Type_Opt):
    d1 = (np.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    try:
        gamma_calc = norm.pdf(d1) / (S*sigma*np.sqrt(T))
        return gamma_calc
    except:
        print("Please confirm option type, either 'C' for Call or 'P' for Put")

print("Gamma Option is : ", round(gamma_calc(r, S, K, T, sigma, type=Type_Opt), 4))


# Calcul du VEGA
def vega_calc(r, S, K, T, sigma, type=Type_Opt):
    d1 = (np.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    try:
        vega_calc = S * norm.pdf(d1, 0, 1) * np.sqrt(T)
        return vega_calc *0.01
    except:
        print("Please confirm option type, either 'C' for Call or 'P' for Put")


# Calcul Theta
def theta_calc(r, S, K, T, sigma, type=Type_Opt):
    d1 = (np.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    try:
        if type == "C":
            theta_calc = -(S*norm.pdf(d1, 0, 1)*sigma)/(2*np.sqrt(T)) - r*K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif type == "P":
            theta_calc = -(S*norm.pdf(d1, 0, 1)*sigma) / (2*np.sqrt(T)) + r*K*np.exp(-r*T)*norm.cdf(-d2, 0, 1)
        return theta_calc/365
    except:
        print("Please confirm option type, either 'C' for Call or 'P' for Put")


# Calcul Rho
def rho_calc(r, S, K, T, sigma, type=Type_Opt):
    d1 = (np.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    try:
        if type == "C":
            rho_calc = K * T * np.exp(-r*T) * norm.cdf(d2,0,1)
        elif type == "P":
            rho_calc = -K * T * np.exp(-r*T) * norm.cdf(-d2,0,1)
        return rho_calc * 0.01
    except:
        print("Please confirm option type, either 'C' for Call or 'P' for Put")