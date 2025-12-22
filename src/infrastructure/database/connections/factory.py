from sqlalchemy import URL


def create_database_url(credentials):
    if hasattr(credentials, 'drivername'):
        return URL.create(
            **credentials.model_dump()
        )
    
    return URL.create(
        **credentials.model_dump()
    )