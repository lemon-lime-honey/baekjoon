SELECT ANIMAL_ID, O.ANIMAL_TYPE, O.NAME
FROM ANIMAL_INS AS I
INNER JOIN ANIMAL_OUTS AS O USING (ANIMAL_ID)
WHERE 
    I.SEX_UPON_INTAKE LIKE 'INTACT%'
    AND O.SEX_UPON_OUTCOME REGEXP 'SPAYED|NEUTERED'