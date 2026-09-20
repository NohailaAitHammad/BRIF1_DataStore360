def anonymize_row(row, salt_key):
      import hashlib
      import hmac

      # Concaténation de la valeur et du sel
      data = f"{row}{salt_key}".encode('utf-8')
      # Calcul du HMAC-SHA256
      hashed = hmac.new(salt_key.encode('utf-8'), data, hashlib.sha256).hexdigest()
      return hashed

def transform_data(df_clean):
      import numpy as np 
      from transform import anonymize_row

      #Creation de colonne Delai Livraison
      df_clean['Délai Livraison'] = np.nan
      df_clean['Délai Livraison'] = (df_clean['Ship Date'] - df_clean['Order Date']).dt.days

      # Après inversion, le délai serait -Délai_actuel

      mask_swap_condition = df_clean['Délai Livraison'] < 0

      delai_apres_swap = -df_clean.loc[mask_swap_condition, 'Délai Livraison']

      mask_swap__condition_valide = mask_swap_condition & (df_clean['Délai Livraison'].abs() <= 30)

      dominant_ship_mode = (
      df_clean.dropna(subset=['Ship Mode'])
      .groupby('Délai Livraison')['Ship Mode']
      .agg(lambda x: x.mode()[0])
      )

      #Inversion des dates

      df_clean.loc[mask_swap__condition_valide, ['Order Date', 'Ship Date']] = (
      df_clean.loc[mask_swap__condition_valide, ['Ship Date', 'Order Date']].values)

      #Supprimer les lignes irrécupérables (|délai| > 30 jours)

      df_clean = df_clean[df_clean['Délai Livraison'].abs() <= 30].copy()

      # Recalcule du Delai de Livraison

      df_clean['Délai Livraison'] = (df_clean['Ship Date'] - df_clean['Order Date']).dt.days

      # Mapping des valeurs manquantes de Ship Mode avec les Ship Mode dominants pour chaque delai de livraison

      mask_condition_ship_mode = df_clean["Ship Mode"].isna() & df_clean['Délai Livraison'].notna() & df_clean['Délai Livraison'] >= 0

      df_clean.loc[mask_condition_ship_mode, 'Ship Mode'] = df_clean.loc[mask_condition_ship_mode, 'Délai Livraison'].map(dominant_ship_mode)

      # Prix Unitaire d'apres le prix total
      
      mask_valide_condition = (
      df_clean['Sales'].notna()
      & df_clean['Quantity'].notna() & (df_clean['Quantity'] > 0)
      & df_clean['Discount'].notna() & (df_clean['Discount'] < 1))

      df_clean['Prix Unitaire'] = np.nan

      df_clean.loc[mask_valide_condition, 'Prix Unitaire'] = (
            df_clean.loc[mask_valide_condition, 'Sales']
            / (df_clean.loc[mask_valide_condition, 'Quantity'] * (1 - df_clean.loc[mask_valide_condition, 'Discount'])))

      prix_ref = (
            df_clean.dropna(subset=['Prix Unitaire'])       
            .groupby('Product Name')['Prix Unitaire']      
            .agg(lambda x: x.mode()[0]))

      mask_imput = (
            df_clean['Sales'].isna()
            & df_clean['Quantity'].notna()
            & df_clean['Discount'].notna()
            & df_clean['Product Name'].notna())

      # Récupérer le prix de référence par produit
      prix_produit = df_clean.loc[mask_imput, 'Product Name'].map(prix_ref)

      # Recalculer Sales

      df_clean.loc[mask_imput, 'Sales'] = (
            df_clean.loc[mask_imput, 'Quantity']
            * prix_produit
            * (1 - df_clean.loc[mask_imput, 'Discount']))

      # Suppression du sales manquantes restantes

      df_clean =  df_clean[df_clean['Sales'].notna()]

      # Vérifier la cohérence : recalculer Prix Unitaire 

      df_clean['Prix Unitaire'] = (
            df_clean['Sales']
            / (df_clean['Quantity'] * (1 - df_clean['Discount']))
            )

      # Creation de la colonne Marge de Profit
      
      mask = df_clean['Sales'] > 0

      df_clean.loc[mask, 'Marge'] = (
      df_clean.loc[mask, 'Profit'] / df_clean.loc[mask, 'Sales'])

      # Anonymisation du Customer Name
      df_clean['Customer Name'] = df_clean['Customer Name'].apply(lambda x: anonymize_row(x, 'SECRET_SALT_KEY'))
      return df_clean