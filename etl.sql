WITH base_info AS (
    SELECT
        s.id_student,
        s.gender,
        s.region,
        s.highest_education,
        s.imd_band,
        s.age_band,
        s.num_of_prev_attempts,
        s.studied_credits,
        s.disability,
        s.final_result
    FROM student_info s
),
assessment_avg AS (
    SELECT
        sa.id_student,
        ROUND(AVG(sa.score), 2) AS avg_score
    FROM student_assessment sa
    GROUP BY sa.id_student
),
student_vle_interactions AS (
    SELECT
        sv.id_student,
        COUNT(*) AS total_clicks,
        SUM(sv.clicks) AS sum_clicks
    FROM student_vle sv
    GROUP BY sv.id_student
),
registration_status AS (
    SELECT
        sr.id_student,
        COUNT(*) AS total_registrations
    FROM student_registration sr
    GROUP BY sr.id_student
),
features_joined AS (
    SELECT
        b.*,
        a.avg_score,
        sv.total_clicks,
        sv.sum_clicks,
        r.total_registrations
    FROM base_info b
    LEFT JOIN assessment_avg a ON b.id_student = a.id_student
    LEFT JOIN student_vle_interactions sv ON b.id_student = sv.id_student
    LEFT JOIN registration_status r ON b.id_student = r.id_student
)

SELECT *
FROM features_joined;
