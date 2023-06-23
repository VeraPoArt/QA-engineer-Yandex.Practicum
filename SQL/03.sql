SELECT COUNT(id) AS cnt,
		 "categoryId"
FROM product_model
GROUP BY  "categoryId"
HAVING COUNT(id) > 5
ORDER BY  cnt;
