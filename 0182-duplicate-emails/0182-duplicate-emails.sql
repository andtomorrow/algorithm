# report all duplicate emails
# SELECT DISTINCT email FROM Person

SELECT email
FROM Person L LEFT JOIN (SELECT DISTINCT email FROM Person) R USING (email)
GROUP BY email
HAVING count(*) > 1;