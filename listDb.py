def list_output(db_cursor):
    table_db = ""

    db_cursor.execute("""
        select * from users_dolg;
    """)

    for k in db_cursor.fetchall():
        if k[3] == True:
            table_db += f"ID {k[0]}|\t{k[1]}\t{k[2]}₽\tВЫ должны\n"
        else:
            table_db += f"ID {k[0]}|\t{k[1]}\t{k[2]}₽\tВАМ должны\n"

    return table_db