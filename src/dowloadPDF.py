from playwright.sync_api import sync_playwright
import os
import time
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
downloads_dir = base_dir / "downloads"
downloads_dir.mkdir(exist_ok=True)
company_quantity = 0
flag = 0
company_with_not_have_pdf = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://internship.cse.hcmut.edu.vn/")
    page.wait_for_timeout(3000) # dong nay bi thua ma thoi ke
    page.wait_for_timeout(3000)

    # get company element
    logos = page.query_selector_all("div.logo-box:not(a div.logo-box)")
    print(f"🧩 Found {len(logos)} companies.")
    
    for i, logo in enumerate(logos):
        try:
            print(f"\n🔍 Clicking company #{i + 1}")
            logo.click()
            time.sleep(5)  # wait for modal loading

            # get all links in company modal
            links = page.query_selector_all("div.about-course a")

            # get company's name
            title_element = page.query_selector("div.about-course h4")
            title_text = title_element.inner_text().strip() if title_element else 'unknown'

            for index, link in enumerate(links):
                text = link.inner_text()
                if text.lower().endswith(".pdf"):
                    flag = 1
                    new_filename = f"{title_text}_{index}.pdf"
                    print(f"⬇️  Found PDF: {text}")
                    with page.expect_download() as download_info:
                        link.click(force=True)
                    download = download_info.value
                    save_path = os.path.join(downloads_dir, new_filename)
                    download.save_as(save_path)
                    print(f"✅ Saved to: {save_path}")

            if flag == 0:
                company_with_not_have_pdf.append(title_text)
            company_quantity += flag
            flag = 0
            
            # close modal
            page.keyboard.press("Escape")
            time.sleep(1)

        except Exception as e:
            print(f"⚠️ Error with company #{i + 1}: {e}")
            continue

    print(f"\n🎉 Done! Complete: {company_quantity / len(logos) * 100} %")
    print(company_with_not_have_pdf)