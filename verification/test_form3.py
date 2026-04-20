from playwright.sync_api import sync_playwright

def test_app():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8501")
        # Increase timeout heavily just in case
        page.wait_for_selector('div[data-testid="stApp"]', timeout=30000)
        # Wait extra time for the app to actually load content
        page.wait_for_timeout(5000)

        errors = page.locator('.stException').all_text_contents()
        if errors:
            print("Errors found on page:")
            for e in errors:
                print(e)
        else:
            print("No exception on page.")
            page.screenshot(path="./verification/screenshots/verification4.png")

        browser.close()

if __name__ == "__main__":
    test_app()
