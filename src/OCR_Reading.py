from pathlib import Path
from pdf2image import convert_from_path
import pytesseract
import pandas as pd
from unidecode import unidecode

# 🔧 Đường dẫn tới tesseract nếu cần
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# "C:\Program Files\Tesseract-OCR\tesseract.exe"

base_dir = Path(__file__).resolve().parent.parent
downloads_dir = base_dir / "downloads"

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
    "go",
    "gin",
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

    # mobile
    "flutter",
    "dart",
    "reactnative",
    "kotlin",
    "swift",
    "androidstudio",
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

for file in downloads_dir.glob("*.pdf"):
    try:
        original_name = file.name
        safe_name = unidecode(original_name)
        safe_path = downloads_dir / safe_name

        # Nếu tên có Unicode → đổi tên file thành bản không dấu
        if file != safe_path:
            file.rename(safe_path)
            print(f"✏️  Renamed: {original_name} → {safe_name}")
        else:
            print(f"✅ Filename OK: {original_name}")

        print(f"🔍 OCR {safe_path.name}")
        images = convert_from_path(safe_path, dpi=200)
        text = ""
        for image in images:
            text += pytesseract.image_to_string(image)

        found = []
        for kw in keywords:
            if kw.lower() in text.lower():
                found.append(kw)

        results.append({
            "Tên công ty (file PDF)": safe_path.stem,
            "Ngôn ngữ / Framework": ", ".join(found)
        })

        print(f"🧠 Found: {found}")

    except Exception as e:
        print(f"❌ Error reading {file.name}: {e}")

df = pd.DataFrame(results)
csv_path = base_dir / "result_ocr.csv"
df.to_csv(csv_path, index=False)

print("📄 Đã lưu kết quả OCR vào result_ocr.csv")

