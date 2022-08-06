# # opening the file in read mode
# fileObject = open("sample_text.txt", "r")
 
# # clearing the input buffer
# fileObject.flush()
 
# # reading the content of the file
# fileContent = fileObject.read()
 
# # displaying the content of the file
# print(fileContent)
 
# # closing the file
# fileObject.close()

import inspect
import pandas as pd
print(inspect.signature(pd.DataFrame))