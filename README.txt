Data cleaning step:
	- Removed missing values
		Handled missing values in PostalCode by removing rows with null values (only 11 records, negligible impact)
	- Converted date columns to datetime format
	- Standardized categorical values
	- Checked for outliers
		- Identified outliers using IQR method
		- Retained high sales values as they represent real business scenarios
	- Create new columns
		- Extracted year and month from order date
		- Calculated shipping duration (shipping_days)
		- Renamed Sales to total_sales for clarity
		- Created order_count for aggregation

E-commerce Sales Analysis

	Overview
		This project examines our e-commerce sales data to uncover meaningful insights, understand emerging trends, and identify areas where we can drive further growth.

	Key Insights
		1. Revenue trend over time
			Between 2015 and 2018, total revenue increased from 479,856.21 to 722,052.02, demonstrating steady company growth over time
			Business impact: The business is growing well, and it might think about increasing marketing expenditures or scaling operations.
		2. Top performing category
			he Technology category generates the highest revenue, accounting for approximately 36.59% of total sales.
			Business impact: To increase profit, concentrate on promoting and growing high-performing product categories.
		3. Regional performance
			The West region contributes the most total sales, representing around 31.40% of overall revenue.
			Business impact: This area is a robust market and may be given priority for upcoming initiatives or growth.
		4. Customer segments
			The Consumer segment accounts for the majority of total revenue, contributing approximately 50.76%.
			Business impact:Marketing tactics should concentrate on attracting and keeping consumers at the consumer level.
		5. Shipping efficiency
			Standard Class has the longest average delivery time at approximately 5 days.
			Business impact: Increasing shipping speed may improve client retention and satisfaction.
		6. Customer ranking
			With the top 10 customers contributing just 6.8% of total revenue, the business demonstrates a well-diversified customer base. This reduces dependency risk but also suggests an opportunity to develop high-value customer segments through targeted strategies.

	Conclusion
		High-performing product categories, important customer segments, and robust growth trends are all revealed by the analysis. The company can boost overall revenue, enhance customer satisfaction, and optimize operations by utilizing these insights.


