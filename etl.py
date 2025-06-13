import pandas as pd
import match

# E
df = pd.read_csv(sample_product.csv)

# T
df["unit_price"] = df["unit_price"].apply(match.ceil)

# L
df.to_csv("output/clern_produce.csv", index="False")
