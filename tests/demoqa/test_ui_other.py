def test_box_form(page):
    page.goto("https://demoqa.com/text-box")

    page.get_by_placeholder("Full Name").fill("Анна Иванова")
    page.get_by_placeholder("name@example.com").fill("anna@test.com")
    page.get_by_placeholder("Current Address").fill("Москва, ул. Ленина, 1")
    page.locator("#permanentAddress").fill("Москва, ул. Ленина, 1")
    page.get_by_role("button", name="Submit").click()