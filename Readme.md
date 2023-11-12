### Install Appium 

1. Explanation link: https://medium.com/tauk-blog/quick-start-guide-for-setting-up-appium-on-an-m1-mac-a629a70a40cb
* Install xcode, android studio
* Install npm `brew install node`
* Install java `brew install java` (or set specific version of JDK)
* Install Appium: 
  * `npm i --location=global appium`
  * associate appium filename: `sudo ln -fs /opt/homebrew/Cellar/node/21.1.0/lib/node_modules/appium/build/lib/main.js /usr/local/bin/appium` add permissions `chmod +x /usr/local/bin/appium`
  * check appium is installed `appium -v`

### Appium usage
* Check available drivers list `appium driver list`
* Install a driver `appium driver install xcuitest`
* Start an Appium `appium`