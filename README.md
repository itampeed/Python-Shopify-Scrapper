# Python-Shopify-Scrapper

**Title:** Shopify Product Variant Data Extraction Tool

**Description:**
This Python script provides a comprehensive solution for extracting, organizing, and analyzing product variant data from Shopify stores' catalogs. Leveraging the robust Requests library for API requests and the versatile Pandas library for data manipulation, this tool streamlines the process of retrieving and structuring product variant information into a structured format for efficient analysis and integration into business workflows.

**Key Features:**
- **Efficient Data Retrieval:** Seamlessly fetches product variant data from Shopify stores' catalogs in JSON format, offering flexibility in configuring parameters such as page limits and pagination for comprehensive coverage and customized data extraction.
- **Dynamic Variant Handling:** Differentiates between variable products and their associated variations, accurately categorizing each variant while preserving essential metadata such as title, price, SKU, availability, and imagery.
- **Flexible Configuration:** Easily customizable for integration with various Shopify stores by replacing the placeholder URL with the desired store's products or catalog URL, followed by '.json', limit, and page parameters.
- **Enhanced Data Organization:** Structures extracted data into a well-defined DataFrame, facilitating effortless analysis, reporting, and manipulation for inventory management, data analysis, and automation purposes.
- **Robust Error Handling:** Incorporates error resilience mechanisms to ensure smooth execution even in the presence of unexpected data structures or connectivity issues, guaranteeing reliable performance under diverse conditions.

**Getting Started:**
1. **Installation:** Install the required dependencies by executing the provided pip commands: `pip install requests` and `pip install pandas`.
2. **Configuration:** Replace the 'url_here' placeholder in the script with the desired Shopify store's products or catalog URL, followed by '.json', limit, and page parameters if products are more than 250. (example is given below).
   Example_Url = 'https://www.shopbogaboga.com/products.json?limit=250&page=1'
3. **Execution:** Run the script to extract product variant data and generate a structured CSV file ('Variants.csv') for further analysis and integration into business workflows.

**Contributing:**
Contributions, bug reports, and feature requests are welcome! Feel free to fork the repository, make enhancements, and submit pull requests to contribute to the project's development.

**License:**
Free for all, happy Coding !!!
