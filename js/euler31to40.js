const performance = require('perf_hooks').performance;

utils = require('./utils.js')
data = require('./data.js')

const euler31 = function(total) {
    t0 = performance.now()
    const coins = [1,2,5,10,20,50,100,200];
    let combs = Array.from(Array(total+1), () => new Array(coins.length))
    for (let v = 0; v < total+1; v++) {
        var target = v + 1
        for (let i = 0; i < coins.length; i ++) {
            if (i == 0) {
                combs[v][i] = 1
            } else {
                var c = coins[i]
                if (c < target) {
                    var ind = target - c - 1
                    if (ind < 0) { ind += combs.length }
                    combs[v][i] = combs[v][i-1] + combs[ind][i]
                } else {
                    combs[v][i] = combs[v][i-1]
                }
            }
        }
    }
    ans = combs[total][coins.length-1]
    t1 = performance.now()
    console.log('Euler #31: ' + ans + ' (' + (t1-t0) + ' ms)')
}

const euler32 = function() {
    t0 = performance.now();
    const nums = utils.heaps([1,2,3,4,5,6,7,8,9]).sort()
    var prods = []
    for (var num of nums) {
        if (
            parseInt(num.slice(0,2))*parseInt(num.slice(2,5)) == parseInt(num.slice(5)) ||
            parseInt(num.slice(0,1))*parseInt(num.slice(1,5)) == parseInt(num.slice(5))
        ) {
            if (!prods.includes(parseInt(num.slice(5)))) {
                prods.push(parseInt(num.slice(5)))
            }
        }
    }
    ans = prods.reduce((p,a) => p + a, 0);
    t1 = performance.now();
    console.log('Euler #32: ' + ans + ' (' + (t1-t0) + ' ms)')
}

const euler33 = function() {
    t0 = performance.now();
    var np = 1
    var dp = 1
    for (let d = 11; d < 100; d++) {
        for (let n = 10; n < d; n++) {
            if (String(n)[0] == String(n)[1] | String(d)[0] == String(d)[1]) { continue }
            if (String(n)[1] == 0 & String(d)[1] == 0) { continue }
            for (var v of String(n)) {
                if (String(d).includes(v)) {
                    var re = new RegExp(v,'g')
                    var nn = parseInt(String(n).replace(re,''))
                    var dd = parseInt(String(d).replace(re,''))
                    if (n/d == nn/dd) {
                        if (nn != 1 & (dd/nn) % 1 == 0) {
                            dd /= nn
                            nn = 1
                        }
                        np *= nn
                        dp *= dd
                    }
                }
            }
        }
    }
    if (np != 1 & (dp/np) % 1 == 0) {
        ans = dp/np
    } else { ans = dp }
    t1 = performance.now();
    console.log('Euler #33: ' + ans + ' (' + (t1-t0) + ' ms)')
}

euler31(200)
euler32()
euler33()