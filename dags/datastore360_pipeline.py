from datetime import datetime
from airflow.decorators import dag, task
from src.extract import extract_data
from src.load import load_data_staging, load_data_core, clean_data_core
from src.cleaning import clean_data
from src.transform import transform_data
from src.validation import validation

@dag(
      dag_id="Hello_airflow",
      start_date=datetime(2026, 9, 19),
      schedule="@daily",
)
def Hello_airflow():

      @task
      def extract():
            print("/==== Extraction des données ===/")
            return extract_data() 
      
      @task
      def load_staging(df_raw):
            result= load_data_staging(df_raw)
            print("/=== Chargement dans staging ===/")
            print("Résultat :", result)
            return df_raw
      
      @task
      def clean(df):
            print("/=== Netoyage de données ===/")
            return  clean_data(df)

      @task
      def transform(df_clean):
            print("/=== Transformation des donnees ===/")
            return  transform_data(df_clean)  

      @task
      def clean_core(df):
            print("/=== Netoyage des tables dans core ===/")
            return clean_data_core(df)
      
      @task
      def load_core(df_clean):
            print("/=== Chargement dans core ===/")
            load_data_core(df_clean)

      @task
      def validate():
            print("/=== validation des donnees ===/")
            validation()
            print("/=== Fin pipeline ===/")

            
      
      extracted = extract()
      staged = load_staging(extracted)
      cleaned = clean(staged)
      transformed = transform(cleaned)
      cleaned_core = clean_core(transformed)
      core_loaded = load_core(cleaned_core)
      validated = validate()

      extracted >> staged >> cleaned >> transformed >> cleaned_core >> core_loaded >> validated

Hello_airflow()