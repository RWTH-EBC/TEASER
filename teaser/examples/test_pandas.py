import ipdb
import pandas as pd
asd = ["asd", "asd1", "asd3"]

export = pd.DataFrame(
    index=pd.date_range(
        '2019-01-01 00:00:00',
        periods=8760,
        freq='H').to_series().dt.strftime('%m-%d %H:%M:%S'),
    columns=[zone for zone in asd])
export.index = [(i + 1) * 3600 for i in range(8760)]
with open('path.csv', 'a') as f:
    f.write('#1\n')
    f.write('double Tset({}, {})\n'.format(
        8760, len(asd) + 1))
    export.to_csv(
        f,
        sep='\t',
        header=False,
        index_label=False)
ipdb.set_trace()  # Break Point ###########
