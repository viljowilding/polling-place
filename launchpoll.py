from playwright.sync_api import sync_playwright
import os, sys
from dotenv import load_dotenv

load_dotenv()
args = sys.argv[1:]
if not args[-1]:
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
    if page.title() == "The Students' Union at UWE | Log In":
        page.get_by_label("Username").fill(os.getenv('MSL_USERNAME'))
        page.get_by_label("Password").fill(os.getenv('MSL_PASSWORD'))
        page.get_by_text("Log in").click()
        page.wait_for_load_state()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("textbox").fill(ID)
    page.get_by_text("Go").click()
    # up to here, it works. need to handle the quitting aspect... maybe wait until back to the logged out page then close the browser?
    print("selecting election...")
    page.wait_for_url("**/SelectPost.aspx",timeout=None)
    print("selecting post...")
    page.wait_for_url("**/SelectElection.aspx",timeout=None)
    print("back to select election!")
    page.goto("")
    page.wait_for_timeout(10000)
    page.close()
    