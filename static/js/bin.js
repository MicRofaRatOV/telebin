// import * as remarkable from 'https://cdnjs.cloudflare.com/ajax/libs/remarkable/2.0.0/remarkable.min.js';

/*
var md = new Remarkable('full', {
  html:         false,        // Enable HTML tags in source
  xhtmlOut:     false,        // Use '/' to close single tags (<br />)
  breaks:       false,        // Convert '\n' in paragraphs into <br>
  langPrefix:   'language-',  // CSS language prefix for fenced blocks
  linkify:      true,         // autoconvert URL-like texts to links
  linkTarget:   '',           // set target to open link in

  // Enable some language-neutral replacements + quotes beautification
  typographer:  false,

  // Double + single quotes replacement pairs, when typographer enabled,
  // and smartquotes on. Set doubles to '«»' for Russian, '„“' for German.
  quotes: '“”‘’',

  // Highlighter function. Should return escaped HTML,
  // or '' if input not changed
  highlight: function (str, lang) {
    if (lang && hljs.getLanguage(lang)) {
      try {
        return hljs.highlight(lang, str).value;
      } catch (__) {}
    }

    try {
      return hljs.highlightAuto(str).value;
    } catch (__) {}

    return ''; // use external default escaping
  }
});

// => <h1>Remarkable rulezz!</h1>

String.prototype.replaceAll = function(search, replacement) {
    var target = this;
    return target.replace(new RegExp(search, 'g'), replacement);
};
*/


// On click to pills
document.getElementById("home-pill").onclick = function () { location.href = "/"; };
document.getElementById("new-bin-pill").onclick = function () { location.href = "/new-bin/"; };
document.getElementById("my-bins-pill").onclick = function () { location.href = "/my-bins/"; };
document.getElementById("account-pill").onclick = function () { location.href = "/account/"; };
