def list_output(db_cursor):
    table_db = ""

    db_cursor.execute("""
        select * from users_dolg;
    """)

    for k in db_cursor.fetchall():
        if k[3] == True:
            table_db += f"{k[0]}   {k[1]}   {k[2]}₽   ВЫ должны\n"
        else:
            table_db += f"{k[0]}   {k[1]}   {k[2]}₽   ВАМ должны\n"

    return table_db