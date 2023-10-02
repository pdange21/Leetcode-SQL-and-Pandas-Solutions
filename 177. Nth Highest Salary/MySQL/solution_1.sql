 
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE result INT;

    SELECT IFNULL(salary, NULL) INTO result
    FROM (
        SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS r
        FROM Employee
    ) AS ranked
    WHERE r = N
    LIMIT 1;

    RETURN result;
END 
