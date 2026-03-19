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