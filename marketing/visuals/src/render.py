import sys, pathlib
from playwright.sync_api import sync_playwright

src = pathlib.Path(sys.argv[1])
out = src.parent
CHROME = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
SIZES = {"00": (1600, 1300), "01": (1024, 500), "02": (1024, 500), "03": (1024, 500), "04": (1080, 1080)}

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME)
    for html in sorted(src.glob("0*.html"), key=lambda p: p.name != "00-sheet.html" and p.name or "zz"):
        w, h = SIZES[html.name[:2]]
        pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
        pg.goto(html.resolve().as_uri())
        pg.wait_for_load_state("networkidle")
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(400)
        fam = pg.evaluate("getComputedStyle(document.querySelector('h1')).fontFamily")
        ok = pg.evaluate("document.fonts.check('500 40px Roboto')")
        imgs = pg.evaluate("[...document.images].map(i=>i.naturalWidth>0)")
        dest = out / (html.stem + ".png")
        pg.screenshot(path=str(dest), full_page=False)
        print(dest.name, w, h, "font", ok, "imgs", imgs)
        pg.close()
    b.close()
