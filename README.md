# Internet Access Data Analysis Project

## Project Overview

This project aims to analyze internet access data by merging datasets from the FCC and NCES. The primary goal is to understand internet accessibility at various levels, such as school districts, census tracts, and states. The project is conducted under the Realizing Rights Lab at Brown University.

## Folder Structure

### 1. `data_inputs`

Contains raw data files from the FCC and NCES:

- **`fbd_us_without_satellite_dec2021_v1.csv`**: FCC data on internet speeds for December 2021, excluding satellite data.
- **`LEAIDtoCensusTract_XWalk.xlsx`**: NCES crosswalk file for matching Local Education Agency IDs (LEAIDs) to Census Tracts.

### 2. `internet_access.ipynb`

This Jupyter Notebook contains the main workflow for data manipulation, wrangling, and analysis. It pulls custom functions from `my_functions.py`.

### 3. `my_functions.py`

A Python script containing reusable functions used in `internet_access.ipynb`.

### 4. `env.yaml`

Defines the project’s Python environment, including required packages and dependencies.

### 5. `data_outputs`

Stores the results of data manipulation and wrangling:

- **`internet_access_nonaggregated.csv`**: Processed data without aggregation.
- **`internet_access_aggregated/`**: Contains aggregated data at various levels:
  - `school_district_name`
  - `school_district_LEAID`
  - `county_level`
  - `census_tract_level`
  - `state_level`

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Jupyter Notebook
- Conda or a virtual environment manager

### Setup

1. Clone the repository or download the project files.
2. Create the environment:
   ```bash
   conda env create -f env.yaml
   conda activate <environment_name>
   ```
3. Open the Jupyter Notebook:
   ```bash
   jupyter notebook internet_access.ipynb
   ```

## Handling Leading Zeros in Data Outputs

When working with the output CSV files, note that leading zeros in some columns (e.g., `StateFIPS`, `LEADID`, `CensusTract`, `County`) may be dropped when the data is re-imported due to how Pandas and CSV files handle numerical data. To ensure consistency and preserve leading zeros, you must use the `pad_column_values` function.

A detailed explanation and example of how to correctly import and process the output data are provided in the `how_to_import_output_data.ipynb` file. This file includes code that resembles the following code snippet:

```python
# Example of re-importing output data while preserving leading zeros
from my_functions import pad_column_values

# Re-import CSV file
file_path = "data_outputs/internet_access_aggregated/school_district_name.csv"
data = pd.read_csv(file_path)

# Pad column values to ensure consistent character count
data = pad_column_values(data, "StateFIPS", target_length=12)
data.head(5)
```

Be sure to apply the `pad_column_values` function to any columns requiring a fixed character length to maintain data integrity.

## Data Sources

- **FCC**: [Federal Communications Commission](https://www.fcc.gov/)
- **NCES**: [National Center for Education Statistics](https://nces.ed.gov/)

## Results

The results of this project provide insights into internet accessibility across different administrative and geographic levels. They are stored in the `data_outputs` folder, with both non-aggregated and aggregated formats for flexibility in analysis.

## Acknowledgments

This project was conducted as part of the Realizing Rights Lab, Brown University.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Disclaimer

This project is provided "as is," without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, or non-infringement. The authors and contributors are not liable for any claims, damages, or other liabilities arising from the use of the data or analysis. Use of this project and its outputs is at your own risk.

For questions or further information, contact the Realizing Rights Lab at Brown University.

