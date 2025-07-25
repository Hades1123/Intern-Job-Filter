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

1. Run the downloader:

```bash
python src/downloadPDF.py
```

2. Then run the OCR analyzer:

```bash
python src/OCR_Reading.py
```

---

## 📂 Output

* All PDFs are saved in `downloads/`
* A `result_ocr.csv` file is generated with:

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

🎉 Done! Processed 331 / 363 companies

Danh sách các công ty bị thiếu do không có file pdf
['CÔNG TY TNHH UGOTECHS', 'CÔNG TY CỔ PHẦN TRUYỀN THÔNG ÁNH SÁNG', 'CÔNG TY AUTONOMOUS VIỆT NAM', 'CÔNG TY TNHH MAYTECH', 'TỔNG CÔNG TY CỔ PHẦN DỊCH VỤ KỸ THUẬT DẦU KHÍ VIỆT NAM', 'TẬP ĐOÀN CÔNG NGHIỆP – VIỄN THÔNG QUÂN ĐỘI', 'CÔNG TY TNHH PHẦN MỀM FPT HỒ CHÍ MINH - TẬP ĐOÀN FPT', 'PHENOMICS LABORATORY', 'CÔNG TY TNHH ALCHERA VIỆT NAM', 'CÔNG TY CỔ PHẦN ACCESSED VIỆT NAM', 'TỔNG CÔNG TY GIẢI PHÁP DOANH NGHIỆP VIETTEL – CHI NHÁNH TẬP ĐOÀN CÔNG NGHIỆP – VIỄN THÔNG QUÂN ĐỘI', 'CÔNG TY TNHH ACACY', 'CÔNG TY TNHH MTV DƯƠNG HOÀNG HOA', 'CÔNG TY CỔ PHẦN HITEK SOLUTION', 'INFINITE SOFTWARE COMPANY LIMITED']
Hiện tại vẫn chưa xử lí công ty chỉ có file .docx
4 công ty nằm trong thẻ a chưa lấy được nữa 😎😎😎😎😎