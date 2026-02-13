# Análisis EDA de pedidos de Amazon


## 📖 Descripción del Proyecto

Este proyecto se basa en un conjunto de casi 60.000 registros simulados por ChatGPT de pedidos de amazon en el período comprendido entre los años 2020 y 2023.

El análisis de estos datos permite conocer las preferencias de los clientes respecto a los productos ofrecidos, las regiones con mayor demanda, su evolución en el tiempo y otros aspectos clave del negocio.

El objetivo del proyecto es detectar los factores que más impactan en las ventas y lograr una visión completa de los pedidos.


## 📂 Descripción de los Datos

Los datos se dividen en dos tablas, una de pedidos, donde está toda la información de cada pedido (un pedido por fila) y la otra de clientes, donde están todos sus detalles.

Dataset 1: amazon_sales.xlsx

Contiene 59.964 filas y 20 columnas. 

Sus columnas son:

-	`Row_ID`: Índice del pedido.
-	`Order_ID`: Número del pedido.
-	`Order_Date`: Fecha del pedido.
-	`Data_Key`: Fecha del pedido en formato key.
-	`Contact_Name`: Nombre del contacto.
-	`Country`: País del cliente que realiza el pedido.
-	`City`: Ciudad del cliente.
-	`Region`: Región del cliente.
-	`Subregion`: Subregión del cliente.
-	`State`: Estado del pedido.
-	`Customer_ID`: Id del cliente.
-	`Industry`: Industria del cliente.
-	`Segment`: Segmento del cliente.
-	`License`: Licencia del pedido.
-	`Sales`: Valor de venta total del pedido.
-	`Quantity`: Cantidad de unidades compradas.
-	`Discount`: Porcentaje de descuento de la compra.
-	`Profit`: Ganancia total del pedido.
-	`Customer`: Nombre del cliente.

Dataset 2: amazon_customer.xlsx

Contiene 99 filas y 5 columnas. 

Sus columnas son:

-	`Customer_id`: Id del cliente.
-	`Customer_age`: Edad del cliente.
-	`Gender`: Género del cliente.
- `Signup_date`: Fecha de registro del cliente.
-	`Prime_member`: Si es miembro o no de Amazon Prime.


## 🗂️ Estructura del Proyecto

├── data/ # Archivos de datos originales y procesados

├── notebooks/ # Jupyter Notebooks del análisis

├── src/ # Funciones auxiliares

├── dashboard/ # Archivo Power BI para visualizar y analizar datos

└── README.md # Descripción del proyecto


## 📥 Primera lectura de los datos y unión en un archivo común

Para comenzar, se importa el archivo amazon_sales.csv, se presentan unas filas de ejemplo y se comprueba su dimensión, lo mismo con amazon_customers.xlsx. 

Se unen ambos dataframe a través de la columna en común (‘customer_id’). La unión se realiza mediante el método ‘inner join’ por lo cual no serán incluidos en el análisis los clientes que no hayan realizado pedidos.

Luego, se borran la columna índice (‘Row_ID’), ya que no será utilizada, y la columna (‘customer_id’) sobrante.


## 🔍 EDA preliminar

Aquí, se ejecuta una función que nos permite hacer un análisis exploratorio preliminar del dataframe. Este análisis incluye:

-	Muestra aleatoria de 5 filas del DataFrame.
-	Información general del DataFrame (tipo de datos, nulos, etc.).
-	Porcentaje de valores nulos por columna.
-	Conteo de filas duplicadas.
-	Distribución de valores para columnas categóricas.
-	
A partir de este informe, se define la estrategia que se necesita para realizar la limpieza y transformación de los datos.


## 🧹 Limpieza de los Datos

-	Cambio de nombres de columnas y valores a minúsculas.
-	Conversión de las columnas ‘order_date’ y ‘signup_date’ a formato datetime.
-	Creación de las columnas de ‘order_month’ y ‘order_year’ para luego analizar los pedidos por mes y año.


## 🚫 Tratamiento de nulos

### Nulos categóricos

La columna ‘state’ presenta un 6,44% de valores nulos. Dado que este porcentaje no es elevado y existe una categoría dominante que cubre el 70,26% del total, se reemplazan los valores nulos por la moda de esta columna, ‘Received by the customer’.

### Outliers numéricos

Se utiliza el método IQR para identificarlos y “anularlos” si es necesario.

Hay 4 columnas con valores outliers: ‘sales’, ‘profit’, ‘quantity’ y ‘discount’.

Se comprueba que los outliers de sales y de profit ocurren en las mismas filas. Parece ser un caso particular de 6 pedidos con ventas y ganancias excesivamente altas.

Estos valores tan altos aparecen solo en estos pedidos específicos del 14/10/2022 realizados por el mismo cliente, se eliminan ya que forman parte de una excepción.

Mientras que los outliers de ‘quantity’ y ‘discount’ se conservan ya que son muchos más (336 y 228, respectivamente) y eliminarlos impediría evaluar la opción de eventos como días de rebajas o compras al por mayor.

### Nulos numéricos

En cuanto a la columna ‘customer_age’, los valores nulos representan un 10,57% del total. Debido a que este porcentaje no es significativo, se completan los valores nulos con la mediana de edad, para evitar distorsionar el análisis con valores extremos.

Las columnas ‘sales’ y ‘profit’ cuentan con 1,95% de valores nulos. Observando varios ejemplos de pedidos, se comprueba que sus nulos se encuentran en las mismas filas. Al no tener el valor de la compra tampoco se obtiene el de la ganancia. Como el porcentaje es tan bajo, se eliminan esas filas del análisis.


