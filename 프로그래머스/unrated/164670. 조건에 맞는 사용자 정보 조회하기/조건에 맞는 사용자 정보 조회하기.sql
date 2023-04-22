-- 코드를 입력하세요
# SELECT U.USER_ID, U.NICKNAME, CONCAT(U.CITY, ' ', U.STREET_ADDRESS1, ' ', U.STREET_ADDRESS2) '전체주소', CONCAT(SUBSTR(TLNO, 1, 3), '-', SUBSTR(TLNO, 4, 4), '-', SUBSTR(TLNO, 8, 4)) '전화번호'
# FROM USED_GOODS_BOARD B
# JOIN USED_GOODS_USER U ON B.WRITER_ID = U.USER_ID
# WHERE USER_ID IN (SELECT WRITER_ID
#                  FROM USED_GOODS_BOARD
#                  GROUP BY WRITER_ID
#                  HAVING COUNT(*) >= 3)
# GROUP BY U.USER_ID
# ORDER BY USER_ID DESC



SELECT USER_ID, NICKNAME, CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) '전체주소', CONCAT(SUBSTR(TLNO, 1, 3), '-', SUBSTR(TLNO, 4, 4), '-', SUBSTR(TLNO, 8, 4)) '전화번호'
FROM USED_GOODS_USER
WHERE USER_ID IN (SELECT WRITER_ID
                  FROM USED_GOODS_BOARD
                 GROUP BY WRITER_ID
                 HAVING COUNT(WRITER_ID) >= 3)
ORDER BY USER_ID DESC