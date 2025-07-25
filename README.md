````markdown
# Internship PDF Automation 🔧

A tool to automatically:
1. Download all internship descriptions (PDFs) from [CSE HCMUT Internship Portal](https://internship.cse.hcmut.edu.vn).
2. Apply OCR to extract tech stacks (programming languages, frameworks).
3. Export results to a CSV file for filtering (e.g. by Python, Web, AI...).

---

## 📦 Requirements
Install with:
```bash
pip install -r requirements.txt
````

Also install:

* [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
* `poppler` (for `pdf2image`, install via `choco install poppler` on Windows)

---

## 🚀 How to use

1. Run:

```bash
python src/main.py
```
---

## 📂 Output

* All PDFs are saved in `downloads/`
* A `result_combined.csv` file is generated with:

  * Company name
  * Detected programming languages/frameworks

---

## 🛠 Technologies

* Python
* Playwright
* Tesseract OCR
* pdf2image
* Pandas

````

🎉 Done! Processed 345 / 349 companies
4 công ty nằm trong thẻ a chưa lấy được nữa 😎😎😎😎😎