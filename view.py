from main import *

print("Option Price is : ", round(blackScholes(r, S, K, T, sigma, type=Type_Opt), 5))

print("Delta Option is : ", round(delta_calc(r, S, K, T, sigma, type=Type_Opt), 4))

print("Gamma Option is : ", round(gamma_calc(r, S, K, T, sigma, type=Type_Opt), 4))

print("Vega Option is : ", round(vega_calc(r, S, K, T, sigma, type=Type_Opt), 4))

print("Theta Price is : ", round(theta_calc(r, S, K, T, sigma, type=Type_Opt), 4))

print("Rho Price is : ", round(rho_calc(r, S, K, T, sigma, type=Type_Opt), 4))