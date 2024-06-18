import pandas as pd

csv_file = 'lookup_table.csv'

def initialise_lookup_table():
    df = pd.DataFrame(columns=['objectID', 'instanceID', 'class_name', 'x_centroid', 'y_centroid', 'z_centroid', 'volume', 'surface_area', 'file_path'])
    df.to_csv(csv_file, index=False)
    print("Lookup table initialized.")

def add_row(objectID, instanceID, class_name, x_centroid, y_centroid, z_centroid, file_path, volume=-1, surface_area=-1):
    df = pd.read_csv(csv_file)
    if df[(df['objectID'] == objectID) & (df['instanceID'] == instanceID)].empty:
        new_row = pd.DataFrame([{
            'objectID': objectID,
            'instanceID': instanceID,
            'class_name': class_name,
            'x_centroid': x_centroid,
            'y_centroid': y_centroid,
            'z_centroid': z_centroid,
            'volume': volume,
            'surface_area': surface_area,
            'file_path': file_path
        }])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(csv_file, index=False)
        print("Row added successfully.")
    else:
        print("Row with given objectID and instanceID already exists.")

def edit_row(objectID, instanceID, class_name, x_centroid, y_centroid, z_centroid, file_path, volume=-1, surface_area=-1):
    df = pd.read_csv(csv_file)
    index = df[(df['objectID'] == objectID) & (df['instanceID'] == instanceID)].index
    if not index.empty:
        df.loc[index, ['class_name', 'x_centroid', 'y_centroid', 'z_centroid', 'volume', 'surface_area', 'file_path']] = [class_name, x_centroid, y_centroid, z_centroid, volume, surface_area, file_path]
        df.to_csv(csv_file, index=False)
        print("Row updated successfully.")
    else:
        print("Row with given objectID and instanceID not found.")

def delete_row(objectID, instanceID):
    df = pd.read_csv(csv_file)
    index = df[(df['objectID'] == objectID) & (df['instanceID'] == instanceID)].index
    if not index.empty:
        df = df.drop(index)
        df.to_csv(csv_file, index=False)
        print("Row deleted successfully.")
    else:
        print("Row with given objectID and instanceID not found.")

def read_table():
    df = pd.read_csv(csv_file)
    return df

