-- 1. Número total de estudantes
SELECT 
    COUNT(*) AS studunt_count
FROM student_info;


-- 2. Contagem de estudantes por tipo de resultado final
SELECT 
    COUNT(CASE WHEN final_result = 'Withdrawn' THEN 1 END) AS withdrawn_count,
    COUNT(CASE WHEN final_result = 'Pass' THEN 1 END) AS pass_count,
    COUNT(CASE WHEN final_result = 'Fail' THEN 1 END) AS fail_count
FROM 
    student_info;


-- 3. Contagem por gênero entre os que passaram ou desistiram
SELECT
    COUNT(CASE WHEN gender = 'M' THEN 1 END) AS count_male,
    COUNT(CASE WHEN gender = 'F' THEN 1 END) AS count_female
FROM student_info
WHERE final_result = 'Pass' OR final_result = 'Withdrawn';


-- 4. Agrupamento por imd_band e número de tentativas anteriores
SELECT
    imd_band,
    num_of_prev_attempts,
    COUNT(*) AS total_students
FROM
    student_info
GROUP BY
    imd_band, num_of_prev_attempts
ORDER BY
    imd_band, num_of_prev_attempts;


-- 5. Comparativo de aprovados e desistentes por faixa etária
SELECT 
    age_band,
    COUNT(CASE WHEN final_result = 'Pass' THEN 1 END) AS total_pass,
    COUNT(CASE WHEN final_result = 'Withdrawn' THEN 1 END) AS total_withdrawn
FROM student_info
GROUP BY age_band
ORDER BY age_band;


-- 6. Média, máximo e mínimo de score por id_assessment
SELECT 
    id_assessment,
    AVG(score) AS average_score,
    MAX(score) AS max_score,
    MIN(score) AS min_score      
FROM student_assessment 
GROUP BY id_assessment;


-- 7. Verificar registros inconsistentes de data
SELECT 
    id_student,
    date_registration,
    date_unregistration
FROM student_registration
WHERE date_registration > date_unregistration;


-- 8. Ver todos os registros com datas
SELECT 
    id_student,
    date_registration,
    date_unregistration
FROM 
    student_registration;


-- 9. Quantos desistiram vs quantos ainda estão inscritos
SELECT
    COUNT(CASE WHEN date_unregistration IS NOT NULL THEN 1 END) AS withdrawn_students,
    COUNT(CASE WHEN date_unregistration IS NULL THEN 1 END) AS still_enrolled
FROM student_registration;


-- 10. Tempo (em dias) entre inscrição e desinscrição
SELECT    
    id_student,
    date_registration,
    date_unregistration,
    (date_unregistration - date_registration) AS days_enrolled
FROM 
    student_registration
WHERE 
    date_unregistration IS NOT NULL;


-- 11. Média de tempo de permanência para desistentes
SELECT 
    AVG(date_unregistration - date_registration) AS avg_days_enrolled
FROM student_registration
WHERE   
    date_registration IS NOT NULL AND date_unregistration IS NOT NULL;


-- 12. Total de registros por tipo de atividade (comentado)
/*
SELECT 
    activity_type,
    COUNT(*) AS total_vle_entries
FROM vle
GROUP BY activity_type
ORDER BY total_vle_entries DESC;
*/


-- 13. Interações por tipo de atividade por estudante
SELECT
    sv.id_student,
    v.activity_type,
    COUNT(*) AS total_interactions
FROM student_vle sv
LEFT JOIN vle v
    ON sv.id_site = v.id_site
GROUP BY sv.id_student, v.activity_type
ORDER BY total_interactions DESC;


-- 14. Cliques totais por aluno em cada site
SELECT 
    id_student,
    id_site,
    SUM(sum_click) AS total_clicks
FROM student_vle
GROUP BY id_student, id_site
ORDER BY total_clicks DESC;
