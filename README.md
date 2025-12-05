# Csv2Excel
Anladım. İstenen kodun ve açıklamanın İngilizce versiyonunu, ikon ve kalın font kullanmadan, düz metin olarak sunuyorum.

-----

# CSV to Excel Converter (Google Colab Compatible)

This Python script is designed to upload a CSV file and convert it into an Excel (.xlsx) file, specifically utilizing the file handling capabilities of the Google Colab environment.

## Features

  * File Upload: Uses the `google.colab.files` module to provide a simple upload mechanism.
  * Conversion: Uses the Pandas library for efficient reading of CSV data and writing to the Excel format (`.xlsx`).
  * Naming Convention: Automatically suggests an output filename based on the input CSV file. The user can override this default name.
  * Download: The converted Excel file is automatically downloaded to the user's local machine.
  * Error Handling: Includes basic error checks for upload failures and issues encountered during CSV parsing.

## Prerequisites

The following Python libraries are necessary to run this script:

  * `pandas`
  * `openpyxl` (Required by Pandas to write `.xlsx` files)

You can install them if necessary:

```
pip install pandas openpyxl
```

## How to Run the Script

When the script is executed in a Google Colab cell, it follows these steps:

1.  Prompt for Upload: It displays "Upload the file (CSV)." and opens a file selection window.
2.  File Selection: After a CSV file is chosen, its name is printed.
3.  Name Input: The user is prompted with "Excel export name: ". If the user provides a name, it is used. If the input is left blank, the original filename with the `.xlsx` extension is used.
4.  Conversion and Download: The script converts the data and initiates the download, confirming with messages like "File Converted Successfully: 'filename.xlsx'" and "Download Started\!".

## Python Code

```python
import pandas as pd
from google.colab import files
import io

print("Upload the file (CSV).")

uploaded = files.upload()

if not uploaded:
    print("Upload failed.")
else:
    input_file_name = next(iter(uploaded))
    print(f"\nFile: '{input_file_name}'")

    try:        
        # Read the uploaded CSV data into a Pandas DataFrame
        data = pd.read_csv(io.BytesIO(uploaded[input_file_name]))
        
        # Determine the default output name
        default_name = input_file_name.replace(".csv", ".xlsx")
        
        # Prompt user for custom output name
        output_file_name_raw = input(f"Excel export name: ")
        
        if not output_file_name_raw:
            output_file_name = default_name
        else:
            output_file_name = output_file_name_raw
            # Ensure the output file has an Excel extension
            if not output_file_name.lower().endswith(('.xlsx', '.xls')):
                output_file_name += ".xlsx"
        
        # Write the DataFrame to an Excel file
        data.to_excel(output_file_name, index=False)
        
        print(f"\nFile Converted Successfully: '{output_file_name}'")
        print("Preparing for Download...")
        
        # Initiate download
        files.download(output_file_name)
        print("Download Started!")
        
    except Exception as e:
        print(f"\nError: {e}")
        print("Check you CSV for correct comma format.")
```

-----

## Troubleshooting

  * "Upload failed.": Ensure a file was selected in the pop-up window.
  * "Check you CSV for correct comma format.": This typically indicates that Pandas could not parse the CSV file due to an unexpected delimiter (e.g., using a semicolon instead of a comma). You may need to modify the script to specify the correct delimiter in the `pd.read_csv` function, such as `pd.read_csv(..., sep=';')`.
