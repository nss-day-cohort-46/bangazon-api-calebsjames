SELECT order_id, first_name, last_name, (price * quantity) as Total, merchant_name
FROM bangazonapi_order
INNER JOIN bangazonapi_orderproduct 
ON bangazonapi_order.id = bangazonapi_orderproduct.order_id
INNER JOIN bangazonapi_customer 
ON bangazonapi_order.customer_id = bangazonapi_customer.id
INNER JOIN bangazonapi_product
ON bangazonapi_orderproduct.product_id = bangazonapi_product.id
INNER JOIN auth_user
ON bangazonapi_customer.user_id = auth_user.id
INNER JOIN bangazonapi_payment
ON bangazonapi_payment.id = bangazonapi_order.payment_type_id
WHERE payment_type_id IS NOT NULL
GROUP BY order_id
