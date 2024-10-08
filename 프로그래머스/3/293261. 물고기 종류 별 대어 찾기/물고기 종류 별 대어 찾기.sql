-- 코드를 작성해주세요
SELECT *
FROM FISH_INFO A
JOIN FISH_NAME_INFO B
ON A.FISH_TYPE = B.FISH_TYPE

# SELECT *
# FROM FISH_INFO A
# JOIN FISH_NAME_INFO B
# USING (FISH_TYPE)
# WHERE (FISH_TYPE, LENGTH) IN (
#     SELECT FISH_TYPE, MAX(LENGTH) AS LENGTH
#     FROM FISH_INFO
#     GROUP BY FISH_TYPE
# )

# SELECT ID, FISHNAME, LENGTH
# FROM FISHINFO JOIN FISHNAMEINFO USING(FISHTYPE)
# WHERE (FISHTYPE, LENGTH) IN (
# SELECT FISHTYPE, MAX(LENGTH) AS LENGTH
# FROM FISHINFO
# GROUP BY FISH_TYPE
# )
# ORDER BY ID ASC;