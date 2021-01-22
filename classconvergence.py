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

def classconvergence_particles(data_star_files):
    """Build a DataFrame of class populations as a function of iteration."""
    counts = [ count_particles(df['particles']) for df in data_star_files ]
    for (count, it) in zip(counts, range(0, len(counts))):
        count['iteration'] = it
    table = pd.concat(counts)
    table.reset_index(inplace=True)
    table.set_index('iteration', inplace=True)
    return table
