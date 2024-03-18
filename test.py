

table_name = 'sebi_orders'
query = f"SELECT COUNT(*) FROM {table_name} WHERE type_of_order = 'ed_cgm';"
print(query)


     
        