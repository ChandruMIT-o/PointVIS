# FIX ME - import lookup_table.py
import numpy
import pandas


table = read_table()
objects = table["objectID"].unique()

def objectMerge():
    for objectID in objects:
        object_df = table[table['objectID'] == objectID]
        
        for i in range(len(object_df)):
            for j in range(i+1, len(object_df)):
                object1 = object_df.iloc[i]
                object2 = object_df.iloc[j]

                # Inter Centroid Distance
                icd = np.sqrt((object1["x_centroid"] - object2["x_centroid"])**2 + 
                              (object1["y_centroid"] - object2["y_centroid"])**2 + 
                              (object1["z_centroid"]- object2["z_centroid"])**2)

                # Read the 2 files 
                df1 = pd.read_csv(object1["file_path"])
                df2 = pd.read_csv(object2["file_path"])

                radius1 = np.max(np.sqrt((df1['X'] - object1["x_centroid"])**2 + 
                                         (df1['Y'] - object1["y_centroid"])**2 + 
                                         (df1['Z'] - object1["z_centroid"])**2))

                radius2 = np.max(np.sqrt((df2['X'] - object2["x_centroid"])**2 + 
                                        (df2['Y'] - object2["y_centroid"])**2 + 
                                        (df2['Z'] - object2["z_centroid"])**2))
                
                r = max(radius1, radius2)

                if icd <= r:
                    # df = pd.concat(df1, df2)
                    # del df1, df2
                    # Write contents of df into the file path - object1["file_path"]

                    # Delete the entry of object2 in lookup table - delete_row(object2["objectID"], object2["instanceID"])

                    # Calculate value of new centroid and update lookuptable - mean of x, y, z cols 

                    # Update the new centroid into lookup table
                    # edit_row(objectID, instanceID, class_name, x_centroid, y_centroid, z_centroid, file_path, volume=-1, surface_area=-1)
                    pass
