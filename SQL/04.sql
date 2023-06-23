SELECT id,
	CASE
	WHEN "deliveryPrice">500
		AND "status" IN (0,1) THEN 'yes'
ELSE 'no'
END AS "update_order"
FROM "order_model"
