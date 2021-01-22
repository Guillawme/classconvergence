import os
import sys
import starfile as star
import pandas as pd

# Building blocks

def load_star_files(directory, pattern):
    """Load star files matching a given pattern from a given directory."""
    if not os.path.isdir(directory):
        sys.stderr.write("Error: the given path is not a directory.")
        sys.exit(1)
    else:
        files = os.listdir(directory)
        files.sort()
        full_files = [ directory + '/' + file for file in files ]
        dfs = [ star.open(file) for file in full_files if pattern in file ]
        return dfs

def count_particles(particles):
    """Count particles in each class."""
    particle_counts = particles[['rlnClassNumber']].value_counts()
    fractions_of_total = particles[['rlnClassNumber']].value_counts(normalize=True) * 100
    return pd.DataFrame({'count': particle_counts, 'fraction': fractions_of_total})
