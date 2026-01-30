import sys
import pyspark
import duckdb
import pandas
import pyarrow

print("Python path:", sys.executable)
print("PySpark version:", pyspark.__version__)
print("DuckDB version:", duckdb.__version__)
print("Pandas version:", pandas.__version__)
print("PyArrow version:", pyarrow.__version__)