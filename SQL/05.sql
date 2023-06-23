SELECT p.name,
		 p.price,
		 c.name
FROM product_model AS p
INNER JOIN category_model AS c
	ON p."categoryId" = c.id
WHERE p.price BETWEEN 200 AND 500;