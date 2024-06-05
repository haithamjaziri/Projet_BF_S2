import logging
import pathlib

import tomli

from repository import Bsm

path = pathlib.Path(__file__).parent / "config.toml"
with path.open(mode="rb") as fp:
    param = tomli.load(fp)



def main():
    print(
        Bsm(
            param["model"]["r"],
            param["model"]["S"],
            param["model"]["K"],
            param["model"]["T"],
            param["model"]["sigma"],
        ).blackScholes(param["model"]["type"])
    )


if __name__ == "__main__":
    logging.basicConfig(
        # stream=sys.stdout,
        level=logging.DEBUG,
        filename="log.log",
        filemode="w",
        format="%(asctime)s - %(" "name)s - %(" "levelname)s - %(" "message)s",
    )

    main()
