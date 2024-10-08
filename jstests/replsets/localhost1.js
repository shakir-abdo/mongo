// Test ReplSet default initiate with localhost-only binding
// @tags: [multiversion_incompatible]

import {ReplSetTest} from "jstests/libs/replsettest.js";

// Select localhost when binding to localhost
const rt = new ReplSetTest({name: "rsLocal", nodes: 1});
const primary = rt.startSet({bind_ip: "127.0.0.1"})[0];
const db = primary.getDB('admin');
const resp = assert.commandWorked(db.adminCommand({replSetInitiate: undefined}));
assert(resp.me.startsWith('127.0.0.1'), tojson(resp.me) + " does not start with 127.0.0.1:");

// Wait for the primary to complete its election before shutting down the set.
assert.soon(() => db.runCommand({hello: 1}).isWritablePrimary);
rt.stopSet();