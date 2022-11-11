# Data-Engineering

The field of Data Engineering concerns itself with the mechanics for the flow and access of data. Its goal is to make quality data available for fact-finding and data-driven decision making.

**Data Engineers**:
- Designing, Building, Maintaining data infrastructures and platforms
- Develop and optimize data systems
- Make data available for analysis

**Data Analysts**:
- Analyze data in data systems to report and derive insights

**Data Scientists**:
- Perform deeper analysis on data
- Develop predictive models to solve more complex data problems


The **field of Data Engineering involves**:
- Collecting source data (Extracting, integrating, and organizing data from disparate sources)
    - Data acquisition from multiple sources
    - Data architecture for storing source data
- Processing data (Cleaning, transforming, and preparing data to make it usable)
    - Distributed systems for processing data
    - Pipelines for extracting, transforming, and loading data
    - Solutions for safeguarding quality, privacy, and security of data
    - Performance optimization
    - Adherence to compliance guidelines
- Storing data for reliability and easy availability of data
    - Data stores for storage of processed data
    - Scalable systems
    - Ensuring data privacy, security, compliance, monitoring, backup, and recovery
- Making data available to users securely
    - APIs, services, and programs for retrieving data for end-users
    - User access through interfaces and dashboards
    - Checks and balances to ensure data security

# Languages needed for Data Engineers

- Query languages:
    - SQL for mostly relational databases we use mostly for: 
    - NoSQL or SQL-like query languages for NoSQL databases
        
- Programming languages
    - Python, R, Java
        
- Shell and Scripting languages
    - Unix/Linux Shell and PowerShell
        
- Big Data Processing Tools
    - Hadoop (for Big Data)
    - HIVE
    - Spark Apache
       
# Data

**Data Forms**:
- Structured
    - Data that follows a rigid format and can be organized into rows and columns.
        - SQL Databases
        - Online Transaction Processing
        - Spreadsheets
        - Online forms
        - Sensors GPS and RFID
        - Network and Web server logs
- Semi-structured
    - Mix of data that has consistent characteristics and data that does not conform to a rigid structure (Row, columns).
    - **XML and JSON** Allow users to Define Tags Attributes and to store Semi-Structured data
        - E-mails
        - XML and other markup languages
        - Binary executables
        - TCP/IP packets
        - Zipped files
        - Integration of data
- Unstructured
    - Data that is complex and mostly qualitative information that cannot be structured into rows and columns.
    - Does not have an easily identifiable structure
    - Cannot be organized in a mainstream relational database in the form of rows and columns
    - Does not follow any particular format, sequence, semantics, or rules
       - such as Files and Docs
       - Manual Analysis
       - NoSQL
       - Analysis tools

**Standard File Formats**:
1. Delimited text file formats, or .CSV 
    - Delimiter - A sequence of one or more characters for specifying the boundary between independent entities or values (Comma, Tab, Colon, Vertical Bar, Space).
2. Microsoft Excel Open .XML Spreadsheet, or .XLSX
    - Open file format, accessible to most other applications
    - Can use and save all functions available in excel
    - Is a secure file format as it cannot save malicious code
3. Extensible Markup Language, or XML
    - Extensible Markup Language, or XML, is a markup language with set rules for encoding data.
        - Readable by both humans and machines
        - Self-descriptive language
        - Similar to .HTML in some respects
        - Does not use predefined tags like .HTML does
        - Platform independent
        - Programming language independent
        - Makes it simpler to share data between systems
4. Portable Document Format, or .PDF
5. JavaScript Object Notation, or .JSON
    - JavaScript Object Notation, or JSON, is a text-based open standard designed for transmitting structured data over the web.
        - Language-independent data format
        - Can be read in any programming language
        - Easy to use
        - Compatible with a wide range of browsers
        - Considered as one of the best tools for sharing data


# DataBases

- **Data Repository** is a general term used to refer to data that has been collected, organized, and isolated. Data repositories help to isolate data and make reporting and analytics more efficient and credible while also serving as a data archive.
- **DataBase**: Collection of data for input, storage, search, retrieval, and modification of data.
- **DataBase Management System** Set of programs for creating and maintaining the database, and storing, modifying, and extracting information from the database.
- **Factors governing choice of database include**: Data type; Data structure; Querying mechanisms; Latency requirements; Transaction speeds; Intended use of data

**Types of Data Repositores:**

- Relational DataBase Management System (RDBMS)
    - Languages of RDBMS: SQL Server, MySQL, IBM DB2, Oracle Database, PostgreSQL
    - Data is organized into tables format with rows (Records) and columns (Attributes).
    - Well-defined structure and schema for Structured Data.
    - Optimized for data operations and querying
    - Use SQL as the standard querying language
    - Insert, update, and delete records in a database Create new databases, tables, and views Write stored procedures
    - Cloud relational databases include Amazon Relational Database Service (RDS), Google Cloud SQL, IBM DB2 on Cloud, Oracle Cloud, and SQL Azure. 
    - Minimize data redundancy by allowing relationships to be defined between tables
    - Offer export and import options that provide ease of backup and disaster recovery
    - Are ACID compliant, ensuring accuracy and reliability in database transactions
    - Does not work well with semi-structured and unstructured data
    - Migration between two DBMS's is possible only when the source and destination tables have identical schemas and data types

