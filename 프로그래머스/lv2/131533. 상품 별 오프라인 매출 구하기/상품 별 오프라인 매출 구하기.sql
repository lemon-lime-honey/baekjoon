SELECT
    product_code, 
    sum(sales_amount * price) AS sales
FROM product
INNER JOIN offline_sale USING (product_id)
GROUP BY product_code
ORDER BY
    sales DESC, 
    product_code ASC;