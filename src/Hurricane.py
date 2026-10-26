# %% [markdown]
# ## Hurricane Tracking Workflow
# This notebook selects trackpoints from a features class of trackpoints for a selected storm (season & name), creates a track line, and extracts US counties that intersect that trackline. 
# 
# Fall 202X  
# John.Fay@duke.edu

# %%
#Import package
import arcpy
from pathlib import Path

#Set paths
raw_folder_path = Path.cwd().parent / 'data' / 'raw'
processed_folder_path = Path.cwd().parent / 'data' / 'processed'

#Arcpy environment settings
arcpy.env.workspace = str(raw_folder_path)
arcpy.env.overwriteOutput = True

# %%
#Set storm variable
storm_season = 2024
affected_counties = processed_folder_path / 'affected_counties.shp'

#Set model layers
ibtracs_NA_points = str(raw_folder_path /'IBTrACS_NA.shp')
usa_counties = 'https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/USA_Counties_Generalized_Boundaries/FeatureServer/0'
storm_track_points =  "memory\\track_points"
storm_track_line = "memory\\Tracklines"

#%% 
#Create list of unique storm names from IBTracts feature class for the year 2000
#ai: storm_names = [row[0] for row in arcpy.da.SearchCursor(ibtracs_NA_points, ['NAME'], where_clause="SEASON = 2000")]
storm_dict = {} #create dictionary 

for storm_season in range(2000, 2004):
    storm_names = []
    #create ist of storm names for the season 2000
    cursor = arcpy.da.SearchCursor(
    in_table = ibtracs_NA_points,
    field_names = ['NAME'], 
    where_clause = f'SEASON = {storm_season}'
)
    #iterate through rows in the cursor
    for row in cursor: 
        storm_name = row[0]
        if not storm_name in storm_names and storm_name !='UNNAMED':
            storm_names.append(storm_name)
            print(storm_name)

del cursor
storm_dict[storm_season] = storm_names


# %%
#Iterate and tally storm county counts
for storm_season in storm_dict.keys():
    #initialize storm count
    storm_count_total = 0
    for storm_name in storm_dict[storm_season]:
        arcpy.analysis.Select(
            in_features=ibtracs_NA_points, 
            out_feature_class=storm_track_points, 
            where_clause=f"SEASON = {storm_season} And NAME = '{storm_name}'"
        )
        arcpy.management.PointsToLine(
            Input_Features=storm_track_points,
            Output_Feature_Class=storm_track_line,
            Sort_Field='ISO_TIME'
        )

        select_output = arcpy.management.SelectLayerByLocation(
            in_layer=usa_counties, 
            overlap_type="INTERSECT", 
            select_features=storm_track_line, 
            )
        select_result = select_output.getOutput(0)
        county_count = int(arcpy.management.GetCount(select_result).getOutput(0))
        storm_count_total+= county_count
        out_file.write(f'{storm_season}, {season_counter}\n')
        
    break

#%% print the count

