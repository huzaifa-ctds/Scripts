import yaml
import subprocess
from itertools import islice

# Load the YAML mapping file
mapping_file = 'map_file_name'   #update the name/path of the file for salt-minions creation
with open(mapping_file, 'r') as file:
    vm_map = yaml.safe_load(file)

# Function to create batches
def batch_generator(data, batch_size):
    it = iter(data)
    for item in it:
        yield [item] + list(islice(it, batch_size - 1))

# Extract VM names
vm_names = []
for service, instances in vm_map.items():
    for instance in instances:
        vm_names.extend(instance.keys())

# Define batch size
batch_size = 10

# Generate and execute batches
for batch in batch_generator(vm_names, batch_size):
    # Formulate the salt-cloud command for the current batch
    cmd = ['salt-cloud', '-P', '-m', mapping_file] + batch
    # Execute the command
    print(f"Executing: {' '.join(cmd)}")  # Debug: Show the command
    subprocess.run(cmd)  # Execute the command

# Note: Depending on your environment, you might need to adjust the subprocess.run command to fit your needs.
