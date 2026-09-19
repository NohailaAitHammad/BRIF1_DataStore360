from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.decorators import dag, task

@dag(
      dag_id="Hello_airflow",
      start_date=datetime(2026, 9, 19),
      schedule="@daily",
)
def Hello_airflow():

      @task
      def extract():
            print("Extract fichier csv")
      
      @task
      def load_staging():
            print("cHARGEMENT DANS STAGING")
      
      @task
      def clean():
            print("netoyage de donnees")
      
      @task
      def transform():
            print("transformation des donnees")
      
      @task
      def load_core():
            print("chargement dans core")

      @task
      def validate():
            print("validation des donnees")
      
      extracted = extract()
      staged = load_staging()
      cleaned = clean()
      transformed = transform()
      core_loaded = load_core()
      validated = validate()

      extracted >> staged >> cleaned >> transformed >> core_loaded >> validated

Hello_airflow()