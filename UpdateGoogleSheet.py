import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def main():        
    print("-- Starting --")

    # Configuration of credencials and connection
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("location/key_api_google_file.json", scope)
    client = gspread.authorize(creds)

    # Open the excel file from Google Excel
    sheets = client.open("[Excel File Name]")

    # Get the sheet from excel file
    sheet_name = "[Sheet name]"
    sheet = sheets.worksheet(sheet_name)     
    
    # Making a batch get from columns 'A' and 'B'
    values = sheet.batch_get(('A2:A', 'B2:B'))    

    print('Getting values from batch_get:')
    print(values)

    info_array = []

    # Some bussiness logic example to process the result
    for row_num, (id_list, status_list) in enumerate(zip(values[0], values[1]), start=1):
        id = id_list[0] if id_list and id_list[0] is not None else None
        status = status_list[0] if status_list and status_list[0] is not None else None

        if id and isinstance(id, str) and id.isdigit() and status and isinstance(status, str) and status.lower() not in ['finish', 'finished']:
            info = {"row_num": row_num + 1, "id": id, "status": status}
            info_array.append(info)            
    # ---------------------------------------------------
        
    print(f'Information: {info_array}')

    # Do something with the data
    json_result = { "data:" : "..."}
    # --------------------------
    
    # Preparing the update list
    update_cells = []

    # Process login example
    for registro in json_result.get("data", []):            
        id = registro.get("Id", "N/A")
        status = registro.get("Status", "N/A")

        for item in info_array:
            if item["id"] == str(id):
                row = item["row_num"]
                
                # Add updated to the list
                cel_status = gspread.Cell(row=row, col=2, value=status)
                cel_updated = gspread.Cell(row=row, col=3, value="updated...")

                update_cells.extend([cel_status, cel_updated])
                                    
                print('')
                break

    # Sendo a batch update
    print(f'Sending updates: ' + str(len(update_cells)))
    sheet.update_cells(update_cells)

main()