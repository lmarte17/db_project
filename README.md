## Metropolitain Museum of Art API pull and Database Creation
### Project Overview
This project pulls data from the MET API and stores it in a SQLite database.

### Project Instructions
1. Delete venv folder after extracting the zip file
```rm -rf venv```
2. Create a virtual environment 
```python3 -m venv venv && source venv/bin/activate```
3. Install the required packages
```pip install -r requirements.txt```
4. Run the main.py file
```python main.py```
5. The database should be created and something similar (different entries) should be printed to console:
```
(venv) lmarte  ➜  ~/Documents/Projects/CU-Boulder/SW_Architecture/db_project   % python main.py
Data saved successfully to the database.
Data saved successfully to the database.
Data saved successfully to the database.
Data saved successfully to the database.
Data saved successfully to the database.
(1, 'Wine Glass', 'https://images.metmuseum.org/CRDImages/ad/original/63695.jpg', '1820–40', 'Gift of Mrs. John Bremond and Mrs. John Emory Meek, 1926', 'United States')
(2, 'Wine Glass', 'https://images.metmuseum.org/CRDImages/ad/original/129746.jpg', '1800–1830', 'Rogers Fund, 1913', 'United States')
(3, 'Inkwell', 'https://images.metmuseum.org/CRDImages/ad/original/181937.jpg', 'ca. 1888', 'Gift of Mrs. Emily Winthrop Miles, 1946', 'United States')
(4, 'Salt', 'https://images.metmuseum.org/CRDImages/ad/original/153404.jpg', '1800–1900', 'Gift of Mrs. Charles W. Green, in memory of Dr. Charles W. Green, 1951', '')
(5, 'Plate', '', '1815–30', 'Gift of Mrs. Alan W. Carrick, 1967', 'France')
```