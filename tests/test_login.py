from playwright.sync_api import Page, Playwright


def test_login(page: Page):
    page.goto("https://4shared.com")
    page.get_by_role("button", name='Log in').click()
    login = page.locator("#login")
    login.fill("vr11@i.ua'")
    password = page.locator("#password")
    password.fill("123456")
    page.locator("div.signin-form button.big-button").click()
    page.locator('#iloginRejectReason').wait_for(state='visible')
    error = page.locator("#iloginRejectReason").inner_text()
    assert error == 'Invalid e-mail address or password'

def test_related(playwright: Playwright):
    api_context = playwright.request.new_context(
        base_url="https://search.4shared.com/web/rest/v1_2/files/4wizDP4aku/related?view=web&offset=0&limit=7"
    )
    response = api_context.get(url='')
    assert response.status == 200
