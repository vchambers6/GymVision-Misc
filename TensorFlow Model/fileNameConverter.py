import os

def rename_files(directory):
    # Iterate over the files in the directory
    for filename in os.listdir(directory):
        # Split the filename into name and extension
        name, extension = os.path.splitext(filename)
        # Check if the filename matches the pattern
        if name.startswith("l_turn_"): #MARK: CHANGE HERE
            # Extract the number from the filename
            number = name.split("_")[-1]
            # Construct the new name
            new_name = f"v_LTurn_c{number.zfill(2)}{extension}" #MARK: CHANGE HERE
            # Rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            print(f"Renamed {filename} to {new_name}")

# Specify the directory containing the files
directory = "Skills Videos (AVI)/LTurn/" #MARK: CHANGE HERE

# Call the function to rename the files
rename_files(directory)

