import subprocess

# File names
receptor_pdbqt = "4ey7_cleaned.pdbqt"
ligand_pdbqt = "ligand_prepared.pdbqt"
config_txt = "vina_config.txt"
output_pdbqt = "docked_output.pdbqt"
log_file = "docking_log.txt"

# Step 1: Write config file
print("[INFO] Writing Vina config file...")
center = "-14.23 -43.79 27.57"  # Coordinates from Chimera (centroid of original ligand)
size = "20 20 20"  # Grid box size
with open(config_txt, "w") as f:
    f.write(f"receptor = {receptor_pdbqt}\n")
    f.write(f"ligand = {ligand_pdbqt}\n")
    f.write(f"center_x = {center.split()[0]}\n")
    f.write(f"center_y = {center.split()[1]}\n")
    f.write(f"center_z = {center.split()[2]}\n")
    f.write(f"size_x = {size.split()[0]}\n")
    f.write(f"size_y = {size.split()[1]}\n")
    f.write(f"size_z = {size.split()[2]}\n")
    f.write(f"out = {output_pdbqt}\n")
    f.write(f"log = {log_file}\n")

# Step 2: Run AutoDock Vina
print("[INFO] Running AutoDock Vina...")
subprocess.run(["vina", "--config", config_txt])

print("[✓] Docking complete!")
