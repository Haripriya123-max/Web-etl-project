import pandas as pd

df = pd.read_csv("raw_data.csv")

# Remove currency symbols and unwanted characters
df["price"] = (
    df["price"]
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .astype(float)
)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove missing values
df.dropna(inplace=True)

df.to_csv("clean_data.csv", index=False)
print("Data cleaned successfully")
