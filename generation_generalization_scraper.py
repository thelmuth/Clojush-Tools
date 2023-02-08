import pandas as pd
import re
import os

# Will not collect values for this data
IGNORE_KEYS = [';; -*- Generalization experiment info', 'Current time', 'Initialization',
               'Reproduction', 'Fitness Testing', 'Report', 'Other']


def generation_scraper(file_path):
    """Collects a list of dicts that contain necessary info for each generation."""

    with open(file_path) as f:
        file_lines = f.readlines()

    log_number = re.search('\d+', file_path.name).group(0)

    generations = []

    # Track whether lines being scanned are within a generation report
    in_report = False

    for line in file_lines:
        # Start a generation
        if bool(re.search('Report at generation (\d+)', line)):
            in_report = True
            gen_number = re.search('Report at generation (\d+)', line).group(1)
            generation_data = {'log': log_number, 'generation': gen_number}

        # End a generation
        elif bool(re.search('End of report for generation (\d+)', line)):
            in_report = False
            generations.append(generation_data)

        # Save data point for this generation
        elif in_report and ':' in line and line.split(':', 1)[0].strip() not in IGNORE_KEYS:
            key = line.split(':')[0].strip()
            value = line.split(':', 1)[1].strip()
            value = value.replace('seconds', '').strip()
            generation_data[key] = value

    return generations


def generalization_scraper(file_path):

    with open(file_path) as f:
        file_text = f.read()

    log_number = re.search('\d+', file_path.name).group(0)

    experiments = re.findall('experiment generalization info (.*)', file_text)
    total_errors = re.findall('Test total error for best: (.*)', file_text)
    assert(len(experiments) == len(total_errors))

    results = []

    for experiment, total_error in zip(experiments, total_errors):
        results.append({'log': log_number, 'experiment': experiment, 'total error': total_error})

    return results


def apply_scraper_to_directory(dir_path, scraper):
    all_logs = []
    for entry in sorted(os.scandir(dir_path), key=lambda e: e.name):
        if entry.is_file() and entry.name.startswith('log'):
            all_logs.extend(scraper(entry))
    return all_logs


# Main ###############################################################################

def main():
    generation_df = pd.DataFrame(apply_scraper_to_directory('logs', generation_scraper))
    generation_df.to_csv('generations.csv', index=False)


    generalize_df = pd.DataFrame(apply_scraper_to_directory('logs', generalization_scraper))
    generalize_df.to_csv('generalization.csv', index=False)
