from database import engine

try:
    with engine.connect() as connection:
        print("successful")
except Exception as e:
    print("failed")
    print(e)