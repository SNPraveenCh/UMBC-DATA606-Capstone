## Airbnb Price Forecasting

**Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang**

Author - **Praveen Chandanala**

**https://github.com/SNPraveenCh/UMBC-DATA606-Capstone**

**[linkedin/praveen-chandanala](https://www.linkedin.com/in/praveen-chandanala-89a1081a1/)**

---

#### **Background**

What is it about?

- This dataset contains information related to Airbnb listings, offering valuable insights into various aspects of short-term rental properties. It includes details such as location, property type, amenities, pricing, and reviews, collected from Airbnb listings across different regions. This dataset presents an opportunity for data scientists and researchers to explore and analyze factors influencing Airbnb rental prices, understand market trends, and identify patterns in guest preferences and property characteristics. By leveraging this dataset, stakeholders in the hospitality industry can gain actionable insights to optimize pricing strategies, enhance guest experiences, and improve the overall efficiency of Airbnb hosting. Moreover, researchers can use this dataset to develop predictive models, recommendation systems, and other data-driven solutions aimed at improving decision-making processes and maximizing value for both hosts and guests in the Airbnb ecosystem.

Why does it matter?

- The dataset matters for several reasons. Firstly, it provides valuable insights into the dynamics of the short-term rental market, particularly through the lens of Airbnb listings. Understanding factors influencing rental prices and property characteristics can benefit various stakeholders, including property owners, travelers, and policymakers. Property owners can use the insights gained from the dataset to optimize pricing strategies, attract more guests, and maximize revenue. Travelers can make more informed decisions when selecting accommodations based on factors such as location, amenities, and pricing trends. Policymakers can leverage this data to develop regulations and policies that promote fair competition, consumer protection, and sustainable growth in the short-term rental industry. Overall, the dataset serves as a valuable resource for analyzing market trends, driving informed decision-making, and fostering innovation in the hospitality sector.

What are your research questions?

- What are the key factors influencing Airbnb rental prices?
- Are there any seasonal trends or patterns in Airbnb rental prices?


---

#### **Data** 

- Data Source – **[Kaggle/airbnb-price-dataset](https://www.kaggle.com/datasets/rupindersinghrana/airbnb-price-dataset)**
- Data Size – **101.5 MB**
- Data Shape – **Rows : 74111 , Columns : 29**
- Time Period – **2008 to 2017**
- What does each row represent? – **A property ( House, Apartment, Townhouse)**
- Data Columns

| No. | Variable               | Type     |
|-----|------------------------|----------|
| 1   | Id                     | int64    |
| 2   | log_price              | float64  |
| 3   | property_type          | object   |
| 4   | room_type              | object   |
| 5   | amenities              | object   |
| 6   | accommodates           | int64    |
| 7   | bathrooms              | float64  |
| 8   | bed_type               | object   |
| 9   | cancellation_policy    | object   |
| 10  | cleaning_fee           | bool     |
| 11  | city                   | object   |
| 12  | description            | object   |
| 13  | first_review           | object   |
| 14  | host_has_profile_pic   | object   |
| 15  | host_identity_verified | object   |
| 16  | host_response_rate     | object   |
| 17  | host_since             | object   |
| 18  | instant_bookable       | object   |
| 19  | last_review            | object   |
| 20  | latitude               | float64  |
| 21  | longitude              | float64  |
| 22  | name                   | object   |
| 23  | neighbourhood          | object   |
| 24  | number_of_reviews      | int64    |
| 25  | review_scores_rating   | float64  |
| 26  | thumbnail_url          | object   |
| 27  | zipcode                | object   |
| 28  | bedrooms               | float64  |
| 29  | beds                   | float64  |

- Which variable/column will be your target/label in your ML model? – **log_price**
- Which variables/columns may be selected as features/predictors for your ML models? - **property_type, room_type, bathrooms, cancellation_policy, cleaning_fee, city, host_has_profile_pic, host_identity_verified, instant_bookable, neighbourhood, zipcode, bedrooms, beds**
