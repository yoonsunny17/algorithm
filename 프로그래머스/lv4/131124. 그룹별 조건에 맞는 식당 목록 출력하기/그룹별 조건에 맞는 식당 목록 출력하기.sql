-- 코드를 입력하세요
# 1. 두 그룹 join
# 2. 리뷰를 가장 많이 작성한 멤버 아이디를 찾아줘
# 3. 리뷰 테이블에서, 멤버 아이디를 기준으로 그룹화 하고
# 4. 갯수 카운트를 해주고, 내림차순 정렬 후 맨 위에 최댓값만 뽑게 리미트 걸어줘

SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE M
JOIN REST_REVIEW R ON M.MEMBER_ID = R.MEMBER_ID
WHERE M.MEMBER_ID IN (SELECT MEMBER_ID FROM REST_REVIEW
                     GROUP BY MEMBER_ID
                     HAVING COUNT(*) = (SELECT COUNT(*) TEMP
                                       FROM REST_REVIEW
                                       GROUP BY MEMBER_ID
                                       ORDER BY TEMP DESC
                                       LIMIT 1))
ORDER BY REVIEW_DATE, REVIEW_TEXT