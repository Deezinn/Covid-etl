from sqlalchemy import URL


def create_database_url(credentials):
    if hasattr(credentials, 'path'):
        return URL.create(
            **credentials.model_dump()
        )
    
    return URL.create(
        **credentials.model_dump()
    )