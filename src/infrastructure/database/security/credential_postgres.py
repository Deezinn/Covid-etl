import os

from dotenv import dotenv_values

ENVDATABASE = {
    **dotenv_values('../.env.example'),
    **dotenv_values('../.env'),
    # **os.environ
}
