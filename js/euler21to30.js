const performance = require('perf_hooks').performance;

utils = require('./utils.js')
data = require('./data.js')

const euler21 = function() {
    t0 = performance.now()
    var done = []
    for (let i = 12; i <= 10000; i++) {
        if (done.includes(i)) {continue}
        var tfs = utils.get_factors(i).reduce((p,a) => p + a, 0)-i
        var sft = utils.get_factors(tfs).reduce((p,a) => p + a, 0) - tfs
        if (sft == i && tfs != i) {
            done.push(sft)
            done.push(tfs)
        }
    }
    ans = done.reduce((p,a) => p + a, 0)
    t1 = performance.now()
    console.log('Euler #21: ' + ans + ' (' + (t1-t0) + ' ms)')
}

const euler22 = function() {
    t0 = performance.now()
    const alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    var ans = 0;
    const names = data.euler22.sort()
    for (let i = 0; i < names.length; i++) {
        var tscore = 0;
        for (let j = 0; j < names[i].length; j++) {
            tscore += alph.indexOf(names[i][j]) + 1
        }
        ans += tscore*(i+1);
    }
    t1 = performance.now()
    console.log('Euler #22: ' + ans + ' (' + (t1-t0) + ' ms)')
}

const euler23 = function() {
    t0 = performance.now();
    var abund_nums = [];
    var ans = 0
    for (let i = 12; i < 28123; i++) {
        if (utils.get_factors(i).reduce((p,a) => p + a, 0)-i > i) {abund_nums.push(i)}
    }
    for (let i = 0; i < 28123; i++) {
        var flag = 0
        for (let j = 0; j < abund_nums.length; j++) {
            if (abund_nums[j] > i/2) {break};
            if (abund_nums.includes(i-abund_nums[j])) {
                flag = 1;
                break
            };
        }
        if (flag == 0) {ans+=i}
    }
    t1 = performance.now()
    console.log('Euler #23: ' + ans + ' (' + (t1-t0) + ' ms)')
}

euler21()
euler22()
euler23()