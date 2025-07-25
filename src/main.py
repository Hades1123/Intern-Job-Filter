from playwright.sync_api import sync_playwright
import time
from pathlib import Path
from pdf2image import convert_from_path
import pytesseract
import pandas as pd
from unidecode import unidecode
from docx import Document

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
base_dir = Path(__file__).resolve().parent.parent
downloads_dir = base_dir / "downloads"
downloads_dir.mkdir(exist_ok=True)

company_do_not_have_pdf_docx = []
company_quantity = 0

keywords = [    
    # frontend
    "javascript",
    "typescript",
    "html",
    "css",
    "react",
    "vue",
    "angular",
    "svelte",
    "nextjs",
    "nuxt",
    "tailwindcss",
    "bootstrap",

    # backend
    "nodejs",
    "express",
    "nestjs",
    "python",
    "django",
    "flask",
    "fastapi",
    "java",
    "springboot",
    "csharp",
    "dotnet",
    "golang",
    "fiber",
    "php",
    "laravel",
    "ruby",
    "rails",
    "graphql",
    "restapi",
    "mysql",
    "postgresql",
    "mongodb",
    "prisma",
    "typeorm",
    "sequelize",
    "mongoose",
    "docker",
    ".net",
    "asp.net",
    "C#",
    "spring",

    # mobile
    "flutter",
    "dart",
    "reactnative",
    'react native',
    "kotlin",
    "swift",
    "android studio",
    "xcode",
    "capacitor",
    "ionic",
    "expo"

    # ai
    "pytorch",
    "tensorflow",
    "transformers",
    "scikitlearn",
    "keras",
    "openai",
    "langchain",
    "llama",
    "onnx",
    "huggingface",

    # data
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "scipy",
    "sql",
    "spark",
    "hadoop",
    "airflow",
    "superset",

    # devops
    "kubernetes",
    "jenkins",
    "gitlabci",
    "githubactions",
    "terraform",
    "ansible",
    "prometheus",
    "grafana",
    "nginx",
    "aws",
    "gcp",
    "azure"
]

results = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://internship.cse.hcmut.edu.vn/")
    page.wait_for_timeout(3000)
    
    logos = page.query_selector_all("div.logo-box:not(a div.logo-box)")
    print(f"🧩 Found {len(logos)} companies.")
    
    for i, logo in enumerate(logos):
        company_data = {}
        try:
            print(f"\n🔍 Clicking company #{i + 1}")
            logo.click()
            time.sleep(3)
            
            title_element = page.query_selector("div.about-course h4")
            title_text = title_element.inner_text().strip() if title_element else 'unknown'
            company_data["Tên công ty"] = title_text
            
            h6_texts = [
                "Số lượng đăng ký tối đa",
                "Số sinh viên chấp nhận tối đa",
                "Số lượng sinh viên đã đăng ký",
                "Số lượng sinh viên đã được chấp nhận"
            ]

            h6_elements = page.query_selector_all("div.about-course h6")
            for h6 in h6_elements:
                text = h6.inner_text().strip().split(':')
                if len(text) < 2: 
                    continue
                key, value = text[0], text[1]
                if key in h6_texts:
                    company_data[key] = value
            
            # Tìm và tải các PDF
            links = page.query_selector_all("div.about-course a")
            pdf_found = False
            all_found_keywords = set()

            for index, link in enumerate(links):
                text = link.inner_text()
                if text.lower().endswith(".pdf"):
                    pdf_found = True
                    new_filename = f"{unidecode(title_text)}_{index}.pdf"
                    print(f"⬇️  Found PDF: {text}")
                    with page.expect_download() as download_info:
                        link.click(force=True)
                    download = download_info.value
                    pdf_path = downloads_dir / new_filename
                    download.save_as(pdf_path)
                    print(f"✅ Saved to: {pdf_path}")

                    # OCR file
                    print(f"🔍 OCR {pdf_path.name}")
                    PATH = downloads_dir / pdf_path.name 
                    try:
                        images = convert_from_path(PATH, dpi=200)
                        text = ""
                        for image in images:
                            text += pytesseract.image_to_string(image)
                        
                        for kw in keywords:
                            if kw.lower() in text.lower():
                                all_found_keywords.add(kw)
                        
                        print(f"🔎 Found keywords in {pdf_path.name}: {list(all_found_keywords)}")

                    except Exception as e:
                        print(f"❌ OCR Error: {e}")
                        company_data["Ngôn ngữ / Framework"] = "OCR error"
            
            if pdf_found:
                company_data["Ngôn ngữ / Framework"] = ", ".join(all_found_keywords)
                print(f"🧠 All keywords found: {list(all_found_keywords)}")
                results.append(company_data)
                company_quantity += 1
            else:
                print(f"⚠️ No PDF found for {title_text}, checking for DOCX...")
                docx_found = False
                for index, link in enumerate(links):
                    text = link.inner_text()
                    if text.lower().endswith(".docx"):
                        docx_found = True
                        new_filename = f"{unidecode(title_text)}_{index}.docx"
                        print(f"⬇️  Found DOCX: {text}")
                        with page.expect_download() as download_info:
                            link.click(force=True)
                        download = download_info.value
                        docx_path = downloads_dir / new_filename
                        download.save_as(docx_path)
                        print(f"✅ Saved to: {docx_path}")

                        # Đọc nội dung file DOCX
                        print(f"🔍 Reading DOCX {docx_path.name}")
                        try:
                            doc = Document(docx_path)
                            docx_text = ""
                            for paragraph in doc.paragraphs:
                                docx_text += paragraph.text + "\n"

                            # Thêm keywords vào tập hợp chung
                            for kw in keywords:
                                if kw.lower() in docx_text.lower():
                                    all_found_keywords.add(kw)

                            print(f"🔎 Found keywords in {docx_path.name}: {list(all_found_keywords)}")

                        except Exception as e:
                            print(f"❌ DOCX Error: {e}")
                
                if docx_found:
                    company_data["Ngôn ngữ / Framework"] = ", ".join(all_found_keywords)
                    print(f"🧠 All keywords found: {list(all_found_keywords)}")
                    results.append(company_data)
                    company_quantity += 1
                else:
                    print(f"⚠️ No PDF or DOCX found for {title_text}")
                    company_do_not_have_pdf_docx.append(title_text)

            page.keyboard.press("Escape")
            time.sleep(1)
        
        except Exception as e:
            print(f"⚠️ Error with company #{i + 1}: {e}")
            continue

    df = pd.DataFrame(results)
    csv_path = base_dir / "result.csv"
    df.to_csv(csv_path, index=False)
    print(f"📄 Đã lưu kết quả vào {csv_path}")

    print(f"\n🎉 Done! Processed {company_quantity} / {len(logos) + 4 + len(company_do_not_have_pdf_docx)} companies")
    print(f"⚠️ Company do not have docx or pdf file", company_do_not_have_pdf_docx)