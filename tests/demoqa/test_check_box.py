def test_check_form(page):
    page.goto("https://demoqa.com/checkbox")

    for i in range(5):
        closed = page.locator(".rc-tree-switcher.rc-tree-switcher_close")
        if closed.count() > 0:
            closed.first.click()
            page.wait_for_timeout(300)
        else:
            break

    page.get_by_role("checkbox", name="Select Desktop").check()
    page.get_by_role("checkbox", name="Select Documents").check()
    page.get_by_role("checkbox", name="Select Downloads").check()

    result = page.locator("#result").inner_text()
    assert "home" in result

