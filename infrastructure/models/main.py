from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/postgres", pool_size=10, max_overflow=0,echo=True)

# verify connection
def check_connection_success() -> bool:
    try:
        # Establish the connection
        connection = engine.connect()
        print("Connection to the database was successful!")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


check_connection_success()
engine.connect().close()