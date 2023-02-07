def readDB(db_cursor,db_table,command,item=""):
    if command == "/del" and item != "":
        db_cursor.execute(f"""
            delete from {db_table} where id={item};
        """)
    # elif command == "/ins":
    #     db_cursor.execute(f"""
    #         insert into {db_table}(DB_TABLE_ITEM1)
    #     """)
        # db_cursor.fetchall()
        return f"{'-'*20}\nЗапись добавленна\n{'-'*20}\n"
    else:
        return f"{'-'*20}\nНет такой команды\n{'-'*20}\n"