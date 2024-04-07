import psycopg2

# Connection details (replace with your actual credentials)
dbname = "arcanum"
user = "arcanum"
password = "nz2TBHLHl8VSBTSxznk"
host = "pg.mlx.institute"
port = 5433

try:
    # Connect to the database
    connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

    # Create a cursor object
    cur = connection.cursor()

    # Sample query to get table information (replace with your desired query)
    cur.execute("SELECT * FROM information_schema.tables LIMIT 10")

    # Fetch data
    data = cur.fetchall()

    # Print retrieved data (optional)
    for row in data:
        print(row)

    # Close the cursor and connection
    cur.close()
    connection.close()

except Exception as e:
    print(f"Error connecting to database: {e}")

