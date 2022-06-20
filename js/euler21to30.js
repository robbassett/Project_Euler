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

// This one is slow ~31 seconds
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

const euler24 = function() {
    t0 = performance.now();
    var a = [0,1,2,3,4,5,6,7,8,9];
    hg = utils.heaps(a).sort();
    t1 = performance.now();
    console.log('Euler #24: ' + hg[999999] + ' (' + (t1-t0) + ' ms)')
}

const euler25 = function(ndigit) {
    t0 = performance.now();
    var f1 = 1
    var f2 = 1
    var c = 2
    do {
        var f3 = f1
        f1 = f2
        f2 = BigInt(f3) + BigInt(f2)
        c += 1
    } while (String(f2).length < ndigit)
    t1 = performance.now();
    console.log('Euler #25: ' + c + ' (' + (t1-t0) + ' ms)')
}

const euler26 = function() {
    t0 = performance.now()
    var ans = 0
    var mx = 0
    for (let i = 2; i < 1000; i++){
        var t = 1
        var done = false
        var rl = 0
        var digits = []
        do {
            var r = t % i
            if (r == 0) {
                rl = 0
                done = true
            } else {
                if (!digits.includes(r)) {
                    digits.push(r)
                    t = 10*r
                } else {
                    done = true
                    rl = digits.length
                }
            }
        } while (!done)
        if (rl > mx) {
            mx = rl
            ans = i
        }
    }
    t1 = performance.now()
    console.log('Euler #26: ' + ans + ' (' + (t1-t0) + ' ms)')
}

const euler27 = function() {
    t0 = performance.now()
    var cprimes = utils.erasthenes(100000)
    var bprimes = utils.erasthenes(1000)
    var a0 = 0
    var b0 = 0
    var mx = 0
    for (let a = -1000; a <= 1000; a++) {
        for (b of bprimes) {
            var n = 0
            var done = false 
            do {
                n++
                if (!cprimes.includes(n*n + a*n + b)) {
                    done = true
                }
            } while (!done)
            if (n >= mx) {
                mx = n
                a0 = a
                b0 = b
            }
        }
    }
    ans = a0*b0
    t1 = performance.now()
    console.log('Euler #27: ' + ans + ' (' + (t1-t0) + ' ms)')
}

const euler28 = function(side) {
    t0 = performance.now()
    var ans = 1
    var step = 2
    var cv = 1
    while (step <= side) {
        for (let i = 0; i < 4; i++) {
            cv += step
            ans += cv
        }
        step += 2
    }
    t1 = performance.now()
    console.log('Euler #28: ' + ans + ' (' + (t1-t0) + ' ms)')
}

// euler21()
// euler22()
// euler23()
// euler24()
euler25(1000)
euler26()
//euler27()
euler28(1001)