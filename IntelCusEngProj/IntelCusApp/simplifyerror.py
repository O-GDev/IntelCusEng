import pandas as pd
import os
from rest_framework.response import Response

def error_simplification(error):
    file_path = 'C:/Users/Administrator/Documents/IntelCusEng/IntelCusEngProj/IntelCusApp/dataset.csv'
        # Use Pandas to read the Excel file
    df = pd.read_csv(file_path, encoding="cp1252")
        # Process the data as needed
    # print(df)        
    # Perform data comparison by iterating through the Excel file
    # for num in df.Response:
    matching_rows = df[df['Response'] == error]

    result = matching_rows['Preferred Interpretation'].values

    if len(result)>0:
        print(result[0])
        return Response(result[0])
    else:
        print("No match found for this error message!.")
        return Response("No match found for this error message!.")
        # if num == error:
    # print(num)

        
        # print(df.Response)
    # return Response(num)

    # matches = [],

    # for index, row in df.columns(row['Response Code'] == error):
    #         print(row)
        # if row['Response Code'] == error:
            # matches.append(row)
            # return Response(row['Preferred Interpretation'])
        # else:
        #     return Response(row['Preferred Interpretation'])
        

        # For testing purposes, you can convert the DataFrame to HTML and render it in a Django template
        # html_table = df.to_html()

        # return render(request, 'excel_data.html', {'html_table': html_table})
        # return Response(row['Preferred Interpretation'])
        # return Response(df)     
    # else:
    #     return Response("File path doesn't exist")