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


**Databases and Data Warehouses**:
- RDBMS:
    - IBM DB2, MySQL,
    - Oracle Database,
    - PostgreSQL
- NoSOL:
    - Redis, MongoDB,
    - Cassandra, Ne04J, HBase (Wide column stores)
- Data Warehouses:
    - Oracle Exadata, IBM
    - Db2 Warehouse on Cloud,
    - IBM Netezza Performance
    - Server, Amazon RedShift

- Data Pipelines
    - Apache Beam
    - AirFlow
    - DataFLow

- ETL Tools Methodologies
    - IBM Infosphere
    - AWS (Amazon)
    - improvado

- Data Lakes

- Languages
    - Query languages
        - SQL for mostly relational databases we use mostly for: 
            - Insert, update, and delete records in a database
            - Create new databases, tables, and views
            - Write stored procedures
        - SQL-like query languages for NoSQL databases
        
    - Programming languages
        - Python, R, Java
        
    - Shell and Scripting languages
        - Unix/Linux Shell and PowerShell
        
    - Big Data Processing Tools
        - Hadoop (for Big Data)
        - HIVE
        - Spark Apache
        
## Pipeline

**Processes**: 
- Extract, Transform and Load Process
- Extract, Load, and Transform Process

![db_0](img/db_0.jpg "db_0")


        
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


**Data  file formats**:
- Relational Database
    - SQL Server, Oracle, MySQL, IBM DB2
- Non-Relational Database
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
