-- 코드를 작성해주세요
SELECT C.ID, C.GENOTYPE, C.PARENT_GENOTYPE
FROM (
    SELECT A.ID, A.PARENT_ID, A.GENOTYPE, B.GENOTYPE AS PARENT_GENOTYPE
    FROM ECOLI_DATA A
    LEFT JOIN ECOLI_DATA B
    ON A.PARENT_ID = B.ID
) AS C
WHERE C.GENOTYPE & C.PARENT_GENOTYPE = C.PARENT_GENOTYPE
ORDER BY C.ID