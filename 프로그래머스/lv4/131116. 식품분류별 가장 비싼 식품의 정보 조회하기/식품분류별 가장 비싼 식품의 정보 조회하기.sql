-- 코드를 입력하세요
# SELECT F.CATEGORY, F.PRICE, F.PRODUCT_NAME FROM FOOD_PRODUCT AS F
# (SELECT CATEGORY, MAX(PRICE) AS MAX_PRICE
#  FROM FOOD_PRODUCT
#  GROUP BY CATEGORY) AS FF
# WHERE F.PRICE = FF.MAX_PRICE AND F.CATEGORY = FF.CATEGORY


SELECT F.CATEGORY, F.PRICE, F.PRODUCT_NAME
FROM FOOD_PRODUCT F,
(SELECT CATEGORY, MAX(PRICE) MAX_PRICE
 FROM FOOD_PRODUCT
 GROUP BY CATEGORY) AS FF
WHERE F.CATEGORY = FF.CATEGORY AND F.PRICE = FF.MAX_PRICE
AND F.CATEGORY IN ('과자', '국', '김치', '식용유')
ORDER BY MAX_PRICE DESC