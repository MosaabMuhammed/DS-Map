import numpy as np
import pandas as pd
from pandas.api.types import is_string_dtype, is_numeric_dtype, is_categorical_dtype
import matplotlib.pyplot as plt
from termcolor import colored
from scipy import stats
import inspect, os, random
import operator as op
from functools import reduce
import IPython
from tabulate import tabulate

#####################################
#       Color the background        #
#####################################
def bg(value, type='num', color='blue'):
    value = str('{:,}'.format(value)) if type == 'num' else str(value)
    return colored(' ' + value + ' ', color, attrs=['reverse', 'blink'])

#####################################
#        Print variable name        #
#####################################
# Credits: https://stackoverflow.com/questions/18425225/getting-the-name-of-a-variable-as-a-string
def var2str(var):
    """
    Gets the name of var. Does it from the out most frame inner-wards.
    :param var: variable to get name from.
    :return: string
    """
    for fi in reversed(inspect.stack()):
        names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
        if len(names) > 0:
            return names[0]

##############################################
#      Print Shape of multiple variables     #
##############################################
def shape(*args):
    all_dfs = []
    for df in args:
        if isinstance(df, list):
            n_columns = bg(1)
            n_rows    = bg(len(df))
        else:
            n_columns = f"~{bg(1 if len(df.shape) <= 1 else df.shape[1])}"
            n_rows    = f"~{bg(df.shape[0])}"
        all_dfs.append([var2str(df), str(n_rows), str(n_columns)])
            
    print(tabulate(all_dfs, headers=["Dataframe", "n_rows", "n_columns"], tablefmt="grid"))
    
#####################################
#           Summary  Table          #
#####################################
def summary(df, sort_col=None):
    def color_True_red(val):
        color, back = ('white', 'red') if val == True else ('black', 'white')
        return f'background-color: {back}; color: {color}'

    summary = pd.DataFrame({'dtypes': df.dtypes}).reset_index()
    summary.columns = ['Name', 'dtypes']
    summary['Uniques'] = df.nunique().values
    summary['Missing'] = df.isnull().sum().values
    summary['% Missing'] = round(100 * summary['Missing'] / df.shape[0], 2)
    summary['has_Infinite'] = df.isin([np.inf, -np.inf]).all(axis='rows').values

    summary['has_Negative'] = [True if is_numeric_dtype(df[col]) and (df[col] < 0).any() else False for col in df]
    summary['top_Frequent'] = df.apply(lambda x: x.value_counts().index[0] if int(x.nunique()) else 0).values
    summary['% frequent'] = df.apply(lambda x: x.value_counts(normalize=True).values[0] if int(x.nunique()) else 0).values
    # summary['Max'] = df.apply(lambda x: max(x) if x.dtype != 'O' else max(x.values, key=list(x.values).count)).values
    # summary['Min'] = df.apply(lambda x: min(x) if x.dtype != 'O' else min(x.values, key=list(x.values).count)).values

    summary = summary.sort_values(by=[sort_col], ascending=False) if sort_col else summary

    # Print some smmaries.
    print(f'~> Dataframe has {bg(df.shape[0])} Rows, and {bg(df.shape[1])} Columns.')
    print(f'~> Dataframe has {bg(summary[summary["Missing"] > 0].shape[0], color="red")} Columns have [Missing] Values.')
    print('---' * 20)
    for type_name in np.unique(df.dtypes):
        print(f'~> There are {bg(df.select_dtypes(type_name).shape[1])}\t Columns that have [Type] = {bg(type_name, "s", "green")}')

    print('---' * 20)
    return summary.style.applymap(color_True_red, subset=['has_Negative', 'has_Infinite']) \
                        .format({'% frequent': "{:.2%}", 'Uniques': "{:,}", 'Missing': '{:,}'}) \
                        .background_gradient(cmap='summer_r')


