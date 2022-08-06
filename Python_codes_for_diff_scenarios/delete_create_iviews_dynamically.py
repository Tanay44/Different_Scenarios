from pyspark.sql import *
import pandas as pd
import numpy as np
#Check all tables in used database
for tables in spark.catalog.listTables(): 
    print('New individual view created : - ', tables.name)
#Create views dynamically
df = pd.DataFrame(pd.read_csv("/dbfs/FileStore/tables/table_primary_keys.csv")) 
for a, b in zip(df ['Table Name'], df ['Primary Key']): 
    dfff = spark.sql("""Create view if not exists t_test.{} as with LTS as (
        select 
        case 
        when max(AE_INSERT_TS) < max(AE_UPDATE_TS) then max(AE_INSERT_TS)
        else max(AE_UPDATE_TS) end as `Latest TS`, 
        {} as `ID_1` 
        from sol_tables.{} 
        group by {}), 
        DLT as (select {} as `ID_2`
        from sol_tables.{}
        where AE_INSERT_TYPE = 'Delete') 
        select * from sol_tables.{} 
        full outer join DLT on DLT.`ID_2` = {}.{}
        inner join LTS on LTS.`ID_1` = {}.{} 
        and (LTS.`Latest TS` = {}.AE_INSERT_TS or LTS.`Latest TS` = {}.AE_UPDATE_TS)
        where DLT.`ID_2` is null or {}.{} is null""".format(a, b, a, b, b, a, a, a, b, a, b, a, a, a, b))
#Delete views dynamically
for tables in spark.catalog.listTables():
    view_name = tables.name
    spark.sql("""Drop view t_test.{}""".format(view_name))
    print(tables.name, ' - Got deleted')