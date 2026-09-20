def generate_statistics():
      from .load import get_engine
      import pandas as pd

      engine = get_engine()

      with engine.connect() as connection:

            customers = pd.read_sql(
            "SELECT COUNT(*) AS total FROM core.customers",
            connection
            )

            products = pd.read_sql(
                  "SELECT COUNT(*) AS total FROM core.products",
                  connection
            )

            orders = pd.read_sql(
                  "SELECT COUNT(*) AS total FROM core.orders",
                  connection
            )

            ventes_by_category = pd.read_sql(
                  "SELECT p.category, SUM(o.sales) as total_ventes FROM core.orders as o JOIN core.products as p ON o.product_id = p.product_id GROUP BY p.category ORDER BY COUNT(o.sales) DESC",
                  connection
            )

            ventes_by_region =  pd.read_sql(
                  "SELECT c.region, SUM(o.sales) as total_ventes FROM core.orders as o JOIN core.customers as c ON o.customer_id = c.customer_id GROUP BY c.region ORDER BY COUNT(o.sales) DESC",
                  connection
            )

            ventes_by_segment =  pd.read_sql(
                  "SELECT c.segment, SUM(o.sales) as total_ventes FROM core.orders as o JOIN core.customers as c ON o.customer_id = c.customer_id GROUP BY c.segment ORDER BY COUNT(o.sales) DESC",
                  connection
            )


            print("/=== Statistiques ===/")
            print("Le nombre de clients  :\n ", customers)
            print("Le nombre de produits :\n ", products)
            print("Le nombre de commandes :\n ", orders)
            print("Repartition des ventes par catégorie:\n ", ventes_by_category)
            print("Repartition des ventes par region:\n ", ventes_by_region)
            print("Repartition des ventes par segment de clientaèle:\n ", ventes_by_segment)
            print("\n/=====================/\n")

            

