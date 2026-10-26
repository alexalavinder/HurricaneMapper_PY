---
Title: Hurricane Mapper
Author: John.Fay@duke.edu
Date: Fall 2025
Name: Alexa Lavinder
Repository forked from https://github.com/ENV859/HurricaneMapper_PY  
---

# HurricaneMapper_PY

This workspace contains a Python-based geoprocessing workflow of the Hurricane Mapping tool created in the Advanced Geoprocessing section of [ENV859](https://env859.github.io). 

The workflow, represented in the `HurricaneTracker.ipynb` notebook, allows the user to specify a storm season (e.g. 2018) and named storm from that season (e.g. "FLORENCE"), and create an output  feature class of the US counties affected by that storm. 

The workspace structure is as follows:

```text
[Project Folder] 
		|
		├ data 
		|	|
		|	├ raw
		|	|	|
		|	|	└ IBTrACS_NA.zip (IBTrACS shapefile of storm track points - compressed)
		|	|	
		|	└ processed
		|
		└ src
			|
			└ HurricaneTracker.ipynb (Jupyter notebook)
```

---

⚠️Note that the IBTrACS_NA shapefile should be unzipped directly into the `raw` folder before running the script.
