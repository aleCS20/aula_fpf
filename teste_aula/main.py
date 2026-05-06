from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://automationexercise.com")

    page.get_by_role("link", name="Products").click()
    #page.locator(".product-image-wrapper").first.wait_for()

    produtos = page.locator(".product-image-wrapper")

    dados = []

    for produto in produtos.all():
        nome = produto.locator(".productinfo p").inner_text()
        preco = produto.locator(".productinfo h2").inner_text()

        dados.append({
            "nome": nome,
            "preco": preco
        })

    for produto in dados:
        print(
            f"Produto: {produto['nome']}\nPreço: {produto['preco']}\n"
    )

    browser.close()

