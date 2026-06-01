Vermin Inventory Analytics System


This repository contains the Vermin Inventory Analytics System, a comprehensive tool built with Streamlit for managing, analyzing, and visualizing inventory data. The application provides a user-friendly interface to perform CRUD operations, clean data, run SQL queries, and integrate with Power BI for advanced analytics.

## Features

*   **Interactive Data Management**: Load, view, and manage data from an Excel file through a clean, tabbed interface.
*   **Full CRUD Functionality**:
    *   **Create**: Add new records to your tables with an intuitive form that includes auto-incrementing IDs and data validation.
    *   **Read**: View raw and cleaned versions of your data tables.
    *   **Update**: Fetch a record by its ID and edit its attributes in a dedicated form.
    *   **Delete**: Remove one or more records by specifying their IDs.
*   **Data Cleaning**: One-click data cleaning that standardizes column names, removes duplicates, strips whitespace, and imputes missing numeric values.
*   **SQL Query Engine**: Run SQL queries directly on your inventory data from within the app and download the results as a CSV file.
*   **Power BI Integration**:
    *   **Live Data Download**: Download the up-to-date Excel data file to refresh your Power BI dashboards.
    *   **Embed Reports**: Display a publicly published Power BI report directly within the application by providing its embed URL.
    *   **Local File Access**: A button to open the local `.pbix` file in Power BI Desktop for quick access.
*   **Data Export**: Export processed data, either as individual cleaned CSV files or as a single ZIP archive containing all tables.

## Technologies Used

*   **Python**: Core programming language.
*   **Streamlit**: For building the interactive web application.
*   **Pandas**: For data manipulation and analysis.
*   **SQLite**: In-memory database for running SQL queries.
*   **Power BI**: For data visualization and reporting.
*   **Microsoft Excel**: As the primary data store.

## Setup and Usage

Follow these steps to run the application locally.

### 1. Prerequisites

*   Python 3.8+
*   The project files, including `app.py` and `Inventory_Analytics_Data_Custom.xlsx`.

### 2. Clone the Repository

```bash
git clone https://github.com/Harshit-1602/Inventory_System.git
cd Inventory_System/project_file
```

### 3. Create a Virtual Environment

It is recommended to create a virtual environment to manage dependencies.

```bash
# For Windows
python -m venv myenv
myenv\Scripts\activate

# For macOS/Linux
python3 -m venv myenv
source myenv/bin/activate
```

### 4. Install Dependencies

Install the required Python libraries.

```bash
pip install streamlit pandas openpyxl
```

### 5. Configure File Paths

Before running the application, you **must** update the hardcoded file paths in `project_file/app.py` to match the locations on your system.

Open `app.py` and modify the following lines:

```python
#
# File paths – update these to match your system
#
SAVE_FILE = r"C:\path\to\your\project_file\Inventory_Analytics_Data_Custom.xlsx"
PBIX_FILE = r"C:\path\to\your\Inventory_vermin.pbix"
```

### 6. Run the Application

Once the paths are configured, run the Streamlit app from your terminal.

```bash
streamlit run app.py
```

Your web browser will open a new tab with the running application.

## How to Use the Power BI Integration

The application offers two ways to integrate with Power BI.

### Option 1: Live Data Connection (Recommended)

The most effective way to use Power BI with this system is to connect Power BI Desktop to the `Inventory_Analytics_Data_Custom.xlsx` file.

1.  In the Streamlit app, perform your data entry and cleaning.
2.  In Power BI Desktop, use **Get Data > Excel Workbook** and select the `Inventory_Analytics_Data_Custom.xlsx` file.
3.  Build your reports.
4.  Whenever you update the data in the Streamlit app, simply click the **Refresh** button in Power BI Desktop to pull in the latest changes.

### Option 2: Embedding a Published Report

You can embed a report directly into the Streamlit interface.

1.  **Publish your report**: After creating your report in Power BI Desktop, publish it to the Power BI Service (app.powerbi.com).
2.  **Generate a public URL**: In the Power BI Service, open your report and go to **File > Embed report > Publish to web (public)**.
3.  **Copy the URL**: Copy the `iframe` embed URL provided.
4.  **Paste in the app**: In the Streamlit app, navigate to the **Power BI Report** tab and paste the URL into the input box. Your report will be displayed.
