DROP VIEW IF EXISTS features_student;

CREATE VIEW features_student AS
WITH student AS (
    SELECT
        si.id_student AS student_id,
        si.code_module,
        si.code_presentation,
        si.gender,
        si.region,
        si.age_band,
        si.imd_band,
        si.highest_education,
        si.num_of_prev_attempts,
        si.studied_credits,
        si.final_result
    FROM student_info si
),

registration AS (
    SELECT
        id_student,
        MIN(date_registration) AS date_registration,
        MAX(date_unregistration) AS date_unregistration,
        CASE
            WHEN MAX(date_unregistration) IS NULL THEN 0
            ELSE 1
        END AS withdrew,
        (MAX(date_unregistration) - MIN(date_registration)) AS days_enrolled
    FROM student_registration
    GROUP BY id_student
),

assessments_summary AS (
    SELECT
        id_student,
        COUNT(*) AS num_assessments,
        AVG(score) AS avg_score,
        MAX(score) AS max_score
    FROM student_assessment
    GROUP BY id_student
),

vle_summary AS (
    SELECT
        id_student,
        COUNT(*) AS num_vle_interactions,
        SUM(sum_click) AS total_clicks
    FROM student_vle
    GROUP BY id_student
)

SELECT
    s.*,
    r.date_registration,
    r.date_unregistration,
    r.withdrew,
    a.num_assessments,
    a.avg_score,
    a.max_score,
    v.num_vle_interactions,
    v.total_clicks
FROM student s
LEFT JOIN registration r ON s.student_id = r.id_student
LEFT JOIN assessments_summary a ON s.student_id = a.id_student
LEFT JOIN vle_summary v ON s.student_id = v.id_student;