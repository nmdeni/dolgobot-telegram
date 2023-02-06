def readDB(db_cursor,db_table,command,item="",ins_user={}):
    try:
        if command == "/del" and item != "":
            db_cursor.execute(f"""
                drop {item} from {db_table}
            """)
        # elif command == "/ins":
        #     db_cursor.execute(f"""
        #         insert into {db_table}(DB_TABLE_ITEM1)
        #     """)
            db_cursor.fetchall()
            return f"{'-'*20}\nЗапись добавленна\n{ex}\n{'-'*20}\n"
        else:
            return f"{'-'*20}\nНет такой команды\n{ex}\n{'-'*20}\n"
    except Exception as ex:
        return f"{'-'*20}\n[INFO] Ошибка программы!!!\n{ex}\n{'-'*20}\n"