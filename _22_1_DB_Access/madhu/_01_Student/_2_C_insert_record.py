'''
Created on Mar 20, 2020

@author: 0_sir_notes
'''
import psycopg2

try:
    #Step1 : Get connection
    conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            password="12345",
                            host="localhost",
                            port="5432")
    #Step2 : Get cursor on db connection
    cursor = conn.cursor()
    '''
    records = [(101, 'MADHU', 'ABC'), (102, 'Prakash', 'AREM'), (103, 'Kiran', 'VN2')]
    for record in records:
        query = "INSERT INTO STUDENT VALUES(%s, %s, %s)"
        cursor.execute(query, record)
    '''
    #Step3 : Prepare sql query
    rec1 = "INSERT INTO STUDENT_1 VALUES(101, 'MADHU', 'ABC')"
    rec2 = "insert into student_1 values(102, 'Prakash', 'AREM')"
    rec3 = "insert into STUDENT_1 values(103, 'Kiran', 'VN2')"
    # Step4 : Execute sql query
    cursor.execute(rec1)
    cursor.execute(rec2)
    res = cursor.execute(rec3)
    print("Insertion : ", res)
    #Step4: Commit the transaction
    conn.commit()
    print("Records inserted successfully")
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()