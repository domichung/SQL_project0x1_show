import MySQLdb

def list_all_grade(grade):
    try:
        # 連線
        conn = MySQLdb.connect(host="127.0.0.1",
                               user="try",
                               passwd="123",
                               db="show_sql")
        
        cursor = conn.cursor()
        
        # 指令
        cursor.execute("SELECT * FROM class_list WHERE class_id = %s", (str(grade)))
        
        # 爬他
        classinfo = cursor.fetchall()
        
        #有沒有都可以地斷連線
        cursor.close()
        conn.close()
        
        classinfo_array = [list(item) for item in classinfo]
        
        return classinfo_array
        
    except Exception as e:
        print("Error:", e)
        return None
    

#print(list_all_grade(1))
