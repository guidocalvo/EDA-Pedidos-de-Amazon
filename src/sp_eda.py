# Tratamiento de datos
import pandas as pd
#---------------

#Visualización
import matplotlib.pyplot as plt
import seaborn as sns


def eda_preliminar (df):

    """
    Realiza un análisis exploratorio preliminar sobre un DataFrame dado.

    Este análisis incluye:
    - Muestra aleatoria de 5 filas del DataFrame.
    - Información general del DataFrame (tipo de datos, nulos, etc.).
    - Porcentaje de valores nulos por columna.
    - Conteo de filas duplicadas.
    - Distribución de valores para columnas categóricas.

    Parameters:
    df (pd.DataFrame): DataFrame a analizar.

    Returns:
    None
    """


    display(df.sample(5))

    print('-----------------')

    print('DIMENSIONES')

    print(f'Nuestro conjunto de datos presenta un total de {df.shape[0]} filas y {df.shape[1]} columnas.')

    print('-----------------')

    print('INFO')

    display(df.info())  

    print('-----------------')
    print('NULOS')

    display(df.isnull().sum() / df.shape[0] * 100)

    print('-----------------')
    print('DUPLICADOS')

    print(f'Tenemos un total de {df.duplicated().sum()} duplicados.')

    print('-----------------')
    print('FRECUENCIA CATEGÓRICAS')
    
    for col in df.select_dtypes(include= 'object').columns:
        print(col.upper())
        print(df[col].value_counts())
        print('-------')

    print('-----------------')
    print('ESTADÍSTICOS NUMÉRICAS')
    display(df.describe().T.round(2))


def analisis_rapido(df, n=5):
        
    """
    Función que proporciona un análisis rápido del dataframe.

    Parameters:
    df (pd.DataFrame): DataFrame a analizar.
    n: número de filas (por defecto = 5)

    Returns:
    None
    """

    print(f"Las {n} primeras filas son:")
    display(df.head(n))
    print("Información básica del dataframe:")
    display(df.info())

    print(f"El número de duplicados es: {df.duplicated().sum()}")
    print("\nValores nulos: ")
    display(df.isnull().sum())


def eda(df, n=2):
    """
    Función que proporciona un eda rápido del dataframe.

    Parameters:
    df (pd.DataFrame): DataFrame a analizar.
    n: número de filas (por defecto = 5)

    Returns:
    None
    """

    num_cols = df.select_dtypes(include='number').columns
    cat_cols = df.select_dtypes(include=['object','category']).columns

    print("Variables numércias:\n\n", num_cols)
    print("\nVariables categóricas:\n\n", cat_cols)

    print("Veamos las estadísticas básicas:\n")
    display(df.describe().T.round(n))
    display(df.describe(include = ['category', 'object']).T.round(n))

    for col in cat_cols:
        print(f" \n ----------- ESTAMOS ANALIZANDO LA COLUMNA: '{col}' -----------\n")
        print(f"Valores únicos: {df[col].unique()}\n")
        print("Frecuencia de los valores únicos de las categorías:")
        display(df[col].value_counts())


def grafico_pastel(df,col):

    """
    Función que proporciona un gráfico tipo pastel.

    Parameters:
    df (pd.DataFrame): DataFrame a analizar.
    col: columna para graficar.

    Returns:
    None
    """

    col_counts = df[col].value_counts()

    # Gráfico de pastel
    plt.figure(figsize=(6, 6))
    plt.pie(
        col_counts,
        labels=col_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        counterclock=False
    )
    plt.title(f'Distribution of {col}')
    plt.axis('equal')  # Para que sea un círculo
    plt.show()


def grafico_horizontal(df,col):

    """
    Función que proporciona un gráfico de barras horizontal.
    Agrupa las filas en función de la columna que se indique y los pedidos completados. 

    Parameters:
    df (pd.DataFrame): DataFrame a analizar.
    col: columna para graficar.

    Returns:
    None
    """
        
    # Contar pedidos por col
    df_plot = (
        df
        .groupby(col)
        .size()
        .reset_index(name='Cantidad')
        .sort_values(by='Cantidad', ascending=False)  # Orden descendente
    )

    # Gráfico horizontal
    fig, ax = plt.subplots(figsize=(10,8))
    sns.barplot(
        data=df_plot,
        y=col,       
        x='Cantidad',      
        ax=ax,
        palette='Blues_r'
    )

    ax.set_title('Número de pedidos completados por producto')
    ax.set(xlabel=None, ylabel=None)

    plt.tight_layout()
    plt.show()

