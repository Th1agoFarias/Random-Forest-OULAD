-- 1 Numerode de estudantes que a na tabela 
SELECT  id_student,
     count(*) as studunt_count
from student_info;


-- 2 Quantidade de estudantes que passaram no exame e quantidade de estudantes que foram reprovados no exame
SELECT 
    COUNT(CASE WHEN final_result = 'Withdrawn' THEN 1 END) AS withdrawn_count,
    COUNT(CASE WHEN final_result = 'Pass' THEN 1 END) AS pass_count
FROM 
    student_info;

-- 3 Quantidade de estudantes que passaram no exame e quantidade de estudantes que foram reprovados no exame por gênero

SELECT
    COUNT(CASE WHEN gender = 'M' THEN 1 END) as count_male,
    COUNT(CASE WHEN gender = 'F' THEN 1 END) as count_female

WHERE final_result = 'Pass' or final_result = 'Withdrawn';
from student_info; 


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

SELECT 
    age_band,
    COUNT(CASE WHEN final_result = 'Pass' THEN 1 END) AS total_pass,
    COUNT(CASE WHEN final_result = 'Withdrawn' THEN 1 END) AS total_withdrawn
FROM student_info
GROUP BY age_band
ORDER BY age_band;


-- Explorando estudante studentAssessment --

SELECT id_assessment,
         avg(score) as average_score,
         max(score) as max_score,
         min(score) as min_score      
FROM student_assessment 
GROUP BY id_assessment;


-- Explorando student_registration--

/* verifica o motivo de está com valores negativos */
SELECT 
    id_student,
    date_registration,
    date_unregistration
FROM 
    student_registration;



SELECT
    COUNT(CASE WHEN date_unregistration IS NOT NULL THEN 1 END) AS withdrawn_students,
    COUNT(CASE WHEN date_unregistration IS NOT NULL THEN 1 END) AS still_enrolled
FROM student_registration;

--  Tempo de permanência no curso (para quem se desinscreveu)
SELECT    
    id_student,
    date_registration,
    date_unregistration,
    (date_unregistration - date_registration) AS days_enrolled
FROM 
    student_registration
WHERE 
    date_unregistration IS NOT NULL;

SELECT 
    AVG(date_unregistration - date_registration) AS avg_days_enrolled
FROM student_registration
WHERE   
    date_registration IS NOT NULL;







