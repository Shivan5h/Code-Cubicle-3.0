# Code-Cubicle-3.0
Gen Ai Project for Mastercard and Geek Room's Code the Cubicle 3.0

SMART QUERY AI
Overview
SMART QUERY AI is a versatile Generative AI system that integrates multiple structured data sources (CSV, SQL, NoSQL, and APIs) and generates meaningful insights, patterns, or anomaly detection from these data sources. It allows users to input natural language queries, processes them using advanced NLP techniques, and provides results powered by OpenAI and SerpAPI.

The project is designed to help users analyze and make data-driven decisions across multiple industries such as finance, healthcare, education, logistics, and more.

Workflow

Stage 1: Data Integration
The system integrates multiple file types such as CSV, SQL, NoSQL, and API responses into one cleaned and structured CSV file.
Data from these sources is processed and converted into a unified format using a series of data pipelines.
Stage 2: Data Processing Pipelines
Data Normalization: Normalizes and standardizes the data.
Handling Missing Values: Processes missing values.
Duplicate Removal: Cleanses the dataset by removing any duplicate entries.
Categorical Encoding & Transformation: Encodes categorical variables and applies necessary transformations.
Stage 3: NLP-Based Insights & Query Processing
The system allows users to input a query via natural language.
Vectorization: The cleaned data is vectorized using TfidfVectorizer for better query processing.
Advanced NLP: The query is analyzed using advanced NLP techniques powered by OpenAI and processed with Named Entity Recognition (NER) and Key Performance Indicator (KPI) extraction.
Stage 4: Output Generation
Textual Insights: Generated based on the user's query using OpenAI's GPT models.
Tabular Insights (optional): Key metrics (KPI) and NER-based results are displayed in a tabular format.
Visual Insights (optional): NER information from the query is used to filter and visualize the data interactively using Plotly.
Features
Multiple File Input Support: Integrates CSV files, SQL databases, NoSQL databases, and API responses into a unified dataset.
Advanced Query Handling: Analyzes user queries using advanced NLP techniques with OpenAI API and LangChain.
NER-based Visualization: Generates interactive visualizations using Plotly based on Named Entities extracted from the query.
Optional Tabular Insights: KPI/NER-based tables can be generated as an optional output.
Real-time Problem Resolution: Uses OpenAI and SerpAPI to resolve and generate insights if there are issues with the user query.

File Structure
main.py: Main entry point for the data integration, query processing, and output generation.
integrated.py: Handles data integration from various sources.
query_analysis.py: Processes user queries using OpenAI and advanced NLP techniques, and handles KPI/NER-based output.
vectorization.py: Vectorizes the cleaned CSV data for better query analysis.
visualize.py: Generates interactive visualizations using Plotly based on NER data.
kpi_ner_extraction.py: Extracts Key Performance Indicators (KPI) and Named Entities (NER) from the user’s query for tabular and visual insights.
handling.py: Handles missing data processing.
duplicate.py: Removes duplicate entries from the dataset.
cat.py: Handles categorical encoding and data transformation.
requirements.txt: A file listing all the necessary dependencies.
Future Work
Streamlit Integration: Input handling will be shifted to a Streamlit interface for a more interactive user experience.
Enhanced Visualizations: More complex visualizations could be added based on additional user inputs.

Contact
For any inquiries or suggestions, feel free to reach out to me via GitHub or email at shuklashivansh343@gmail.com.
