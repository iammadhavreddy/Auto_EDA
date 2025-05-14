# Load the Data
# Import the pandas library
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv(r"C:/Users/Bharani Kumar/Desktop/Data Analytics/EDA_Module/education.csv")

# Auto EDA
# ---------
# Sweetviz
# Dtale
# Pandas Profiling

# Sweetviz
###########
# pip install sweetviz
import sweetviz as sv # Import the sweetviz library

# Analyze the DataFrame and generate a report
s = sv.analyze(df)

# Display the report in HTML format
s.show_html()


# D-Tale
########

# pip install dtale   # In case of any error then please install werkzeug appropriate version (pip install werkzeug==2.0.3)
import dtale
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv(r"C:/Users/Bharani Kumar/Desktop/Data Analytics/EDA_Module/education.csv")

# Display the DataFrame using D-Tale
d = dtale.show(df, host = 'localhost', port = 8000)

# Open the browser to view the interactive D-Tale dashboard
d.open_browser()


# Pandas Profiling
###################

# pip install --upgrade ydata-profiling
import pandas as pd
from ydata_profiling import ProfileReport
import os

# Generate and save EDA report
profile = ProfileReport(df, title = "Education", explorative = True)
output_file = "Education.html"
profile.to_file(output_file)

print(f"✅ Report saved at: {os.path.abspath(output_file)}") # Converting a Relative Path to an Absolute Path

# END OF MODULE
