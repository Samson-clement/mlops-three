import os
import gdown

# Define the Google Drive folder URL
drive_url = "https://drive.google.com/drive/u/0/folders/1QP-gY9Ne9EIFN_Pvo9BZSLmpfrJj04MP"

# Target output file
output_file = "data_raw.csv"

print(f"Downloading data from Google Drive to {output_file}")

# Using folder download but specifying output directory as current directory
gdown.download_folder(url=drive_url, quiet=False, output="./", use_cookies=False)

# Check if the file exists in the expected location (remote folder)
remote_path = os.path.join("remote", "data_raw.csv")
if os.path.exists(remote_path):
    # Move the file to the current directory
    os.rename(remote_path, output_file)
    print(f"Successfully moved file to {output_file}")
    
    # Display first few lines of the CSV
    try:
        with open(output_file, 'r') as f:
            first_lines = ''.join([f.readline() for _ in range(3)])
            print(f"\nFirst few lines of {output_file}:")
            print(first_lines)
    except Exception as e:
        print(f"Could not read the file: {e}")
    
    # Clean up by removing the remote directory if it's empty
    if os.path.exists("remote") and not os.listdir("remote"):
        os.rmdir("remote")
else:
    print(f"File not found at expected location: {remote_path}")
    
    # Look for the file in other locations
    for root, dirs, files in os.walk("."):
        for file in files:
            if file == "data_raw.csv":
                file_path = os.path.join(root, file)
                print(f"Found file at: {file_path}")
                if file_path != output_file:
                    os.rename(file_path, output_file)
                    print(f"Moved file to {output_file}")