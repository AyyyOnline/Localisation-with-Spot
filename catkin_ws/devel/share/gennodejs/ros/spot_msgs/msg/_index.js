
"use strict";

let LeaseResource = require('./LeaseResource.js');
let LeaseArray = require('./LeaseArray.js');
let EStopStateArray = require('./EStopStateArray.js');
let BatteryStateArray = require('./BatteryStateArray.js');
let EStopState = require('./EStopState.js');
let PowerState = require('./PowerState.js');
let WiFiState = require('./WiFiState.js');
let FootState = require('./FootState.js');
let Metrics = require('./Metrics.js');
let Lease = require('./Lease.js');
let FootStateArray = require('./FootStateArray.js');
let BehaviorFaultState = require('./BehaviorFaultState.js');
let BatteryState = require('./BatteryState.js');
let SystemFault = require('./SystemFault.js');
let SystemFaultState = require('./SystemFaultState.js');
let LeaseOwner = require('./LeaseOwner.js');
let Feedback = require('./Feedback.js');
let BehaviorFault = require('./BehaviorFault.js');

module.exports = {
  LeaseResource: LeaseResource,
  LeaseArray: LeaseArray,
  EStopStateArray: EStopStateArray,
  BatteryStateArray: BatteryStateArray,
  EStopState: EStopState,
  PowerState: PowerState,
  WiFiState: WiFiState,
  FootState: FootState,
  Metrics: Metrics,
  Lease: Lease,
  FootStateArray: FootStateArray,
  BehaviorFaultState: BehaviorFaultState,
  BatteryState: BatteryState,
  SystemFault: SystemFault,
  SystemFaultState: SystemFaultState,
  LeaseOwner: LeaseOwner,
  Feedback: Feedback,
  BehaviorFault: BehaviorFault,
};
