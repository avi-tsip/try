const { Builder, By, Key } = require("selenium-webdriver");
const fireFox = require("selenium-webdriver/firefox")
const proxy = require("selenium-webdriver/proxy")

const options = new fireFox.Options();

//set options for browser preferences
options.setPreference("browser.download.dir", "C:\\mySelDown")
options.setPreference("browser.download.folderList", 2);
options.setPreference("browser.helperApps.neverAsk.saveToDisk", "text/csv")

//set to use a specific profile
//options.setProfile("C:\\Users\\Aba\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\78rztbzo.default-release");


//set a proxy to use in your browser - make sure to copy it to another location
const proxyServer = "206.189.154.182:8080";

//add proxy settings/profile to creation of driver
const driver = new Builder().forBrowser('firefox').setFirefoxOptions(options).setProxy(proxy.manual({http:proxyServer, https:proxyServer})).build();

driver.get('https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2019-financial-year-provisional/Download-data/annual-enterprise-survey-2019-financial-year-provisional-csv.csv');
// driver.findElement(By.name('q')).sendKeys('selenium', Key.ENTER);