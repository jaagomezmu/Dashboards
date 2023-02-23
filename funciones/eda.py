def describe(data_frame, columna):
    """Describe a dataframe easily."""

    # remove any pre-existing indices for ease of use in the D-Tale code, but this is not required
    df = data_frame.reset_index().drop('index', axis=1, errors='ignore')
    df.columns = [str(c) for c in df.columns]  # update columns to strings in case they are numbers

    if df[columna].dtype != 'O':
        return ("","","","","")
    else:
        # main statistics
        stats = df[columna].describe()
        count = stats.loc['count']
        unique = stats.loc['unique']
        top = stats.loc['top']
        freq = stats.loc['freq']
        
        s = df[columna]
        s = s[s.isnull()]
        char_len = len(s)    
    
    return (count, unique, top, freq, char_len)

def make_series(data_frame, columna):
    """Define a series to plot with highcharts"""
    s = data_frame[~pd.isnull(data_frame[columna])][columna]
    chart = pd.value_counts(s.str.split(expand=True).stack())
    chart = chart.to_frame(name='data').sort_index()
    chart.index.name = 'name'
    chart = chart.reset_index().sort_values(['data', 'name'], ascending=[False, True])
    chart = chart[:100]
    chart = chart.reset_index(drop=True)
    chart = chart.to_dict(orient='list')
    # chart = chart.to_json()
    return chart

def make_num_series(data_frame, columna):
    """Define a series of numeric data to plot with highcharts"""
    s = data_frame[~pd.isnull(data_frame[columna])][columna]
    chart = s.to_list()
    return chart

def pie_data(data_frame):
    """Define 2 list of values to make a pie chart with highchart"""
    s = data_frame['MOTIVO_RETIRO'].value_counts(normalize=True)
    chart = s.to_dict()
    return chart

def card1_serie(data_frame):
    """Define 2 list of values to make a chart with highchart"""
    s = data_frame[['MOTIVO_RETIRO','TOTAL_SALARIO']]
    df = s.groupby(['MOTIVO_RETIRO']).mean()
    df1 = df.reset_index()
    chart = df1.to_dict(orient = 'list')
    return chart

def card2_serie(data_frame):
    """Define 2 list of values to make a chart with highchart"""
    s = data_frame[['MOTIVO_RETIRO','AÑOS_EN_LA_EMPRESA']]
    df = s.groupby(['MOTIVO_RETIRO']).mean()
    df1 = df.reset_index()
    chart = df1.to_dict(orient = 'list')
    return chart
    
    