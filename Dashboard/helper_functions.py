import pandas as pd

def combine_raw_data(start=9, end=21, write=False, file_root='raw_data/season-x.csv', out_file='data/csv_data/raw_combined.csv'):
    """
    This is a helper function that appends all Premier League season datafiles
    into one pandas DataFrame.

    Start at season 2009 and end on season 2021. Write is defaulted to False but
    when True this function will save the combined DataFrame into a csv file.
    """
    df = pd.DataFrame()
    for i in range(start, end+1):
        curr_file = file_root.replace('x', str(i) + str(i+1))

        curr_df = pd.read_csv(curr_file)

        if 'Time' in curr_df.columns:
            curr_df.drop(['Time'], axis=1, inplace=True)

        #make sure that we only get subset [:24] of columns
        curr_df = curr_df.iloc[:, :23]

        curr_df['Season'] = i
        #append all the dataframes together
        df = pd.concat([df, curr_df]).reset_index(drop=True)
    if write:
        df.to_csv(out_file, index=False)
        print('Wrote combined data frame to: ', out_file)
    return df

def build_table(df):
    """
    This is a helper function that builds season stats from a dataframe. This
    function takes in a dataframe of results and returns a dictionary that
    displays wins, losses, draws, Goals scored and goals conceded for each
    team in the original dataframe.
    """
    table_dic = {}
    poss_res = ['H', 'A', 'D']
    for name, group in df.groupby('HomeTeam'):
        table_dic[name] = {}
        results_dic = group['FTR'].value_counts().to_dict()

        miss = set(poss_res).difference(list(results_dic.keys()))
        while miss:
            curr = miss.pop()
            results_dic[curr] = 0

        table_dic[name]['W'] = results_dic['H']
        table_dic[name]['D'] = results_dic['D']
        table_dic[name]['L'] = results_dic['A']
        table_dic[name]['GF'] = sum(group['FTHG'])
        table_dic[name]['GA'] = sum(group['FTAG'])

    for name, group in df.groupby('AwayTeam'):
        results_dic = group['FTR'].value_counts().to_dict()

        miss = set(poss_res).difference(list(results_dic.keys()))
        while miss:
            curr = miss.pop()
            results_dic[curr] = 0

        table_dic[name]['W'] = table_dic[name]['W'] + results_dic['A']
        table_dic[name]['D'] = table_dic[name]['D'] + results_dic['D']
        table_dic[name]['L'] = table_dic[name]['L'] + results_dic['H']

        table_dic[name]['GF'] = table_dic[name]['GF'] + sum(group['FTAG'])
        table_dic[name]['GA'] = table_dic[name]['GA'] + sum(group['FTHG'])
    return table_dic

def build_df_from_table(dic_table):
    """
    Helper function that returns a DataFrame built from the returned dictionary
    in build_table.
    """
    data = {}
    for team in dic_table.keys():
        data[team] = dic_table[team].values()
    cols = dic_table[team].keys()
    df = pd.DataFrame.from_dict(data, orient='index', columns=cols)
    df['GD'] = df['GF'] - df['GA']
    df['Pts'] = (3 * df['W']) + df['D']
    df = df.sort_values(by=['Pts', 'GD', 'GF'], ascending=False)
    df['Place'] = range(1, df.shape[0]+1)
    return df

def write_standings(df, file_root='data/csv_data/standings-x.csv'):
    """
    Helper function that writes the current standings dataframe into a csv file.
    """
    for szn, group in df.groupby('Season'):
        #get the output file name replacing with season years
        file_name = file_root.replace('x', str(szn) + str(szn+1))
        curr_df = build_df_from_table(build_table(group))
        print('Writing standings for 20' + "{0:0=2d}".format(szn) + '-' + str(szn+1) +
              ' season to file: ' + file_name)
        curr_df.to_csv(file_name)
