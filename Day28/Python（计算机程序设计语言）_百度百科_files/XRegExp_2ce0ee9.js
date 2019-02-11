var XRegExp;if(XRegExp)throw Error("can't load XRegExp twice in the same frame");!function(e){function t(e,t){if(!XRegExp.isRegExp(e))throw TypeError("type RegExp expected");var r=e._xregexp;return e=XRegExp(e.source,n(e)+(t||"")),r&&(e._xregexp={source:r.source,captureNames:r.captureNames?r.captureNames.slice(0):null}),e}function n(e){return(e.global?"g":"")+(e.ignoreCase?"i":"")+(e.multiline?"m":"")+(e.extended?"x":"")+(e.sticky?"y":"")}function r(e,t,n,r){var a,p,i,c=s.length;l=!0;try{for(;c--;)if(i=s[c],n&i.scope&&(!i.trigger||i.trigger.call(r))&&(i.pattern.lastIndex=t,p=i.pattern.exec(e),p&&p.index===t)){a={output:i.handler.call(r,p,n),match:p};break}}catch(o){throw o}finally{l=!1}return a}function a(e,t,n){if(Array.prototype.indexOf)return e.indexOf(t,n);for(var r=n||0;r<e.length;r++)if(e[r]===t)return r;return-1}XRegExp=function(n,a){var i,s,o,g,x,h=[],d=XRegExp.OUTSIDE_CLASS,f=0;if(XRegExp.isRegExp(n)){if(a!==e)throw TypeError("can't supply flags when constructing one RegExp from another");return t(n)}if(l)throw Error("can't call the XRegExp constructor within token definition functions");for(a=a||"",i={hasNamedCapture:!1,captureNames:[],hasFlag:function(e){return a.indexOf(e)>-1},setFlag:function(e){a+=e}};f<n.length;)s=r(n,f,d,i),s?(h.push(s.output),f+=s.match[0].length||1):(o=c.exec.call(u[d],n.slice(f)))?(h.push(o[0]),f+=o[0].length):(g=n.charAt(f),"["===g?d=XRegExp.INSIDE_CLASS:"]"===g&&(d=XRegExp.OUTSIDE_CLASS),h.push(g),f++);return x=RegExp(h.join(""),c.replace.call(a,p,"")),x._xregexp={source:n,captureNames:i.hasNamedCapture?i.captureNames:null},x},XRegExp.version="1.5.1",XRegExp.INSIDE_CLASS=1,XRegExp.OUTSIDE_CLASS=2;var p=/[^gimy]+|([\s\S])(?=[\s\S]*\1)/g,i=/^(?:[?*+]|{\d+(?:,\d*)?})\??/,l=!1,s=[],c={exec:RegExp.prototype.exec,test:RegExp.prototype.test,match:String.prototype.match,replace:String.prototype.replace,split:String.prototype.split},o=c.exec.call(/()??/,"")[1]===e,g=function(){var e=/^/g;return c.test.call(e,""),!e.lastIndex}(),x=RegExp.prototype.sticky!==e,u={};u[XRegExp.INSIDE_CLASS]=/^(?:\\(?:[0-3][0-7]{0,2}|[4-7][0-7]?|x[\dA-Fa-f]{2}|u[\dA-Fa-f]{4}|c[A-Za-z]|[\s\S]))/,u[XRegExp.OUTSIDE_CLASS]=/^(?:\\(?:0(?:[0-3][0-7]{0,2}|[4-7][0-7]?)?|[1-9]\d*|x[\dA-Fa-f]{2}|u[\dA-Fa-f]{4}|c[A-Za-z]|[\s\S])|\(\?[:=!]|[?*+]\?|{\d+(?:,\d*)?}\??)/,XRegExp.addToken=function(e,n,r,a){s.push({pattern:t(e,"g"+(x?"y":"")),handler:n,scope:r||XRegExp.OUTSIDE_CLASS,trigger:a||null})},XRegExp.cache=function(e,t){var n=e+"/"+(t||"");return XRegExp.cache[n]||(XRegExp.cache[n]=XRegExp(e,t))},XRegExp.copyAsGlobal=function(e){return t(e,"g")},XRegExp.escape=function(e){return e.replace(/[-[\]{}()*+?.,\\^$|#\s]/g,"\\$&")},XRegExp.execAt=function(e,n,r,a){var p,i=t(n,"g"+(a&&x?"y":""));return i.lastIndex=r=r||0,p=i.exec(e),a&&p&&p.index!==r&&(p=null),n.global&&(n.lastIndex=p?i.lastIndex:0),p},XRegExp.freezeTokens=function(){XRegExp.addToken=function(){throw Error("can't run addToken after freezeTokens")}},XRegExp.isRegExp=function(e){return"[object RegExp]"===Object.prototype.toString.call(e)},XRegExp.iterate=function(e,n,r,a){for(var p,i=t(n,"g"),l=-1;p=i.exec(e);)n.global&&(n.lastIndex=i.lastIndex),r.call(a,p,++l,e,n),i.lastIndex===p.index&&i.lastIndex++;n.global&&(n.lastIndex=0)},XRegExp.matchChain=function(e,n){return function r(e,a){var p,i=n[a].regex?n[a]:{regex:n[a]},l=t(i.regex,"g"),s=[];for(p=0;p<e.length;p++)XRegExp.iterate(e[p],l,function(e){s.push(i.backref?e[i.backref]||"":e[0])});return a!==n.length-1&&s.length?r(s,a+1):s}([e],0)},RegExp.prototype.apply=function(e,t){return this.exec(t[0])},RegExp.prototype.call=function(e,t){return this.exec(t)},RegExp.prototype.exec=function(t){var r,p,i,l;if(this.global||(l=this.lastIndex),r=c.exec.apply(this,arguments)){if(!o&&r.length>1&&a(r,"")>-1&&(i=RegExp(this.source,c.replace.call(n(this),"g","")),c.replace.call((t+"").slice(r.index),i,function(){for(var t=1;t<arguments.length-2;t++)arguments[t]===e&&(r[t]=e)})),this._xregexp&&this._xregexp.captureNames)for(var s=1;s<r.length;s++)p=this._xregexp.captureNames[s-1],p&&(r[p]=r[s]);!g&&this.global&&!r[0].length&&this.lastIndex>r.index&&this.lastIndex--}return this.global||(this.lastIndex=l),r},RegExp.prototype.test=function(e){var t,n;return this.global||(n=this.lastIndex),t=c.exec.call(this,e),t&&!g&&this.global&&!t[0].length&&this.lastIndex>t.index&&this.lastIndex--,this.global||(this.lastIndex=n),!!t},String.prototype.split=function(t,n){if(!XRegExp.isRegExp(t))return c.split.apply(this,arguments);var r,a,p=this+"",i=[],l=0;if(n===e||0>+n)n=1/0;else if(n=Math.floor(+n),!n)return[];for(t=XRegExp.copyAsGlobal(t);(r=t.exec(p))&&!(t.lastIndex>l&&(i.push(p.slice(l,r.index)),r.length>1&&r.index<p.length&&Array.prototype.push.apply(i,r.slice(1)),a=r[0].length,l=t.lastIndex,i.length>=n));)t.lastIndex===r.index&&t.lastIndex++;return l===p.length?(!c.test.call(t,"")||a)&&i.push(""):i.push(p.slice(l)),i.length>n?i.slice(0,n):i},XRegExp.addToken(/\(\?#[^)]*\)/,function(e){return c.test.call(i,e.input.slice(e.index+e[0].length))?"":"(?:)"}),XRegExp.addToken(/\((?!\?)/,function(){return this.captureNames.push(null),"("}),XRegExp.addToken(/\(\?<([$\w]+)>/,function(e){return this.captureNames.push(e[1]),this.hasNamedCapture=!0,"("}),XRegExp.addToken(/\\k<([\w$]+)>/,function(e){var t=a(this.captureNames,e[1]);return t>-1?"\\"+(t+1)+(isNaN(e.input.charAt(e.index+e[0].length))?"":"(?:)"):e[0]}),XRegExp.addToken(/\[\^?]/,function(e){return"[]"===e[0]?"\\b\\B":"[\\s\\S]"}),XRegExp.addToken(/^\(\?([imsx]+)\)/,function(e){return this.setFlag(e[1]),""}),XRegExp.addToken(/(?:\s+|#.*)+/,function(e){return c.test.call(i,e.input.slice(e.index+e[0].length))?"":"(?:)"},XRegExp.OUTSIDE_CLASS,function(){return this.hasFlag("x")}),XRegExp.addToken(/\./,function(){return"[\\s\\S]"},XRegExp.OUTSIDE_CLASS,function(){return this.hasFlag("s")})}();