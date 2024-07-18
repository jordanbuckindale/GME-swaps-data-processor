# GME Swaps Data Processor

This repository hosts Python scripts designed to process swaps data related to GameStop (GME) from the DTCC (Depository Trust & Clearing Corporation) public data API.

## Overview

The project involves Python scripts to download and process large volumes of data, pulled dfrom public data API. The DTCC provides a user guide for their dashboard [here](https://kgc0418-tdw-data-3.s3.amazonaws.com/gtr/static/gtr/docs/RT_PPD_quick_ref_guide.pdf). While their website includes a search feature, it's limited by date range and output size constraints, prompting a focus on Python scripting via their API.

## Features

- Automated download of daily equity reports in ZIP format.
- Extraction of CSV files from ZIP archives for further analysis.
- Ability to process and filter data related to GME swaps.

## Usage

### Prerequisites

- Python 3.x
- `requests` library

Install the required library using pip:
```bash
pip install requests
