// try reconfiguring with space at the end of the host:port

import {ReplSetTest} from "jstests/libs/replsettest.js";

var replTest = new ReplSetTest({name: 'testSet', nodes: 1});
var nodes = replTest.startSet();
replTest.initiate();

var primary = replTest.getPrimary();
var config = primary.getDB("local").system.replset.findOne();
config.version++;
var origHost = config.members[0].host;
config.members[0].host = origHost + " ";
var result = primary.adminCommand({replSetReconfig: config});
assert.eq(result.ok, 1, tojson(result));
// print("current (bad) config:"); printjson(config);

// check new config to make sure it doesn't have a space in the hostname
config = primary.getDB("local").system.replset.findOne();
assert.eq(origHost, config.members[0].host);
// print("current (good) config:"); printjson(config);

replTest.stopSet();
