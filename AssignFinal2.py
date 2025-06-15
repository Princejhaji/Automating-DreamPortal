from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    print("going to Dream Portal...")
    driver.get("https://arjitnigam.github.io/myDreams/")
    time.sleep(3)

    print("clicking My Dreams button...")
    dreams_button = driver.find_element(By.XPATH, "//button[contains(text(), 'My Dreams')]")
    dreams_button.click()
    time.sleep(2)

    windows = driver.window_handles
    for window in windows:
        driver.switch_to.window(window)
        if "dreams-diary.html" in driver.current_url:
            break

    print("now on dreams diary page")
    time.sleep(2)

    dream_rows = driver.find_elements(By.XPATH, "//tbody/tr")
    total_dreams = len(dream_rows)
    print(f"found {total_dreams} dreams")

    good_count = 0
    bad_count = 0

    for row in dream_rows:
        cells = row.find_elements(By.XPATH, ".//td")
        if len(cells) >= 3:
            dream_type = cells[2].text.strip()
            if "Good" in dream_type:
                good_count += 1
            elif "Bad" in dream_type:
                bad_count += 1

    print(f"good dreams: {good_count}")
    print(f"bad dreams: {bad_count}")

    for window in windows:
        driver.switch_to.window(window)
        if "dreams-total.html" in driver.current_url:
            break

    print("now checking summary page...")
    time.sleep(2)

    try:
        good_stat = driver.find_element(By.XPATH, "//*[contains(text(),'Good Dreams')]/following-sibling::*").text
        bad_stat = driver.find_element(By.XPATH, "//*[contains(text(),'Bad Dreams')]/following-sibling::*").text
        total_stat = driver.find_element(By.XPATH, "//*[contains(text(),'Total Dreams')]/following-sibling::*").text
        recurring_stat = driver.find_element(By.XPATH, "//*[contains(text(),'Recurring')]/following-sibling::*").text

        print(f"page shows - Good: {good_stat}, Bad: {bad_stat}, Total: {total_stat}, Recurring: {recurring_stat}")

    except:
        print("couldnt find all statistics on page")

    print("\nresults:")
    if total_dreams == 10:
        print("✓ total dreams count is correct (10)")
    else:
        print(f"✗ expected 10 dreams, got {total_dreams}")

    if good_count == 6:
        print("✓ good dreams count is correct (6)")
    else:
        print(f"✗ expected 6 good dreams, got {good_count}")

    if bad_count == 4:
        print("✓ bad dreams count is correct (4)")
    else:
        print(f"✗ expected 4 bad dreams, got {bad_count}")

except Exception as e:
    print(f"something went wrong: {e}")

finally:
    print("\nclosing browser...")
    driver.quit()
    print("done!")