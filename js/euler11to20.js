const performance = require('perf_hooks').performance;

utils = require('./utils.js')
data = require('./data.js')

const euler11 = function() {
    var t0 = performance.now()
    var mx = 0
    var d = data.euler11
    for (let i = 0; i < 20; i++) {
        for (let j = 0; j < 20; j++) {
            var s1 = []
            var s2 = []
            var s3 = []
            var s4 = []
            for (let k = 0; k < 4; k++) {
                if (j < 17) {
                    s1.push(d[i][j+k])
                } else {s1.push(0)}
                if (i < 17) {
                    s2.push(d[i+k][j])
                } else {s2.push(0)}
                if (i < 17 && j < 17) {
                    s3.push(d[i+k][j+k])
                } else {s3.push(0)}
                if (i > 3 && j < 17) {
                    s4.push(d[i-k][j+k])
                }
            }
            p1 = s1.reduce((psum,a) => psum * a, 1)
            p2 = s2.reduce((psum,a) => psum * a, 1)
            p3 = s3.reduce((psum,a) => psum * a, 1)
            p4 = s4.reduce((psum,a) => psum * a, 1)
            tmx = Math.max.apply(Math,[p1,p2,p3,p4])
            if (tmx > mx){
                mx = tmx
            }
        }
    }
    var t1 = performance.now()
    console.log('Euler #11: ' + mx + ' (' + (t1-t0) + ' ms)')
}

const euler12 = function(n) {
    const t0 = performance.now()
    var val = 1
    var cn = 1
    var facts = []
    do {
        cn ++
        val += cn
        facts = utils.get_factors(val)
    } while (facts.length < n);
    const t1 = performance.now()
    console.log('Euler #12: ' + val + ' (' + (t1-t0) + ' ms)')
}

const euler13 = function() {
    const t0 = performance.now()
    ans = String(data.euler13.reduce((a,b) => a + b, 0)).replace('.','').substring(0,10)
    const t1 = performance.now()
    console.log('Euler #13: ' + ans + ' (' + (t1-t0) + ' ms)')
}

const euler14 = function() {
    const t0 = performance.now()
    var maxlen = 1
    var ans = 0
    for (let curr = 13; curr <= 1e6; curr++){
        var clen = 1
        var n = curr
        do {
            if (n%2 == 0) {
                n = n/2
            } else { n = 3*n + 1 }
            clen++
        } while (n > 1);
        if (clen > maxlen) {
            maxlen = clen
            ans = curr
        }
    }
    const t1 = performance.now()
    console.log('Euler #14: ' + ans + ' (' + (t1-t0) + ' ms)')
}

const euler15 = function(N) {
    const t0 = performance.now();
    var row = [1,2];
    var prev = [...row]
    do {
        row = Array(row.length+1).fill(1)
        for (let i = 1; i < prev.length; i++){
            row[i] = row[i-1] + prev[i]
        }
        row[prev.length] = 2*row[prev.length-1]
        prev = [...row]
    } while (row.length < N+1);
    const t1 = performance.now();
    console.log('Euler #15: ' + row[row.length-1] + ' (' + (t1-t0) + ' ms)')
}

const euler16 = function(exp) {
    const t0 = performance.now();
    num = String(BigInt(2**exp))
    var ans = 0
    var i = num.length
    while (i--) {
        ans += parseInt(num.charAt(i))
    };
    const t1 = performance.now();
    
    console.log('Euler #16: ' + ans + ' (' + (t1-t0) + ' ms)')
}

const euler17 = function() {
    const t0 = performance.now()
    const count_dic = {
        1:3,
        2:3,
        3:5,
        4:4,
        5:4,
        6:3,
        7:5,
        8:5,
        9:4,
        10:3,
        11:6,
        12:6,
        13:8,
        14:8,
        15:7,
        16:7,
        17:9,
        18:8,
        19:8,
        20:6,
        30:6,
        40:5,
        50:5,
        60:5,
        70:7,
        80:6,
        90:6
    }
    var ans = 0
    for (let i = 1; i <= 1000; i ++) {
        num = String(i)
        if (i < 21) {
            ans += count_dic[i]
        } else {
            if (num.length == 2) {
                ans += count_dic[parseInt(num.charAt(0))*10]
                if (num.charAt(1) != '0') {
                    ans += count_dic[parseInt(num.charAt(1))]
                }
            } else {
                if (num.length == 3) {
                    ans += 7
                    ans += count_dic[parseInt(num.charAt(0))]
                    if (i%100 != 0) {
                        tens = num[1]+num[2]
                        if (parseInt(tens) < 21) {
                            ans += count_dic[parseInt(tens)]
                        } else {
                            ans += count_dic[parseInt(num.charAt(1))*10]
                            if (num.charAt(2) != '0') {
                                ans += count_dic[parseInt(num.charAt(2))]
                            }
                        }
                        ans += 3
                    }
                } else {ans += 'onethousand'.length}
            }
        }
    }
    const t1 = performance.now()
    console.log('Euler #17: ' + ans + ' (' + (t1-t0) + ' ms)')
}



const euler18 = function() {
    const t0 = performance.now()
    var e18 = data.euler18
    var prev = e18[e18.length-1]
    var i = e18.length-1
    while (i--) {
        var curr = e18[i]
        for (let j = 0; j < curr.length; j ++) {
            curr[j] = Math.max(curr[j]+prev[j],curr[j]+prev[j+1])
        }
        prev = [...curr]
    }
    const t1 = performance.now()
    console.log('Euler #18: ' + curr[0] + ' (' + (t1-t0) + ' ms)')
}

const euler19 = function() {
    const t0 = performance.now()
    var days = 1
    var count = 0
    for (let year = 1900; year < 2000; year ++) {
        for (let month = 1; month < 13; month ++) {
            if ([4,6,9,11].includes(month)) {
                days += 30
            } else {
                if (month != 2) {
                    days += 31
                } else {
                    days += 28
                    if (year%4 == 0) {days += 1}
                }
            }
            if (days%7 == 0) {count += 1}
        }
    }
    const t1 = performance.now()
    console.log('Euler #19: ' + count + ' (' + (t1-t0) + ' ms)')
}

const euler20 = function(N) {
    const t0 = performance.now()
    var num = String(utils.bigFactorial(N))
    var i = num.length-1
    var ans = parseInt(num.charAt(i))
    while (i--) {
        ans += parseInt(num.charAt(i))
    }
    const t1 = performance.now()
    console.log('Euler #20: ' + ans + ' (' + (t1-t0) + ' ms)')
}

euler11()
euler12(500)
euler13()
euler14()
euler15(20)
euler16(1000)
euler17()
euler18()
euler19()
euler20(100)