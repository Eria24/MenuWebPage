import base64

# Replace 'menu.xlsx' with your actual Excel file path
file_path = r"C:\Users\HP\Desktop\Menu\menu.xlsx"

with open(file_path, "rb") as file:
    encoded_string = base64.b64encode(file.read()).decode("utf-8")

# Print or save the Base64 string
print(encoded_string)
