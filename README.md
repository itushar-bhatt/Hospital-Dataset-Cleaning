# Hospital-Dataset-Cleaning
Cleaned a real-world hospital dataset using Python and pandas by removing duplicates, fixing data types, handling missing values, and exporting a clean, analysis-ready file. Ideal for beginners learning data cleaning workflows.

# 🏥 Hospital Data Cleaning Project

This project demonstrates the process of cleaning a real-world hospital dataset using Python and pandas. It involves transforming raw, messy data into a structured and usable format.

---

## 📁 Dataset

- `hospital_raw.xlsx`: The original dataset with inconsistencies and noise.
- `hospital_cleaned.csv`: Final cleaned version after applying all cleaning steps.

---

## 🧹 Data Cleaning Performed

The following operations were carried out using pandas:

- Removed unwanted columns
- Handled missing values using `fillna()`
- Converted column data types using `astype()`
- Removed duplicate rows with `drop_duplicates()`
- Stripped unwanted spaces using `strip()` and `replace()`
- Applied custom logic using `apply()` for column transformations
- Exported the cleaned dataset to `.csv`

---

## 📂 Project Structure

```
hospital-data-cleaning/
│
├── data/
│   ├── hospital_raw.xlsx
│   └── hospital_cleaned.csv
│
├── scripts/
│   └── clean_data.py
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Tools & Technologies

- Python
- pandas
- openpyxl
- Jupyter Notebook (for exploratory steps)

---

## ▶️ How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Cleaning Script:
```bash
python scripts/clean_data.py
```

---

## 📊 Future Scope

- Build a dashboard using Power BI
- Perform statistical analysis on patient/hospital data
- Create interactive visual reports

---

## 👤 Author

**Tushar Bhatt**  
*Data Analytics Enthusiast*  
LinkedIn: [www.linkedin.com/in/itusharbhatt](https://www.linkedin.com/in/itusharbhatt)

---

## ⭐️ Show Your Support

If you like this project, give it a ⭐️ on GitHub!