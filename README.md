
GoogleSheetUpdate is a Python script template designed for seamless integration with Google Sheets, focusing on efficient batch reading and updating operations. The primary goal of this project is to minimize the number of API requests, thereby optimizing usage within the constraints of the free tier of the Google Sheets/Drive API.

## Key Features
* Batch Operations: Perform bulk reading and updating of data in Google Sheets to reduce the number of API requests.
* Request Optimization: Minimize the risk of exceeding API limits on the free plan by consolidating actions into efficient batch processes.
* Ease of Use: Utilize a straightforward Python script template that facilitates integration with Google Sheets, ensuring quick setup and implementation.    

## Prerequisites

#### Python 3
You can find the official download and instalation guide here > https://www.python.org/downloads/

## Requirements

The ```requirements.txt``` file should list all Python libraries that tis project depends on, and they will be installed using:

```
pip install -r requirements.txt
```

## Getting Started

1. Clone the repository.
2. Follow the setup instructions in the documentation on **"Google Cloud Console"** to configure the script with your Google Sheets API credentials.
3. Customize the script according to your specific use case.
4. Run the script to efficiently read and update data in your Google Sheets.

#### Configuration Steps on Google Drive:

1. Create a Project in the Google Developers Console:
    * Access the Google Cloud Console.
    * Create a new project or select an existing project.

2. Enable the Google Sheets API for the Project:
    * In the Google Cloud Console, go to the "Library" page.
    * Search for and enable the "Google Sheets API."

3. Create Credentials for the Project:
    * On the API configuration page, click on "Create credentials."
    * Select "Service" and choose "Service Account."
    * Provide a name for the service account and assign the "Editor" role to it.
    * Create the service account and download the JSON key file.

4. Share the Spreadsheet with the Service Account's Email Address:
    * Open the spreadsheet in Google Sheets.
    * Share the spreadsheet with the service account's email address, allowing editing permissions.