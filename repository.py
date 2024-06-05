import logging

import numpy as np
from scipy.stats import norm

logger = logging.getLogger(__name__)


class Bsm:
    def __int__(self):
        self.s = S
        self.k = K
        self.t = T
        self.r = r
        self.sigma = sigma

    def d1(self) -> float:
        return (
            np.log(self.spot / self.strike)
            + (self.r - self.q + 0.5 * self.sigma**2) * self.t
        ) / (self.sigma * np.sqrt(self.t))

    def d2(self) -> float:
        return -(self.sigma * np.sqrt(self.t)) + self.d1

    # Calcul du prix de option avec la formule de BS
    def blackScholes(self, type: str):
        try:
            if type == "C":
                price = self.s * norm.cdf(self.d1(), 0, 1) - self.k * np.exp(
                    -self.r * self.t
                ) * norm.cdf(self.d2(), 0, 1)
            elif type == "P":
                price = self.k * np.exp(-self.r * self.t) * norm.cdf(
                    -self.d2(), 0, 1
                ) - self.s * norm.cdf(-self.d1(), 0, 1)
            return price
        except:
            logger.info(
                f"Please confirm option type, either 'C' for Call or 'P' for Put"
            )

    # Calcul du DELTA
    def delta_calc(self, type: str):
        try:
            if type == "C":
                delta_calc = norm.cdf(self.d1(), 0, 1)
            elif type == "P":
                delta_calc = -norm.cdf(-self.d1(), 0, 1)
            return delta_calc
        except:
            logger.info(
                f"Please confirm option type, either 'C' for Call or 'P' for Put"
            )

    # Calcul du GAMMA
    def gamma_calc(self):
        gamma_calc = norm.pdf(self.d1()) / (self.s * self.sigma * np.sqrt(self.t))
        return gamma_calc

    # Calcul du VEGA
    def vega_calc(self):
        vega_calc = self.s * norm.pdf(self.d1(), 0, 1) * np.sqrt(self.t)
        return vega_calc * 0.01

    # Calcul Theta
    def theta_calc(self, type: str):
        try:
            if type == "C":
                theta_calc = -(self.s * norm.pdf(self.d1(), 0, 1) * self.sigma) / (
                    2 * np.sqrt(self.t)
                ) - self.r * self.k * np.exp(-self.r * self.t) * norm.cdf(
                    self.d2(), 0, 1
                )
            elif type == "P":
                theta_calc = -(self.s * norm.pdf(self.d1(), 0, 1) * self.sigma) / (
                    2 * np.sqrt(self.t)
                ) + self.r * self.k * np.exp(-self.r * self.t) * norm.cdf(
                    -self.d2(), 0, 1
                )
            return theta_calc / 365
        except:
            logger.info(
                f"Please confirm option type, either 'C' for Call or 'P' for Put"
            )

    # Calcul Rho
    def rho_calc(self, type: str):
        try:
            if type == "C":
                rho_calc = (
                    self.k
                    * self.t
                    * np.exp(-self.r * self.t)
                    * norm.cdf(self.d2(), 0, 1)
                )
            elif type == "P":
                rho_calc = (
                    -self.k
                    * self.t
                    * np.exp(-self.r * self.t)
                    * norm.cdf(-self.d2(), 0, 1)
                )
            return rho_calc * 0.01
        except:
            logger.info(
                f"Please confirm option type, either 'C' for Call or 'P' for Put"
            )
