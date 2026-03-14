import pandas as pd
import numpy  as np

#Supplier Data
#1 Load data
df = pd.read_excel("Inventory_Analytics_Data_Custom.xlsx",sheet_name="Suppliers")

print("--------Original Data-----")
print(df.head())
print("\nShape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())

# 2. Remove duplicate rows
df = df.drop_duplicates()
print("--------Duplicate Rows Removed---------\n")
print(df.head())

# 3. Clean column names
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("--After cleaning Column Names\n--")
print(df.head())
print("\nNew Column Names:", df.columns.tolist())

# 4. Handle missing values
#Filling missing numbers
df["phone"] = df["phone"].fillna("Unknown")
print("\n---- After Handling Missing Values ----\n",df.head())
print(df.isnull().sum())

#5. Text Columns standardize
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip().str.title()
print("\n---- Text Columns ----\n",df.head())
print(df.isnull().sum())

#6 Save the Data
df.to_excel("cleaned_suppliers.xlsx", index=False)

print("\n✅ Suppliers sheet cleaned and saved successfully.")


#===== Components_Master Data =====

df_comp = pd.read_excel(
    "Inventory_Analytics_Data_Custom.xlsx",
    sheet_name="Components_Master"
)
print("\n===== Components Master Original =====")
print(df_comp.head())
print("\nShape:", df_comp.shape)
print("\nMissing values:\n", df_comp.isnull().sum())

# 1. Remove duplicates
before_rows = df_comp.shape[0]

df_comp = df_comp.drop_duplicates()

after_rows = df_comp.shape[0]

print("\nDuplicates removed:")
print("Rows before:", before_rows)
print("Rows after :", after_rows)

#2 Clean Column names
df_comp.columns = (
    df_comp.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
)
print("\nColumn names after cleaning:")
print(df_comp.columns.tolist())

#3.Check Missing Values
print("\nMissing Values before handling: \n", df_comp.isnull().sum())

#4.Standardize text columns
for col in df_comp.select_dtypes(include=["object","string"]).columns:
    df_comp[col] =  df_comp[col].str.strip().str.title()

print("\nPreview after Standardization of Text:\n")
print(df_comp.head())

#5. Cleaned components_master
df_comp.to_excel("cleaned_components_master.xlsx", index=False)

print("\nComponents_Master fully cleaned and saved.")

# ================= PURCHASE_ORDERS CLEANING =================

#1 Load Data
df_po = pd.read_excel(
    "Inventory_Analytics_Data_Custom.xlsx",
    sheet_name="Purchase_Orders"
)
print("\n======= Purchase Orders  =========\n")
print(df_po.head())
print("\nShape:", df_po.shape)
print("\nMissing values:\n", df_po.isnull().sum())

#2 Remove Duplicates if any
before_rows = df_po.shape[0]
df_po = df_po.drop_duplicates()
after_rows = df_po.shape[0]

print("\n Duplicates Removed:")
print("\n Rows Before: ",before_rows)
print("\n Rows After: ",after_rows)

#3 Clean Column Names(Upper to lower,extra spaces,etc.)
df_po.columns =(
    df_po.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\n Columns name after Cleaning ")
print(df_po.columns.tolist())


#4.Convert date columns to datetime
df_po["po_date"] = pd.to_datetime(df_po["po_date"], errors="coerce")
df_po["delivery_date"] = pd.to_datetime(df_po["delivery_date"], errors="coerce")

print("\n Date conversion done")
print(df_po[["po_date", "delivery_date"]].head())

# 5. Standardize text columns
for col in df_po.select_dtypes(include=["object", "string"]).columns:
    df_po[col] = df_po[col].str.strip().str.title()

print("\n Text standardization done")
print(df_po.head())

# 6. Final missing value check
print("\n Final missing values:\n", df_po.isnull().sum())

#7.Save cleaaned sheet
df_po.to_excel("cleaned_purchase_orders.xlsx", index=False)

print("\n✅ Purchase_Orders manual cleaning COMPLETED")


# ================= INVENTORY_STOCK CLEANING =================
#1. Load data
df_inv = pd.read_excel(
    "Inventory_Analytics_Data_Custom.xlsx",
    sheet_name="Inventory_Stock"
)
print("\n========= Inventory Stock=======")
print(df_inv.head())
print("\nShape: ", df_inv.shape)
print("\n Missing Values:\n", df_inv.isnull().sum())

#2. Remove Duplicates
before_rows = df_inv.shape[0]
df_inv = df_inv.drop_duplicates()
after_rows = df_inv.shape[0]

print("\n Duplicates Removed:")
print("Rows before:", before_rows)
print("\n Rows After:", after_rows)

#3. Standardize Column
df_inv.columns = (
    df_inv.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\n Columns names after Cleaned:")
print(df_inv.columns.tolist())

#4. Missing Values
for col in df_inv.select_dtypes(include="number").columns:
    df_inv[col] = df_inv[col].fillna(df_inv[col].median())

for col in df_inv.select_dtypes(include=["object", "string"]).columns:
    df_inv[col] = df_inv[col].fillna("Unknown")

#5. Missing
print("\nFinal missing values:\n", df_inv.isnull().sum())

#6. Final
df_inv.to_excel("cleaned_inventory_stock.xlsx", index=False)

print("\nInventory_Stock manual cleaning COMPLETED")



# ================= COMBINE ALL CLEANED SHEETS =================

with pd.ExcelWriter("cleaned_inventory_final.xlsx") as writer:
    df.to_excel(writer, sheet_name="Suppliers", index=False)
    df_comp.to_excel(writer, sheet_name="Components_Master", index=False)
    df_po.to_excel(writer, sheet_name="Purchase_Orders", index=False)
    df_inv.to_excel(writer, sheet_name="Inventory_Stock", index=False)

print("\n🎉 FINAL CLEANED EXCEL CREATED SUCCESSFULLY!")


import pandas as pd

df = pd.read_excel("Inventory_Analytics_Data_Cleaned.xlsx", sheet_name=None)
df['Inventory_Stock']['date'] = df['Inventory_Stock']['date'].str.replace('/', '-')

for sheet_name, data in df.items():
    data.to_csv(f"{sheet_name}.csv", index=False)
    print(f"✅ {sheet_name}.csv → {len(data)} rows")