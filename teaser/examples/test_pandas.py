import ipdb
import pandas as pd

seconds = [i + 1 * 3600 for i in range(8760)]
set_point = [293.15 for i in range(8760)]
index1 = pd.date_range(
    '2019-01-01 00:00:00',
    periods=8760,
    freq="H").to_series().dt.strftime('%m-%d %H:%M:%S')


schedule = pd.DataFrame(
    index=index1,
    data={'time in seconds': seconds, 'set point heat': set_point})
ipdb.set_trace()  # Break Point ###########
None
