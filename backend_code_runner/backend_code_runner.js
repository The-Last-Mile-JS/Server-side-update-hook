var testCode = require('tape');
var unitTest = require("./unit_test");      // Unit tests
var code = require("../input");            // Written function


testCode(unitTest.testCodeString, { timeout: 10000 }, function (t) {
    var index;
    for (index = 0; index < unitTest.testCases.length; index += 1){
        t.equal(unitTest.answers[index], code.mainFunc(unitTest.testCases[index][0], unitTest.testCases[index][1]));
    }
    t.end();
});
