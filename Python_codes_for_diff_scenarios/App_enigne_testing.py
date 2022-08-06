import pandas as pd
#This csv has a colummn having all coalesce columns
    # main_csv = {'columns': ['a','b','c','d','e','f','g','h','i','j','k']}
    # print(main_csv)
    # df_main = pd.DataFrame(main_csv)
    # print(df_main.to_string(index=False))
a_m = ['a','b','c','d','e','f','g','h','i','j','k']
#this will have a single table column
a =  ['a', 'b', 'i']

#Now we want only intersected values
print([x for x in a_m if x not in a]) # it will give values not in a
print([x for x in a_m if x in a]) # it will give only intersected values
#column will go to dynamic code
ac = [x for x in a_m if x in a]
print(','.join(ac))
for i in ac:
    j = "ae.",i
    print(f"create view views_test.view1 as select {j}, {j}", end="")