from infrastructure.database.security import credential_postgres
from infrastructure.database.connections.postgre import PostgreCredentials
from infrastructure.database.connections.sqlite import SqliteCredential


def load_database_credentials():
    engine = credential_postgres.get("ENGINE", "sqlite")

    if engine == "postgres":
        return PostgreCredentials(
            username=credential_postgres["DB_USER"],
            password=credential_postgres["DB_PASS"],
            host=credential_postgres["DB_HOST"],
            port=int(credential_postgres["DB_PORT"]),
            database=credential_postgres["DB_NAME"],
        )

    return SqliteCredential()