## 📊 Análisis Exploratorio de Datos (EDA)

En esta sección se analizan las principales variables de la tabla de pedidos de Amazon, con el objetivo de identificar los factores que influyen en el comportamiento de compra de los clientes. El análisis abarca tanto variables relacionadas con los productos, como características del cliente y el contexto de la compra, incluyendo descuentos y membresías.


## 📝 Conclusiones

A partir del análisis exploratorio realizado, se pueden extraer las siguientes conclusiones principales:

### Principales características de los clientes

-	La edad promedio de los clientes es de 43 años. La distribución muestra una concentración entre los 33 y 57 años (rango intercuartílico), esto indica que la base de clientes está compuesta mayoritariamente por adultos en etapa laboral. 
-	La distribución según el género es bastante equilibrada entre Masculino y Femenino, con un porcentaje muy pequeño en la categoría Otro, por lo que no parece haber un sesgo marcado en esta variable.
-	La región EMEA concentra la mayor cantidad de operaciones. A nivel país, Estados Unidos contiene la gran mayoría de pedidos, y ciudades como Londres presentan una alta frecuencia de transacciones. Esto refleja una fuerte concentración de ventas en mercados específicos.
-	El segmento SMB (Small and Medium Business) representa la mayor proporción de operaciones, y la industria con mayor participación es Finance, lo que indica una gran penetración en estos sectores.
-	La mayoría de los clientes son miembros de Amazon Prime. Esta base de usuarios tiende a generar mayores niveles de ventas y de frecuencia de compra, lo que sugiere un alto nivel de fidelización o recurrencia.

### Columna ‘state’

-	Se observa que la gran mayoría de los pedidos se encuentran en estado ‘Recieved by the customer’. Sin embargo, existe una proporción menor de pedidos en estado ‘Cancelled’.
-	La cancelación de los pedidos podría estar relacionado con condiciones comerciales (por ejemplo, descuentos elevados), demoras en la gestión, disponibilidad de producto o características del cliente.
-	Al comparar variables como ‘sales’ y ‘quantity’ entre pedidos completados y cancelados, suele observarse que los pedidos cancelados presentan valores promedio distintos (generalmente menores o con mayor dispersión), lo que podría indicar que las órdenes más pequeñas o aquellas con condiciones comerciales particulares tienen mayor probabilidad de no concretarse.
-	Aunque la mayoría de las operaciones se completan exitosamente, los pedidos cancelados constituyen un indicador clave de eficiencia comercial. Su estudio permite identificar posibles mejoras en la gestión de clientes, en la política de descuentos o en el proceso operativo.


### Columnas numéricas clave

-	La columna ‘sales’ presenta una media de 1.116, pero con una desviación estándar muy elevada (4.638), lo que evidencia una fuerte dispersión y una distribución asimétrica positiva. El primer cuartil se sitúa en valores muy bajos (25,92), lo que indica que la mayoría de las ventas son pequeñas y que un número reducido de transacciones de alto valor eleva considerablemente el promedio.
-	La columna ‘profit’ sigue un patrón similar al de ‘sales’: media relativamente alta, pero con gran variabilidad y valores mínimos muy cercanos a cero. Esto indica que, si bien existen operaciones altamente rentables, muchas transacciones generan márgenes reducidos.
-	En cuanto a la cantidad, la mediana se sitúa en torno a 2 unidades, lo que muestra que la mayoría de las órdenes son de bajo volumen. Esto podría estar asociado a compras específicas o licencias individuales más que a grandes adquisiciones masivas.
-	En la columna ‘discount’ el 25% de las operaciones no tiene descuento y la mediana también se sitúa en 0, lo que indica que una proporción importante de ventas se realiza sin descuentos. Sin embargo, existen casos con descuentos elevados que incrementan la dispersión, estos casos pueden representar eventos especiales de descuentos.
-	El dataset cubre operaciones entre 2020 y 2023 (con algunas fechas de alta de clientes incluso previas. La distribución por año muestra una mayor concentración en 2022 y 2023, lo que podría reflejar crecimiento o mayor actividad comercial en esos períodos.

En conjunto, el análisis sugiere que el negocio presenta una fuerte concentración de ingresos en pocas ventas de alto valor, una base de clientes mayoritariamente adulta y profesional, y una alta presencia en determinados mercados geográficos e industrias como Finance. La variabilidad en ventas y beneficios indica heterogeneidad entre clientes y segmentos, lo que abre la posibilidad de profundizar en análisis por segmento, industria o región para identificar oportunidades de optimización comercial y de rentabilidad.

En relación con la existencia de órdenes canceladas, representan una pérdida potencial de ingresos y un indicador clave de eficiencia operativa. Analizar los patrones de cancelación por segmento, región o nivel de venta puede contribuir a identificar oportunidades de mejora en la gestión comercial y en el proceso de conversión de ventas.


## 💻 Requisitos para ejecución

Para ejecutar los notebooks se necesita:

-	Contar con un editor de código como Visual Studio Code.
-	Instalar Python y las librerías utilizadas en cada Notebook (pandas, numpy, matplotlib, etc).
-	Ejecutar los notebooks siguiendo el orden que tienen los nombres de los archivos.

Para visualizar el dashboard se requiere tener Power BI instalado.


## 🤝 Contribuciones

Las contribuciones son bienvenidas. Puedes sugerir nuevas consultas, correcciones o mejoras estructurales.


## ✍️ Autor

Guido Julián Calvo Sio
