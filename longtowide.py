
import pandas as pd

df = pd.read_excel('C:\\Users\\v870603\\Documents\\Data\\Fitabase Data 4.12.16-5.12.16\\dailyCalories_merged.xlsx')

# Converting long data to wide data
df_wide = df.pivot(index = 'Id', columns = 'ActivityDay', values = 'Calories')

df_wide.to_excel(r'C:\\Users\\v870603\\Documents\\Data\\Fitabase Data 4.12.16-5.12.16\\dailyCalories_merged_wide.xlsx', sheet_name='dailyCalories_merged_wide', index = True)

print(df_wide)

"""
# Converting wide data to long data
df_long = pd.melt(df_wide, id_vars = ['Id'], var_name = 'ActivityDay', values = 'Calories')

"""
