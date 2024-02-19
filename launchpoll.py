from playwright.sync_api import sync_playwright
import os, sys
from dotenv import load_dotenv

load_dotenv()
args = sys.argv[1:]
if len(args)==0:
    ID="15999999" # test ID
else:
    ID=args[-1]
with sync_playwright() as p:
    try:
        browser = p.chromium.connect_over_cdp("http://localhost:9222")
        print("connected")
        page = browser.contexts[0].pages[0]
        print("got page")
    except Exception:
         print("oops exception")
         browser = p.chromium.launch(channel="msedge",headless=False,args=["--kiosk"])
         page = browser.new_context().new_page()
    page.goto("https://uwe.admin.ukmsl.net/voting/")
    page.get_by_label("Username").fill(os.getenv('MSL_USERNAME'))
    page.get_by_label("Password").fill(os.getenv('MSL_PASSWORD'))
    page.get_by_text("Log in").click()
    page.wait_for_load_state()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("textbox").fill(ID)
    page.get_by_text("Go").click()
    print("selecting election...")
    if not os.getenv('DEBUG'):
        # viljo remember to change this
        page.locator("input#ContentPlaceHolder_rptElections_btnSelect_2").click()
    else:
        page.wait_for_url("**/SelectPost.aspx",timeout=None)
    print("selecting post...")
    page.wait_for_url("**/SelectElection.aspx",timeout=None)
    print("back to select election!")
    page.goto("https://viljowilding.github.io/polling-place/thank-you")
    page.wait_for_timeout(10000)
    page.close()
    