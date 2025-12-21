import os
from dotenv import dotenv_values

credential_postgres = {
    **dotenv_values('../.env.example'),
    **dotenv_values('../.env'),
    # **os.environ
}
