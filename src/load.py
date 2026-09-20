from sqlalchemy import create_engine

def get_engine():
      return create_engine(
        "postgresql+psycopg2://root:root@postgres:5432/datastore360")

def clean_data_core(df):
      from sqlalchemy import text

      engine = get_engine()
      with engine.begin() as connection:
            connection.execute(
                  text("TRUNCATE TABLE core.orders, core.products, core.customers CASCADE")
            )
      print("Tables core vidées")
      return df

def load_data_staging(df_raw):
      engine = get_engine()
      with engine.connect() as connection:
            print("Connexion PostgreSQL réussie !")

      return df_raw.to_sql("superstore_raw", engine, schema='staging', if_exists="append", index=False)


def load_core(df, table_name):

      engine = get_engine()
      
      return df.to_sql(table_name, engine, schema='core', if_exists="append", index=False)

def load_data_core(df_clean):

      # DataFrame de Customers

      customers = df_clean[
      [
            "Customer ID",
            "Customer Name",
            "Segment",
            "Country",
            "City",
            "State",
            "Postal Code",
            "Region"
      ]
      ].copy()

      # Suppression des dupliques

      customers = customers.drop_duplicates(
            subset=["Customer ID"])

      # Renomage des colonnes comme celle de base de données

      customers = customers.rename(columns={
            "Customer ID": "customer_id",
            "Customer Name": "customer_name",
            "Segment": "segment",
            "Country": "country",
            "City": "city",
            "State": "state",
            "Postal Code": "postal_code",
            "Region": "region"
            })
      
      load_core(customers, 'customers')

      # Table Products

      products = df_clean[
            [
            "Product ID",
            "Product Name",
            "Category",
            "Sub-Category"
            ]
      ].copy()

      # Suppression des doublons

      products = products.drop_duplicates(
            subset=['Product ID']
            )

      # Renomage des colonnes comme celle de base de données

      products = products.rename(columns={
            "Product ID":"product_id",
            "Product Name":"product_name",
            "Category":"category",
            "Sub-Category":"sub_category"
            })

      load_core(products, 'products')

      # Table orders

      orders = df_clean[
            [
                  "Row ID",
                  "Order ID",
                  "Customer ID",
                  "Product ID",
                  "Order Date",
                  "Ship Date",
                  "Ship Mode",
                  "Délai Livraison",
                  "Sales",
                  "Quantity",
                  "Profit",
                  "Discount",
                  "Marge"
            ]
            ].copy()
      
      # Suppression des doublons

      orders = orders.drop_duplicates(subset=['Row ID'])

      # Renomage des colonnes comme celle de base de données

      orders = orders.rename(columns={
            "Row ID" : "row_id",
            "Order ID" : "order_id",
            "Customer ID" : "customer_id",
            "Product ID" : "product_id",
            "Order Date" : "order_date",
            "Ship Date" : "ship_date",
            "Ship Mode" : "ship_mode",
            "Délai Livraison" : "delivery_time",
            "Sales" : "sales",
            "Quantity" : "quantity",
            "Profit" : "profit",
            "Discount" : "discount",
            "Marge" : "profit_margin"
            })

      load_core(orders, 'orders')
      
      return True


