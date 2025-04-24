WITH student AS (
    SELECT
        si.id_student AS student_id,
        si.code_module,
        si.code_presentation,
        si.gender,
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
        (MAX(date_unregistration) - MIN(date_registration)) AS days_enrolled
    FROM student_registration
    GROUP BY id_student
),

assessments_summary AS (
    SELECT
        sa.id_student,
        COUNT(*) AS assessments,
        AVG(score) AS score,
        COUNT(CASE WHEN sa.date_submitted - sr.date_registration <= 14 AND sa.date_submitted - sr.date_registration >= 0 THEN 1 END) AS early_assessments
    FROM student_assessment sa
    JOIN student_registration sr ON sr.id_student = sa.id_student
    GROUP BY sa.id_student
),

vle_summary AS (
    SELECT
        sv.id_student,
        COUNT(*) AS interactions,
        SUM(sum_click) AS clicks,
        SUM(CASE WHEN sv.date - sr.date_registration <= 14 AND sv.date - sr.date_registration >= 0 THEN sv.sum_click ELSE 0 END) AS early_clicks
    FROM student_vle sv
    JOIN student_registration sr ON sr.id_student = sv.id_student
    GROUP BY sv.id_student
)

SELECT
    s.code_module,
    s.code_presentation,
    s.gender,
    s.age_band,
    s.imd_band,
    s.highest_education,
    s.num_of_prev_attempts,
    s.studied_credits,
    s.final_result,
    r.days_enrolled,
    a.assessments,
    a.score,
    a.early_assessments,
    v.interactions,
    v.clicks,
    v.early_clicks
FROM student s
LEFT JOIN registration r ON s.student_id = r.id_student
LEFT JOIN assessments_summary a ON s.student_id = a.id_student
LEFT JOIN vle_summary v ON s.student_id = v.id_student;
