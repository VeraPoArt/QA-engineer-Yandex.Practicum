SELECT c.name,
		 SUM(k."productsCount") AS cnt
FROM card_model AS c
INNER JOIN kit_model AS k ON c.id=k."cardId"
GROUP BY  c.name
ORDER BY  c.name;
