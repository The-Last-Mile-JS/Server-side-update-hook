var testCode = require('tape');
var unitTest = require('./unittest');
var fileName = process.argv[2];
var code = require("./" + fileName.substring(0, fileName.length-3));

testCode(unitTest.testCodeString, { timeout: 10000 }, function (t) {
    var index;
    for (index = 0; index < unitTest.testCases.length; index += 1){
        // console.log(`Test Case #${index}`, "\nInput(s):", unitTest.testCases[index]);
        t.equal(unitTest.answers[index], code.mainFunc(unitTest.testCases[index]));
    }
    console.log("yes");
    t.end();
});
