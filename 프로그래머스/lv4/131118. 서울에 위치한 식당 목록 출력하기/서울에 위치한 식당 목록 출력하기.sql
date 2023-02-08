-- 코드를 입력하세요
SELECT INFO.REST_ID, INFO.REST_NAME, INFO.FOOD_TYPE, INFO.FAVORITES, INFO.ADDRESS, ROUND(AVG(REVIEW.REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO AS INFO
INNER JOIN REST_REVIEW AS REVIEW ON INFO.REST_ID = REVIEW.REST_ID
WHERE INFO.ADDRESS LIKE '서울%'
GROUP BY INFO.REST_ID
ORDER BY SCORE DESC, FAVORITES DESC