import logging, os
from file_handling.SQL.sql_handler import SQL_handler

em = SQL_handler(memory=True, debug=True)

#print(em.create_table("um", "ooh, ah, bum"))

#print(em.logical_statement("up ",
#    ["uuu", "<", '1'],
#    ['shit', '=', '4']
#    ))

#print(em.where(
#    ["uuu", "<", '1'],
#    ['shit', '=', '4']
#    ))
#print(em.make_col_string(
#    ['uu', 'VARCHAR(200)'],
#    ['id', 'int']
#))


print(em.update("UwU",
                [
                    ['boob', '=', 'unimpressive'],
                    ['but', '=', 'adequete']
                ],
                [
                    ["uuu", "<", '1'],
                    ['shit', '=', '4']
                ]
                ))
