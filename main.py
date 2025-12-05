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
        data = pd.read_csv(io.BytesIO(uploaded[input_file_name]))
        default_name = input_file_name.replace(".csv", ".xlsx")
        output_file_name_raw = input(f"Excel export name: ")
        if not output_file_name_raw:
            output_file_name = default_name
        else:
            output_file_name = output_file_name_raw
            if not output_file_name.lower().endswith(('.xlsx', '.xls')):
                output_file_name += ".xlsx"
        data.to_excel(output_file_name, index=False)
        print(f"\nFile Converted Successfully: '{output_file_name}'")
        print("Preparing for Download...")
        files.download(output_file_name)
        print("Download Started!")
    except Exception as e:
        print(f"\nError: {e}")
        print("Check you CSV for correct comma format.")
