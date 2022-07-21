import yaml

fname = "data.yaml"

# choose a loader
loader = yaml.BaseLoader    # basic loader
# loader = yaml.FullLoader  # more advanced loader

# Open and deserialize the YAML file
with open(fname, "rt") as yaml_file: 
    yaml_data = yaml.load(yaml_file, Loader=loader) 


# Print the information about the deserialized data
print("Type of the loaded data is: ", type(yaml_data), "\n")
print("Contents of the YAML file:")
print("--------------------------")
print( yaml.dump(yaml_data, indent=4) )
print("\n")


# iterate over the items and print them
width = 40 
for key, value in yaml_data.items(): 
    print(f"{str(key):40}  {type(key)}")
    print(f"{str(value):40}  {type(value)}")
    print()

print()
print(yaml_data["PalMod_Date"])
print(yaml_data["foo"]["bar"]["fizz"]["buzz"])
print(yaml_data["models"][-1])
