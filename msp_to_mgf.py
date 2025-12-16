from matchms.importing import load_from_msp
from matchms.exporting import save_as_mgf
import os
import argparse 

parser = argparse.ArgumentParser() 

parser.add_argument("inputfile", help="Input .msp file")
args = parser.parse_args() 

# Define the input and output file paths
input_msp_file = args.inputfile #"your_library.msp"
output_mgf_file = args.inputfile.replace('msp', 'mgf') #"converted_library.mgf"

# 1. Load the spectra from the MSP file
# load_from_msp returns a generator, so we convert it to a list
try:
    spectrums = list(load_from_msp(input_msp_file))
    print(f"Loaded {len(spectrums)} spectra from {input_msp_file}")

    # Optional: Apply filters (cleaning, normalization, etc.) to the spectra before saving
    # from matchms.filtering import default_filters
    # cleaned_spectrums = [default_filters(s) for s in spectrums]

    # 2. Save the spectrum objects as an MGF file
    save_as_mgf(spectrums, output_mgf_file)
    print(f"Successfully saved spectra to {output_mgf_file}")

except FileNotFoundError:
    print(f"Error: The file '{input_msp_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


