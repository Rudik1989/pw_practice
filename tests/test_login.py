from playwright.sync_api import Page, Playwright


def test_login(page: Page):
    page.goto("https://4shared.com")
    page.get_by_role("button", name='Log in').click()
    login = page.locator("#login")
    login.fill("")
    password = page.locator("#password")
    password.fill("")
    page.locator("div.signin-form button.big-button").click()
    page.locator('#iloginRejectReason').wait_for(state='visible')
    error = page.locator("#iloginRejectReason").inner_text()
    page.screenshot(path="test_results/image.png")
    assert error == 'Invalid e-mail address or password'


def test_related(playwright: Playwright):
    base_url = (
        "https://search.4shared.com/web/rest/v1_2/files/4wizDP4aku/related?"
        "view=web&offset=0&limit=7"
    )
    api_context = playwright.request.new_context(base_url=base_url)
    response = api_context.get(url='')
    assert response.status == 200
