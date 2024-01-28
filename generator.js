var svgCaptcha = require('svg-captcha');
var fs = require('fs');
var svg2img = require('svg2img');
var num = 10000;//desired amount of captcha (10k is very good)
const FORMAT = 'webp';
const SIZE = [720, 360];
const out = './temp';
async function generate(){
    // process.stdout.write(`\r${num} left   `);
    var captcha = svgCaptcha.create({
        size: 4,
        noise: 1,
        color: true, 
        background: '#2E3137',
        width: SIZE[0],
        height: SIZE[1],
        fontSize: 160
    });
    svg2img(captcha.data,{ format: FORMAT }, function(error, buffer) {
        fs.writeFileSync(`${out}/${captcha.text}.${FORMAT}`, buffer);
        console.log(`${out}/${captcha.text}.${FORMAT}`);
    });
    if (num > 1){
        num--;
        await generate();
    }
}
async function main(){
    await generate();
}
main();
