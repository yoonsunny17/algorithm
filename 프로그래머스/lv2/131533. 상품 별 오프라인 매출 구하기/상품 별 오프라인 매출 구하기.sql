-- 코드를 입력하세요
SELECT P.PRODUCT_CODE, SUM(P.PRICE * S.SALES_AMOUNT) SALES FROM PRODUCT P
JOIN OFFLINE_SALE S ON P.PRODUCT_ID = S.PRODUCT_ID
GROUP BY P.PRODUCT_ID
ORDER BY SALES DESC, P.PRODUCT_CODE ASC