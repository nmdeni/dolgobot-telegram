def readDB(db_cursor,db_table,command,new_user={},item=""):
    if command == "/del" and item != "":
        db_cursor.execute(f"""
            delete from {db_table} where id={item};
        """)
        return f"{'-'*20}\nЗапись добавленна\n{'-'*20}\n"
    elif command == "/ins":
        db_cursor.execute(f"""
            insert into {db_table}(user_name,user_sum,user_status) 
            values ('{new_user['name']}',{new_user['sum']},{new_user['status']});
        """)
        return f"{'-'*20}\nЗапись добавленна\n{'-'*20}\n"
    else:
        return f"{'-'*20}\nНет такой команды\n{'-'*20}\n"