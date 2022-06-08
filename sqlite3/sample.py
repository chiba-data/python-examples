from cdcc.sample.sqlite3.sample import connect_to_database, create_table, insert_into, select_all


def main():
    connection = connect_to_database()
    cursor = connection.cursor()
    create_table(cursor)
    insert_into(cursor, [
        ('1003-02', '共済組合貯金(5月分)'),
        ('1004-02', '減免申請書(5月分)'),
        ('1005-02', '経営事項(5月分)'),
    ])
    select_all(cursor)
    for row in cursor:
        print(row)


if __name__ == '__main__':  # pragma no cover
    main()
