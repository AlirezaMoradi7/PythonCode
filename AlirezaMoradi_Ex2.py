import pandas as pd

# داده‌های نمونه
# ساخت DataFrame
df = pd.read_csv('HouseNew.csv')
#
# # کدگذاری دستی مقادیر رشته‌ای
def manual_label_encoding(column):
    unique_values = list(set(column))
    encoding_map = {val: idx for idx, val in enumerate(unique_values)}
    return column.map(encoding_map), encoding_map
#
# # کدگذاری ستون‌های رشته‌ای
df["lable_Address"], feature_1_map = manual_label_encoding(df["Address"])
# df["feature_3_encoded"], feature_3_map = manual_label_encoding(df["feature_3"])
#
# # بررسی همبستگی بین ویژگی‌ها و متغیر هدف
correlations = {}
for col in ["lable_Address", "Area", "Room","Elevator","Floor","Parking","Warehouse","YearOfConstruction"]:
    correlation = df[col].corr(df["Price"])
    correlations[col] = correlation
    # print(correlations[col])

# # نمایش ویژگی‌های با همبستگی بالا
selected_features = [feature for feature, corr in correlations.items() if abs(corr) > 0.2]
#
# # ساخت DataFrame نهایی
df2 = pd.DataFrame(correlations.items())
df2.columns = ["home_feature", "correlation"]
sorted_df2=df2.sort_values(by='correlation',ascending=False)
print(sorted_df2)

