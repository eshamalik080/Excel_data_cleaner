import pandas as pd
import matplotlib.pyplot as plt
import os

#--------------------------------
#Input /output files and folders
#--------------------------------
input_file = "input_data.xlsx"
outputDir = "output"

cleanedFile = os.path.join(outputDir, "cleaned_data.xlsx")
summaryFile = os.path.join(outputDir, "summary.xlsx")
chartFile = os.path.join(outputDir,  "sales.png")

#--------------
#Taking input
#--------------
os.makedirs(outputDir, exist_ok=True)

print("Loadig Excel file...")
df= pd.read_excel(input_file)

print("Original rows= ", len(df))

#---------------
#Data Cleaning
#---------------

print("Cleaning data... ")

df = df.drop_duplicates()

df = df.dropna(subset=["Product"])

df["Quantity"] = df["Quantity"].fillna(0)
df['Price'] = df["Price"].fillna(df["Price"].mean())

print("Rows after cleaning: ", len(df))

#---------------------
#Data Transformation
#---------------------

df["Total_Sale"] = df["Quantity"]*df["Price"]

#----------------------
#Summary Report
#----------------------

total_rev = df["Total_Sale"].sum()
average_sale = df["Total_Sale"].mean()
top_product = df.groupby("Product")["Total_Sale"].sum().idxmax()

summar_df = pd.DataFrame({
    "Metric": ["Total Revenue", "Average Sale", "Top Selling Products"],
    "Value": [round(total_rev, 2), round(average_sale, 2), top_product]
})

#------------------------
#Save clened excel file
#------------------------
df.to_excel(cleanedFile, index=False)
summar_df.to_excel(summaryFile, index=False)

#------------------------
#Visualization
#------------------------
print("Creating charts...")

plt.figure(figsize=(8,5))
df.groupby("Category")["Total_Sale"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(chartFile)
plt.close()

print("Process completed successfully!!!")