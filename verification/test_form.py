from playwright.sync_api import sync_playwright

def test_app():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8501")
        page.wait_for_selector('div[data-testid="stApp"]', timeout=10000)

        # Check if the submit button is there and disabled
        button = page.locator('button:has-text("EXECUTE")')
        is_disabled = button.get_attribute("disabled") is not None
        print(f"Button is disabled: {is_disabled}")

        # Also let's check if there's any error message on the page
        errors = page.locator('.stException').all_text_contents()
        if errors:
            print("Errors found on page:")
            for e in errors:
                print(e)

        browser.close()

if __name__ == "__main__":
    test_app()
