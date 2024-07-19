# %% download all data
#------------------------------------------------
# Jordan Buckindale
# Date: July 17
#
# The script performs the following tasks:
# - Initializes a start date.
# - Iterates through each day from the start date to the current date.
# - Constructs a URL based on the date to download a ZIP file containing cumulative equity reports.
# - Downloads the ZIP file and saves it locally in a data/ directory.
# - Moves to the next day and repeats the process until it reaches the current date.
#------------------------------------------------

import requests
import datetime

date = datetime.datetime(2024, 6, 27)

while date <= datetime.datetime.now():
    y = date.year
    m = date.month
    d = date.day

    print(f"downloading {y:04d}_{m:02d}_{d:02d}")

    url = f"https://pddata.dtcc.com/ppd/api/report/cumulative/sec/SEC_CUMULATIVE_EQUITIES_{y:04d}_{m:02d}_{d:02d}.zip"

    req = requests.get(url)

    zip_filename = "data/" + url.split("/")[-1]
    with open(zip_filename, "wb") as f:
        f.write(req.content)

    date += datetime.timedelta(days=1)

    req.close()