- No-Relational DataBase Management System Database (NoSQL):
    - Languages of non-RDBMS: Redis, MongoDB, Cassandra, Ne04J, HBase
    - Emerged in response to the volume, diversity, and speed at which data is being generated today
    - Built for speed, flexibility, and scale
    - Data can be stored in a schema-less form widely used for processing big data
    - Do not use a traditional row/column/table database design with fixed schemas
    - Types of NoAQL:
        - Key-value store
            - Data in a key-value database is stored as a collection of key-value pairs.
            - A key represents an attribute of the data and is a unique identifier.
            - Both keys and values can be anything from simple integers or strings to complex JSON documents.
            - Great for storing user session data, user preferences, real-time recommendations, targeted advertising, in-memory data caching.
            - Not a great fit if you want to: Query data on specific data value; Need relationships between data values; Need multiple unique keys
            - i.e. Redis, Memcached, and DynamoDB 
        - Document Based
            - Document databases store each record and its associated data within a single document.
            - They enable flexible indexing, powerful ad hoc queries, and analytics over collections of documents.
            - Preferred for eCommerce platforms, medical records storage, CRM platforms, and analvtics platforms.
            - Not a great fit if you want to: Run complex search queries; Perform multi-operation transactions
            - i.e. MongoDB, DocumentDB, CouchDB, and Cloudant are some of the popular document-based databases
        - Column Based
            - Data is stored in cells grouped as columns of data instead of rows.
            - A logical grouping of columns is referred to as a column family.
            - All cells corresponding to a column are saved as a continuous disk entry, making access and search easier and faster.
            - Great for systems that require heavy write requests, storing time-series data, weather data, and IoT data.
            - Not a great fit if you want to: Run complex queries; Change querying patterns frequently
            - The most popular column databases are Cassandra and HBase.
        - Graph Based
            - Graph-based databases use a graphical model to represent and store data.
            - Useful for visualizing, analyzing, and finding connections between different pieces of data.
            - Graph databases are great for social networks, real-time product recommendations, network diagrams, fraud detection, and access management
            - Not a great fit if you want to: Process high volumes of transactions
            - Neo4J and CosmosDB are some of the more popular graph databases.

- Data Warehouses:
    - i.e. Oracle Exadata, IBM, Db2 Warehouse on Cloud, IBM Netezza Performance, Server, Amazon RedShift    
    - Works as a central repository that merges information coming from disparate sources and consolidates it through the extract, transform, and load process, also known as the ETL process, into one comprehensive database for analytics and business intelligence. 
    - When data gets loaded into the data warehouse, it is already modeled and structured for a specific purpose, meaning it's analysis-ready
    - Has a three-tier architecture: 
        - The bottom tier of the architecture includes the database servers, which could be relational, non-relational, or both, that extract data from different sources. 
        - The middle tier of the architecture consists of the OLAP Server, a category of software that allows users to process and analyze information coming from multiple database servers. 
        - And the topmost tier of the architecture includes the client front-end layer. 
    - Some of the popularly used data warehouses include Teradata Enterprise Data Warehouse platform, Oracle Exadata, IBM Db2 Warehouse on Cloud, IBM Netezza Performance Server, Amazon RedShift, BigQuery by Google Cloudera's Enterprise Data Hub, and Snowflake Cloud Data Warehouse.

- Data Mart
    - A data mart is a sub-section of the data warehouse, built specifically for a particular business function, purpose, or community of users. 
    
- ETL Tools Methodologies:
    - i.e. IBM Infosphere, AWS (Amazon),improvado
    - At a very high-level, the ETL process helps you to extract data from different data sources, transform the data into a clean and usable state, and load the data into the enterprise’s data repository. Related to Data Warehouses are the concepts of Data Marts and Data Lakes, which we will cover later. Data Marts and Data Warehouses have historically been relational, since much of the traditional enterprise data has resided in RDBMSes. 
    
   
    
![db_2](img/db_2.jpg "db_2")

- Data Pipelines
    - i.e. Apache Beam; AirFlow; DataFLow
    - Extract, Transform and Load Process
    - Extract, Load, and Transform Process

![db_0](img/db_0.jpg "db_0")


- Data Lakes
    
    

- APIs
    - Text, XML, HTML, Jason
- Web Services
- Data Streams
    - Popular data streams tools: **(Kafka, Apache Spark, Apache Storm)**.
    - Aggregating streams of data flowing from instruments, IT devices and applications, GPS data from cars, computer programs, websites, and social media posts.
        - Social media feeds for sentiment analysis.
        - Sensor data feeds for monitoring industrial or farming machinery.
        - Web click feeds for monitoring web performance and improving design.
        - Real-time flight events for rebooking and rescheduling.
    - RSS (or Really Simple Syndication) feeds Capturing updated data from online forums and news sites where data is refreshed on an ongoing basis.
- Social Platforms
- Sensor Devices
- Web Scraping
    - Popular web scraping tools: **(BeautifulSoup, Scrapy, Pandas, Selenium)** 
    - Extract relevant data from unstructured sources
    - Also known as Screen scraping, Web harvesting, and Web data extraction
    - Downloads specific data based on defined parameters
    - Can extract text, contact information, images, videos, product items, and more...





**Data Repositories**:
- Transactional Or Online Transaction Processing (OLTP) System
    - Designed to store high volume day-to-day operational data
    - Typically relational, but can also be non-relational

- Analytical or Online Analytical Processing (OLAP) Systems
    - Optimized for conducting complex data analytics
    - Include relational and non-relational databases, data warehouses, data marts, data lakes, and big data stores

## Data Integration

![db_1](img/db_1.jpg "db_1")







# Refernce
- https://www.coursera.org/specializations/data-engineering-foundations
