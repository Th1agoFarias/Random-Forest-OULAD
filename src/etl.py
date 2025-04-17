from sqlalchemy import create_engine
import pandas as pd

def run_etl(db_path="data/oulad.db"):
    egine = create_engine(f"sqlite:///{db_path}")
    query = """
    CREATE VIEW IF NOT EXISTS course_summary AS
    WITH feature_student AS (
    
    FROM student_info si
    left join student_assement sa
    ON si.id_student = sa.id_student
    group by 
    si.id_student
        )

    SELECT * FROM feature_student
"""