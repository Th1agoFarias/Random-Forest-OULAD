-- 1 Numerode de estudantes que a na tabela 
/*SELECT  id_student,
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
from student_info; */


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





