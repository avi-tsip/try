const { Options } = require('selenium-webdriver/chrome');

var webdriver = require('selenium-webdriver'),
    By = webdriver.By,
    until = webdriver.until;

require('geckodriver');

var driver = new webdriver.Builder().forBrowser('firefox').build();

driver.get('https://library-app.firebaseapp.com/');

//finding elemnt by css path
// driver.findElement(By.css("html body.ember-application main.container.mt-4 section.jumbotron.text-center div.form-row.justify-content-center div.col-md-6 input.ember-text-field.ember-view.form-control"));
//finding element by css tag
driver.findElement(By.css("input")).sendKeys('user@email.com');
//finding elemetn by css class
var submitBtn = driver.findElement(By.css(".btn-lg"))
driver.wait(function(){
    return submitBtn.isEnabled();
}, 3000);
submitBtn.click()

//another custom explicit wait
var submitBtn = driver.findElement(By.css(".btn-lg"))
driver.wait(function(){
    return submitBtn.getCssValue('opacity').then(function(result){
        return result == 1;
    });
}, 3000);
submitBtn.click()
//implicit wait
driver.manage().timeouts().implicitlyWait(5000);
//explicit wait
driver.wait(until.elementLocated(By.css('.alert-success')), 5000).getText().then(function(txt){console.log('succeeded reading text after email entry: ' + txt)});

//finding element by css class
driver.findElement(By.css(".alert-success"));
//finding many elements
driver.findElements(By.css("nav li")).then(function(elements){elements.map(function(el){el.getText().then(function(txt){console.log("the button name is: " + txt);});});});
//using getText 
driver.findElement(By.css(".btn-lg")).getText().then(function(txt){console.log(txt);});

driver.sleep(5000);
//driver.quit();
