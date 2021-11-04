import pandas as pd
from google.cloud import bigquery

def get_bq_table(table, date_partition_field, date_field, first_day, last_day, column=None):
    """Descarga una tabla de BQ en las fechas dadas.
    
    Args:
        table (str):                  URl de tabla BQ (ej: 'mllifecycledxc.landing_prodiq.prodiq_preparation')
        date_partition_field (str):   Campo de la tabla BQ que se utiliza para particionar
        date_field (str):             Campo de la tabla BQ que almacena la fecha
        first_day (str):              Primer día a descargar en formato YYYY-MM-DD
        last_dary (str):              Último día a descargar en formato YYYY-MM-DD
        column (str):                 Nombre de columna o columnas separadas por comas (por defecto, todas)
    
    Return:
        pd.DataFrame()
    """
    
    first_month_date = first_day.split("-")[0] + "-" + first_day.split("-")[1] + "-01"
    last_month_date = last_day.split("-")[0] + "-" + last_day.split("-")[1] + "-01"
    if column is None:
        select = "*"
    else:
        select = column
    
    query = f"""
    SELECT {select} FROM {table}
    WHERE DATE({date_partition_field}) >= "{first_month_date}" AND DATE({date_partition_field}) <= "{last_month_date}"
    AND DATE({date_field}) >= "{first_day}" AND DATE({date_field}) <= "{last_day}"
    ORDER BY {date_field} ASC"""
    client = bigquery.Client()
    result = client.query(query).to_dataframe()
    
    return result

def reduce_memory_usage(df, verbose=True):
    numerics = ["int8", "int16", "int32", "int64", "float16", "float32", "float64"]
    start_mem = df.memory_usage().sum() / 1024 ** 2
    for col in df.columns:
        col_type = df[col].dtypes
        if col_type in numerics:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == "int":
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                if (
                    c_min > np.finfo(np.float16).min
                    and c_max < np.finfo(np.float16).max
                ):
                    df[col] = df[col].astype(np.float16)
                elif (
                    c_min > np.finfo(np.float32).min
                    and c_max < np.finfo(np.float32).max
                ):
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
    end_mem = df.memory_usage().sum() / 1024 ** 2
    if verbose:
        print(
            "Mem. usage decreased to {:.2f} Mb ({:.1f}% reduction)".format(
                end_mem, 100 * (start_mem - end_mem) / start_mem
            )
        )
    return df

def import_data():
    """
    Front function to import data from the source/s
    
    Args:
        Whatever
        
    Returns:
        data (pd.DataFrame): a pandas dataframe with the raw data to train
    """
    data = pd.DataFrame()
    return data
