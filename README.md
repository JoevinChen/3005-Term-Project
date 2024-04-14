# COMP3005 - Project (Option 2)
- Members:
  - Joevin Chen
    - Student Number: 101227689
  - Steven Lin
    - Student Number: 101240382
  - Danny Tran
    - Student Number: 101225611

## Youtube Video
[Project Video](https://youtu.be/8ZoW2OwVF6s)

## Instructions to Compile
1. Check that Python is installed:
```
python --version
```
2. Install psycopg2 if not already installed:
```
pip install psycopg2
```
3. Clone/download the repository

## Instructions to Setup the Program
1. Open PgAdmin and create a new database called "FitnessClubManagementSystem"
2. Open the Query Tool in the right click menu for "FitnessClubManagementSystem"
3. Execute the SQL code in the "ddl.sql" file
4. Execute the SQL code in the "dml.sql" file
5. In the "/App/db_connect.py" file, verify the following PostgreSQL credentials:  
```db = DatabaseConnect('FitnessClubManagementSystem', 'postgres', '!postgres', 'localhost', '5432')```
```
Replace the following from above with your credentials:

'FitnessClubManagementSystem' with your database name
'postgres' with your default PostgreSQL account name
'postgres' with your default PostgreSQL account password
'localhost' with your port number
'5432' with your PostgreSQL server IP
```

## Instructions to Run the Program
1. In the command line, navigate to the "/App" project directory
2. In the command line, execute:
```
python main.py
```
