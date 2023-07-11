from textfsm import clitable
#import Clitable
#from Clitable import cli_table

# Create a CLI Table instance
cli_table = clitable.CliTable()

# Define the template file
template_file = "NAN0184ASW01.template"

# Load the template file
cli_table.load_template(template_file)

# Read the log file contents
with open("NAN0184ASW01_10.239.119.26_S3100-28FC.txt") as f:
    log_content = f.read()

# Parse the log content using the template
parsed_data = cli_table.ParseText(log_content)

# Process and print the parsed data
table_rows = []
header_row = cli_table.header
for parsed_row in parsed_data:
    table_row = [parsed_row[field] for field in header_row]
    table_rows.append(table_row)

# Print the table header
print(header_row)

# Print the table rows
for row in table_rows:
    print(row)
