const { Octokit, App } = require("@octokit/core");

const octokit = new Octokit({
    auth: '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'
})

const { createHash } = require('crypto');

function hash(string) {
    return createHash('sha256').update(string).digest('hex');
}

const header = `
<!DOCTYPE html>
<html>
<head>
    <script>MathJax={tex:{inlineMath:[['$','$'],['\\\\(','\\\\)']]},svg:{fontCache:'global'}}</script>
    <script type="text/javascript" id="MathJax-script" async="" src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
    <link href="./markdown.css" rel="stylesheet" />
</head>
<body>
`
const footer = `
</body>
`



var fs = require("fs");
const { stringify } = require("querystring");
var file = process.argv[2];
var raw = fs.readFileSync(file).toString('utf-8');

let escape = false;
let maths = [];
let mathMode = 0;
let content = "";
let mathcontent = "";
for (var i = 0; i < raw.length; i++) {

    if (!mathMode && !escape && raw[i] == '\\') {
        escape = true;
        content = content.concat(raw[i]);
    }
    else if (!escape && raw[i] == '$') {
        var diff = 0;
        if (i + 1 < raw.length && raw[i + 1] == '$') {
            diff = 2;
            mathcontent = mathcontent.concat('$$');
            i++;
        }
        else {
            diff = 1;
            mathcontent = mathcontent.concat(raw[i]);
        }
        mathMode ^= diff;
        if (mathMode == 0) {
            if (diff == 2)
                content = content.concat(`\n`);
            content = content.concat(`{{${hash(mathcontent)}}}`);
            if (diff == 2)
                content = content.concat(`\n`);
            maths.push(mathcontent);
            mathcontent = "";
        }
    }
    else if (mathMode) {
        mathcontent = mathcontent.concat(raw[i]);
    }
    else if (escape) {
        escape = false;
        content = content.concat(raw[i]);
    }
    else {
        content = content.concat(raw[i]);
    }
}

fs.writeFileSync("output.md", content);

/*await*/ octokit.request('POST /markdown', {
    text: content,
    headers: {
        'X-GitHub-Api-Version': '2022-11-28'
    }
}).then((response) => {
    content = response.data;
    for (var i = 0; i < maths.length; i++) {
        content = content.replace(`{{${hash(maths[i])}}}`, maths[i]);
    }

    fs.writeFileSync("output.html", header + content + footer);
})