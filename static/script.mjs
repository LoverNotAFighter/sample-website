import{value} from './script2.mjs';
let rgstrdAcc;

function disp(){rgstrdAcc = window.rgstrdAccLoad; console.log(rgstrdAcc); console.log(value);}
setInterval(disp,1000);
