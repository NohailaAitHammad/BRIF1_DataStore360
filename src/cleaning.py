def clean_data(df):
      import numpy as np
      import pandas as pd

      
      #une copie de dataframe pour ne pas modifier de l'origine

      df_clean = df.copy()

      #suppression des doublants

      df_clean.drop_duplicates(inplace=True)

      #Trasformation du types des dates Order Date et Ship Date

      df_clean['Order Date'] = pd.to_datetime(df_clean['Order Date'], errors='coerce', format='%m/%d/%Y')

      df_clean['Ship Date'] = pd.to_datetime(df_clean['Ship Date'], errors='coerce', format='%m/%d/%Y')

      #Transformation de tout les valeurs de type object en str lowercase

      id_cols = ["Row ID", "Order ID", "Customer ID", "Product ID"]

      string_cols = df_clean.select_dtypes(include="object").columns.difference(id_cols)

      for col in string_cols:
            df_clean[col] = df_clean[col].str.strip().str.lower()

      #Modification des fautes d'orthographe pour le segment

      df_clean.loc[df_clean['Segment'] == 'consumerr', 'Segment'] = 'consumer'

      df_clean.loc[df_clean['Segment'] == 'corporrate', 'Segment'] = 'corporate'

      df_clean.loc[df_clean['Segment'] == 'home ofice', 'Segment'] = 'home office'

      #Remplavement de tous les Customer Name manquants par leur valuer d'apres le regroupement de Customer Id, et supprimer le dernier un qui existe

      df_clean['Customer Name'] = df_clean.groupby('Customer ID')['Customer Name'].transform('first')

      #Suppresion d'un Customer anonyme

      df_clean.drop(df_clean[df_clean["Customer Name"].isna()].index, inplace=True)

      #Transformation des valeurs manquantes du ship mode d'apres les ship mode valide du regroupement d'order id

      df_clean['Ship Mode'] = df_clean.groupby('Order ID')['Ship Mode'].transform('first')


      # Rempliçage de Postal Code depuis Order ID

      df_clean['Postal Code'] = (
            df_clean.groupby('Order ID')['Postal Code']
            .transform(lambda s: s.ffill().bfill())
            )

      # Mapping City + State depuis le dataset lui-même

      mapping_postal_code = (
            df_clean.dropna(subset=['Postal Code'])
            .groupby(['City', 'State'])['Postal Code']
            .agg(lambda x: x.mode()[0])
            )
      
      mask_postal_code = (df_clean['Postal Code'].isna()
      & df_clean['City'].notna()
      & df_clean['State'].notna()
      )

      keys = df_clean.loc[mask_postal_code, ['City', 'State']].apply(tuple, axis=1)

      df_clean.loc[mask_postal_code, 'Postal Code'] = keys.map(mapping_postal_code)

      # Suppression des quantites negatives

      df_clean= df_clean[df_clean['Quantity'] >= 0].copy()

      # Suppression des remises supérieure à 100%
      df_clean = df_clean[df_clean['Discount'] <= 1.0].copy()

      # 2 eme Suppression des valuers dupliquer
      df_clean.drop_duplicates(inplace=True)


      return df_clean


















