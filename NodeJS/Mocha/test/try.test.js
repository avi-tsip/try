var webdriver = require('selenium-webdriver'),
    By = webdriver.By,
    until = webdriver.until,
    {describe, it, afterEach, beforeEach } = require('testing');

var driver;

describe('Youtube test', function() {
    
    beforeEach(function(done) {
        this.timeout(5000);
        driver = new webdriver.Builder().
        withCapabilities(webdriver.Capabilities.firefox()).build();
        driver.get('http://www.youtube.com');
        done();
    });

    afterEach(function(done) {
        driver.quit();
        done();
    });
    
    it('webpage should have expected title value', function(done) {
        var promise = driver.getTitle().then(function(title) {
            assert.strictEqual(title, 'YouTube');
        });
    
        done();
    });
    
    it('search box should have expected text', function(done) {
        var searchBox = driver.findElement(By.name('search_query'));
        searchBox.sendKeys('random text');
        searchBox.getAttribute('value').then(function(value) {
            assert.strictEqual(value, 'random text');
        });

        done();
    });

});

