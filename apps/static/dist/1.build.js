(window.webpackJsonp=window.webpackJsonp||[]).push([[1],[,,,,,,,,,,,,function(t,e,s){var o=s(13);"string"==typeof o&&(o=[[t.i,o,""]]),o.locals&&(t.exports=o.locals);(0,s(5).default)("02cd9fce",o,!0,{})},function(t,e,s){(t.exports=s(4)(!1)).push([t.i,".clock{color:#c03763;font-size:48px;line-height:1.1em;margin:40px 0 60px}",""])},function(t,e,s){"use strict";var o={data:()=>({time:"00:00:00"}),mounted(){this.startTime()},methods:{startTime(){let t=new Date,e=t.getHours(),s=t.getMinutes(),o=t.getSeconds();s=this.checkTime(s),o=this.checkTime(o),this.time=e+":"+s+":"+o;setTimeout(this.startTime,500)},checkTime:t=>(t<10&&(t="0"+t),t)}},i=s(3);var n=function(t){s(12)},c=Object(i.a)(o,(function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"clock"},[e("h1",[this._v(this._s(this.time))])])}),[],!1,n,null,null);e.a=c.exports},function(t,e,s){var o=s(16);"string"==typeof o&&(o=[[t.i,o,""]]),o.locals&&(t.exports=o.locals);(0,s(5).default)("75b56f98",o,!0,{})},function(t,e,s){(t.exports=s(4)(!1)).push([t.i,"",""])},,,,,function(t,e,s){"use strict";s.r(e);var o=s(14);const i=io("localhost:5000");var n={data:()=>({msg:"Home"}),methods:{test(t){console.log("response :: ",t)}},mounted(){console.log("Mounted"),i.emit("my_event",{message:"test"}),i.on("my_response",t=>{console.log("response :: ",t)})},components:{Clock:o.a}},c=s(3);var l=function(t){s(15)},a=Object(c.a)(n,(function(){var t=this.$createElement;return(this._self._c||t)("h1",[this._v(this._s(this.msg))])}),[],!1,l,null,null);e.default=a.exports}]]);