#####################################
#        Reduce Memory Usage        #
#####################################
def reduce_mem_usage(df, verbose=True):
    if verbose:
        start_mem = df.memory_usage().sum() / 1024**2
    
    n_cols = len(df.columns)
    for i, col in enumerate(df.columns, 1):
        percent = 100.*i/n_cols
        print(f"\rProgress: {percent:.2f}%", end='')
        col_type = df[col].dtype
        if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()

            if str(col_type)[:3] == 'int' or np.all(np.mod(df[col], 1) == 0):
                # Booleans mapped to integers
                if list(df[col].unique()) == [1, 0]:
                    df[col] = df[col].astype(bool)
                elif c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.uint8).min and c_max < np.iinfo(np.uint8).max:
                    df[col] = df[col].astype(np.uint8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.uint16).min and c_max < np.iinfo(np.uint16).max:
                    df[col] = df[col].astype(np.uint16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.uint32).min and c_max < np.iinfo(np.uint32).max:
                    df[col] = df[col].astype(np.uint32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
                elif c_min > np.iinfo(np.uint64).min and c_max < np.iinfo(np.uint64).max:
                    df[col] = df[col].astype(np.uint64)
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
        # Comment this if you have NaN value in this column.
        # else:
        #     df[col] = df[col].astype('category')

    if verbose:
        end_mem = df.memory_usage().sum() / 1024 ** 2
        print(f"\n~> Memory usage reduced from {start_mem:.3f} MG to {end_mem:.3f} MG by {(100 * (start_mem - end_mem) / start_mem):.1f}%")
        print('---' * 20)
    return df

#####################################
#          Show Annotations         #
#####################################
def show_annotation(dist, n=5, size=14, total=None):
    sizes = []  # Get highest value in y
    for p in dist.patches:
        height = p.get_height()
        sizes.append(height)

        dist.text(p.get_x() + p.get_width() / 2.,          # At the center of each bar. (x-axis)
                  height + n,                            # Set the (y-axis)
                  '{:1.2f}%'.format(height * 100 / total) if total else '{}'.format(height),  # Set the text to be written
                  ha='center', fontsize=size)
    dist.set_ylim(0, max(sizes) * 1.15)  # set y limit based on highest heights

#####################################
#          dd for debuging          #
#####################################
def dd(*args):
    print('--' * 20)
    for x in args:
        varName = colored(var2str(x), attrs=['blink'])
        # Get the type of the variable.
        try:
            print(f"~> Type  of {varName}: {colored(type(x), 'green')}")
        except:
            print(f"~> Can't get the {colored('type', 'green')} of {varName}")

        # Get the shape of the variable.
        try:
            print(f"~> Shape of {varName}: {colored(str(x.shape), 'blue')}")
        except:
            print(f"~> Length of {varName}: {colored(str(len(x)), 'blue')}")

        # Get the first value of the variable.
        try:
            print(f"~> First Value of {varName}: {x[0]}")
        except:
            if type(x) is type(pd.DataFrame()) or type(x) is type(pd.Series):
                print(f"~> First Row of {varName}: \n\n{x.iloc[0]}")
            elif type(x) is type(dict()):
                print(f"~> Can't show the first value of a {colored('dictionary', 'red')}.")
        print('--' * 20)

#####################################
#        Read & write Feather       #
#####################################
def read_feather(path):
    # Read
    df = pd.read_feather(path)

    # Remove the redundant columns. [index]
    df.drop('index', axis=1, inplace=True)
    df = reduce_mem_usage(df, verbose=False)
    return df

def write_feather(df, path):
    df.reset_index().astype('float32', errors='ignore').to_feather(path)


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom


#####################################
#        Display Multiple dfs       #
#####################################
def display(*dfs, head=True):
    for df in dfs:
        print(f'{bg(var2str(df), "S")} Table')
        IPython.display.display(df.head() if head else df)
        print('\n')


#####################################
#           Progress bar            #
#####################################
def progress_bar(iteration, total, size=30):
    running = iteration < total
    c = ">" if running else "="
    p = (size - 1) * iteration // total
    fmt = "{{:-{}d}}/{{}} [{{}}]".format(len(str(total)))
    params = [iteration, total, "=" * p + c + "." * (size - p - 1)]
    return fmt.format(*params)

#####################################
#              Set Seed             #
#####################################
def set_seed(seed: int=42, tf_flag: bool=False) -> int:
    os.environ['PYTHONHASHSEED'] = str(seed)
    os.environ['TF_DETERMINISTIC_OPS'] = '1'
    os.environ['TF_KERAS'] = '1'
    np.random.seed(seed)
    random.seed(seed)
    if tf_flag: tf.random.set_seed(seed)
    return seed

